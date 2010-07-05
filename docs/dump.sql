BEGIN TRANSACTION;
CREATE TABLE "auth_user" (
    "id" integer NOT NULL PRIMARY KEY,
    "username" varchar(30) NOT NULL UNIQUE,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL,
    "email" varchar(75) NOT NULL,
    "password" varchar(128) NOT NULL,
    "is_staff" bool NOT NULL,
    "is_active" bool NOT NULL,
    "is_superuser" bool NOT NULL,
    "last_login" datetime NOT NULL,
    "date_joined" datetime NOT NULL
);
INSERT INTO "auth_user" VALUES(1,'admin','','','admin@admin.com','sha1$0c047$afd64e0423e4e73a01734502e764c91b431232d3',1,1,1,'2010-07-05 17:12:17.245627','2010-07-05 17:12:17.245627');
CREATE TABLE "django_content_type" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(100) NOT NULL,
    "app_label" varchar(100) NOT NULL,
    "model" varchar(100) NOT NULL,
    UNIQUE ("app_label", "model")
);
INSERT INTO "django_content_type" VALUES(1,'log entry','admin','logentry');
INSERT INTO "django_content_type" VALUES(2,'permission','auth','permission');
INSERT INTO "django_content_type" VALUES(3,'group','auth','group');
INSERT INTO "django_content_type" VALUES(4,'user','auth','user');
INSERT INTO "django_content_type" VALUES(5,'message','auth','message');
INSERT INTO "django_content_type" VALUES(6,'content type','contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES(7,'session','sessions','session');
INSERT INTO "django_content_type" VALUES(8,'registration profile','registration','registrationprofile');
INSERT INTO "django_content_type" VALUES(9,'user profile','places','userprofile');
INSERT INTO "django_content_type" VALUES(10,'category','places','category');
INSERT INTO "django_content_type" VALUES(11,'asset','places','asset');
INSERT INTO "django_content_type" VALUES(12,'place','places','place');
INSERT INTO "django_content_type" VALUES(13,'favorite','places','favorite');
INSERT INTO "django_content_type" VALUES(14,'photo','places','photo');
INSERT INTO "django_content_type" VALUES(15,'storage','easy_thumbnails','storage');
INSERT INTO "django_content_type" VALUES(16,'source','easy_thumbnails','source');
INSERT INTO "django_content_type" VALUES(17,'thumbnail','easy_thumbnails','thumbnail');
CREATE TABLE "django_session" (
    "session_key" varchar(40) NOT NULL PRIMARY KEY,
    "session_data" text NOT NULL,
    "expire_date" datetime NOT NULL
);
CREATE TABLE "registration_registrationprofile" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id"),
    "activation_key" varchar(40) NOT NULL
);
CREATE TABLE "places_userprofile" (
    "id" integer NOT NULL PRIMARY KEY,
    "firstname" varchar(30) NOT NULL,
    "lastname" varchar(30) NOT NULL,
    "home_address" varchar(30) NOT NULL,
    "phone_number" varchar(12) NOT NULL,
    "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id"),
    "public_profile_field" bool NOT NULL
);
CREATE TABLE "places_category" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(100) NOT NULL,
    "description" text NOT NULL
);
CREATE TABLE "places_asset" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(30) NOT NULL
);
CREATE TABLE "places_place_assets" (
    "id" integer NOT NULL PRIMARY KEY,
    "place_id" integer NOT NULL,
    "asset_id" integer NOT NULL REFERENCES "places_asset" ("id"),
    UNIQUE ("place_id", "asset_id")
);
CREATE TABLE "places_place" (
    "id" integer NOT NULL PRIMARY KEY,
    "address" varchar(50) NOT NULL,
    "zipcode" integer NOT NULL,
    "city" varchar(50) NOT NULL,
    "country" varchar(50) NOT NULL,
    "latitude" real NOT NULL,
    "longitude" real NOT NULL,
    "action" varchar(1) NOT NULL,
    "price" integer unsigned NOT NULL,
    "area" integer unsigned NOT NULL,
    "year" integer unsigned NOT NULL,
    "description" text NOT NULL,
    "submitter_id" integer NOT NULL REFERENCES "auth_user" ("id"),
    "category_id" integer NOT NULL REFERENCES "places_category" ("id"),
    "pub_date" datetime NOT NULL,
    "published" bool NOT NULL,
    "hits" integer NOT NULL
);
CREATE TABLE "places_favorite" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL REFERENCES "auth_user" ("id"),
    "place_id" integer NOT NULL REFERENCES "places_place" ("id")
);
CREATE TABLE "places_photo" (
    "id" integer NOT NULL PRIMARY KEY,
    "place_id" integer NOT NULL REFERENCES "places_place" ("id"),
    "pic" varchar(100) NOT NULL
);
CREATE INDEX "places_place_assets_c4391d6c" ON "places_place_assets" ("place_id");
CREATE INDEX "places_place_assets_89694383" ON "places_place_assets" ("asset_id");
CREATE INDEX "places_place_1a37f020" ON "places_place" ("submitter_id");
CREATE INDEX "places_place_42dc49bc" ON "places_place" ("category_id");
CREATE INDEX "places_favorite_fbfc09f1" ON "places_favorite" ("user_id");
CREATE INDEX "places_favorite_c4391d6c" ON "places_favorite" ("place_id");
CREATE INDEX "places_photo_c4391d6c" ON "places_photo" ("place_id");
COMMIT;