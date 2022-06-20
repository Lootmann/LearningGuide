-----------------------
--- TABLE ice
-----------------------
CREATE TABLE IF NOT EXISTS ice (
  id        SERIAL NOT NULL,
  name      VARCHAR(30),
  kind      VARCHAR(30),
  calorie   INTEGER,

  PRIMARY KEY (id)
);


-----------------------
--- INSERT INTO ice
-----------------------
INSERT INTO ice (name, kind, calorie) VALUES
  ('common men',       'SuperMan',   151),
  ('Vinnila',          'TimBrrah',   158),
  ('locky load',       'THE 31',     162),
  ('Nuts To You',      'Elegant',    168),
  ('Choped Chocolate', 'CHOCOLATE',  175),
  ('Vannila',          'Kentaccky',  186),
  ('Baginner',         'Washington', 199)
;


--- select
SELECT distinct i1.name, i2.name, i1.kind, i1.calorie + i2.calorie AS cal
  FROM ice i1, ice i2
  WHERE i1.id != i2.id
;


--- select
SELECT i1.name, i2.name, i1.calorie + i2.calorie AS CAL
  FROM ice i1, ice i2
  WHERE (i1.id != i2.id)
    AND (i1.calorie + i2.calorie <= 350)
    AND 'Elegant' IN (i1.kind, i2.kind)
  ORDER BY CAL ASC
;


--- select
SELECT i1.name, i2.name, i3.name, i1.calorie + i2.calorie + i3.calorie AS CAL
  FROM ice i1, ice i2, ice i3
  WHERE (i1.id != i2.id AND i2.id != i3.id AND i3.id != i1.id)
    AND (i1.calorie + i2.calorie + i3.calorie <= 510)
    AND 'Elegant' IN (i1.kind, i2.kind, i3.kind)
  ORDER BY CAL ASC
;
