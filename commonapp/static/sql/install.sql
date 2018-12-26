(djenv) I:\venv\workspace\working\common>python manage.py sqlmigrate commonapp 0001
BEGIN;
--
-- Create model Choice
--
CREATE TABLE "commonapp_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL);
--
-- Create model Question
--
CREATE TABLE "commonapp_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT);
--
-- Add field question to choice
--
ALTER TABLE "commonapp_choice" RENAME TO "commonapp_choice__old";
CREATE TABLE "commonapp_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL, "question_id" integer NOT NULL REFERENCES "commonapp_question" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "commonapp_choice" ("id", "choice_text", "votes", "question_id") SELECT "id", "choice_text", "votes", NULL FROM "commonapp_choice__old";
DROP TABLE "commonapp_choice__old";
CREATE INDEX "commonapp_choice_question_id_67b7d025" ON "commonapp_choice" ("question_id");
COMMIT;