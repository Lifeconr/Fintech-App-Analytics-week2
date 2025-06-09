-- Check current user
SHOW USER;

-- Check PDBs and their status
SELECT name, open_mode FROM v$pdbs;

-- Switch to XEPDB1 if not already there
ALTER SESSION SET CONTAINER = XEPDB1;

-- Confirm current container
SELECT SYS_CONTEXT('USERENV', 'CON_NAME') FROM dual;

-- OPTIONAL: Drop existing tables to avoid conflicts (ONLY FOR CLEAN SETUP)
BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE reviews CASCADE CONSTRAINTS';
EXCEPTION WHEN OTHERS THEN
    IF SQLCODE != -942 THEN RAISE; END IF;
END;
/

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE banks CASCADE CONSTRAINTS';
EXCEPTION WHEN OTHERS THEN
    IF SQLCODE != -942 THEN RAISE; END IF;
END;
/

-- Create tables under your application user (not SYS ideally)
CREATE TABLE banks (
    bank_id VARCHAR2(10) PRIMARY KEY,
    bank_name VARCHAR2(50) NOT NULL,
    app_id VARCHAR2(50) UNIQUE
);

CREATE TABLE reviews (
    review_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    bank_id VARCHAR2(10) REFERENCES banks(bank_id),
    review_text VARCHAR2(1000) NOT NULL,
    rating NUMBER(1) CHECK (rating BETWEEN 1 AND 5),
    date_posted DATE NOT NULL,
    source VARCHAR2(50) NOT NULL,
    sentiment_label VARCHAR2(20),
    sentiment_score NUMBER(5,4),
    themes VARCHAR2(200)
);

-- Insert banks with MERGE to avoid duplicates
MERGE INTO banks b
USING (SELECT 'CBE' AS bank_id, 'Commercial Bank of Ethiopia' AS bank_name, 'com.combanketh.mobilebanking' AS app_id FROM dual) incoming
ON (b.bank_id = incoming.bank_id)
WHEN NOT MATCHED THEN
  INSERT (bank_id, bank_name, app_id)
  VALUES (incoming.bank_id, incoming.bank_name, incoming.app_id);

MERGE INTO banks b
USING (SELECT 'BOA' AS bank_id, 'Bank of Abyssinia' AS bank_name, 'com.boa.boaMobileBanking' AS app_id FROM dual) incoming
ON (b.bank_id = incoming.bank_id)
WHEN NOT MATCHED THEN
  INSERT (bank_id, bank_name, app_id)
  VALUES (incoming.bank_id, incoming.bank_name, incoming.app_id);

MERGE INTO banks b
USING (SELECT 'DASHEN' AS bank_id, 'Dashen Bank' AS bank_name, 'com.dashen.dashensuperapp' AS app_id FROM dual) incoming
ON (b.bank_id = incoming.bank_id)
WHEN NOT MATCHED THEN
  INSERT (bank_id, bank_name, app_id)
  VALUES (incoming.bank_id, incoming.bank_name, incoming.app_id);

-- Commit your inserts
COMMIT;

-- Verify table creation and data
SELECT table_name FROM user_tables;
SELECT owner, table_name FROM all_tables WHERE table_name = 'REVIEWS';
SELECT * FROM banks;
SELECT COUNT(*) FROM reviews;