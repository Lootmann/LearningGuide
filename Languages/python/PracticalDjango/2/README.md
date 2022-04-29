# ORM



## sql migrate1

```
$ python3 manage.py sqlmigrate snippets 0001_initial

BEGIN;
--
-- Create model Snippet
--
CREATE TABLE "snippets_snippet" (
  # created automatically !
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "title" varchar(128) NOT NULL,
  "code" text NOT NULL,
  "description" text NOT NULL,
  "created_at" datetime NOT NULL,
  "updated_at" datetime NOT NULL,
  "created_by_id" bigint NOT NULL REFERENCES "accounts_customuser" ("id") DEFERRABLE INITIALLY DEFERRED
  );

CREATE INDEX "snippets_snippet_created_by_id_a14886ce" ON "snippets_snippet" ("created_by_id");
COMMIT;
```



## sqlmigrate2

```
$ python3 manage.py sqlmigrate snippets 0002_alter_snippet_options_alter_snippet_table

BEGIN;
--
-- Change Meta options on snippet
--
--
-- Rename table for snippet to snippets
--
ALTER TABLE "snippets_snippet" RENAME TO "snippets";
COMMIT;
```



## sqlmigrate3

```
❯ python3 manage.py sqlmigrate snippets 0003_tag_comment

BEGIN;
--
-- Create model Tag
--
CREATE TABLE "tags" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "name" varchar(32) NOT NULL
  );


# middle table
CREATE TABLE "tags_snippets" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "tag_id" bigint NOT NULL REFERENCES "tags" ("id") DEFERRABLE INITIALLY DEFERRED,
  "snippet_id" bigint NOT NULL REFERENCES "snippets" ("id") DEFERRABLE INITIALLY DEFERRED
  );

--
-- Create model Comment
--
CREATE TABLE "comments" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "text" text NOT NULL, "commented_to_id" bigint NOT NULL REFERENCES "snippets" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "tags_snippets_tag_id_snippet_id_2243bbc3_uniq" ON "tags_snippets" ("tag_id", "snippet_id");
CREATE INDEX "tags_snippets_tag_id_ef38fad9" ON "tags_snippets" ("tag_id");
CREATE INDEX "tags_snippets_snippet_id_9b74bed5" ON "tags_snippets" ("snippet_id");
CREATE INDEX "comments_commented_to_id_cf72b868" ON "comments" ("commented_to_id");
COMMIT;
```
