CREATE TABLE test_table (
    id SERIAL PRIMARY KEY,
    key VARCHAR(256) NOT NULL,
    value VARCHAR(256)
);

INSERT INTO test_table (key, value)
VALUES
('Hello', 'World'),
('SampleKey1', 'SampleValue1'),
('SampleKey2', 'SampleValue2'),
('SampleKey3', 'SampleValue3'),
('SampleKey4', 'SampleValue4');
