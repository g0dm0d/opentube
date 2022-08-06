CREATE DATABASE /*!32312 IF NOT EXISTS*/ `opentube` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `opentube`;

CREATE TABLE users
(
 username    varchar(20) NOT NULL,
 password    varchar(128) NOT NULL,
 email       varchar(50) NOT NULL,
 create_date date NOT NULL,
 avatar      varchar(50) NOT NULL,
 CONSTRAINT PK_13 PRIMARY KEY ( username )
);

CREATE TABLE video
(
 "ID"          varchar(50) NOT NULL,
 title       varchar(50) NOT NULL,
 username    varchar(20) NOT NULL,
 description varchar(300) NOT NULL,
 view_count  integer NOT NULL,
 upload_date date NOT NULL,
 thumbnail   varchar(50) NOT NULL,
 CONSTRAINT PK_5 PRIMARY KEY ( "ID" ),
 CONSTRAINT FK_19 FOREIGN KEY ( username ) REFERENCES users ( username )
);

CREATE TABLE comments
(
 comment_id varchar(50) NOT NULL,
 text       varchar(300) NOT NULL,
 "ID"         varchar(50) NOT NULL,
 username   varchar(20) NOT NULL,
 CONSTRAINT PK_43 PRIMARY KEY ( comment_id ),
 CONSTRAINT FK_26 FOREIGN KEY ( username ) REFERENCES users ( username ),
 CONSTRAINT FK_31 FOREIGN KEY ( "ID" ) REFERENCES video ( "ID" )
);

CREATE TABLE viewed
(
 "ID"       varchar(50) NOT NULL,
 username varchar(20) NOT NULL,
 CONSTRAINT FK_36 FOREIGN KEY ( "ID" ) REFERENCES video ( "ID" ),
 CONSTRAINT FK_39 FOREIGN KEY ( username ) REFERENCES users ( username )
);

CREATE INDEX FK_38 ON viewed
(
 "ID"
);

CREATE INDEX FK_41 ON viewed
(
 username
);

CREATE INDEX FK_28 ON comments
(
 username
);

CREATE INDEX FK_33 ON comments
(
 "ID"
);

CREATE INDEX FK_21 ON video
(
 username
);