CREATE TABLE "room_type"(
	"listing_id" int NOT NULL,
	"room_type" varchar(200) NOT NULL,
	 CONSTRAINT "pk_room_type" PRIMARY KEY (
        "listing_id"
		)
);

CREATE TABLE "prices"(
	"listing_id" int NOT NULL,
	"listing_price" Varchar(200) NOT NULL,
	"borough" varchar(200) NOT NULL,
	"neighborhood" varchar(200) NOT NULL,
	CONSTRAINT "pk_prices" PRIMARY KEY (
        "listing_id"
		)
);