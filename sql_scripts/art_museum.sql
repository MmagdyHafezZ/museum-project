DROP DATABASE IF EXISTS art_museum;
CREATE DATABASE art_museum; 
USE art_museum;

DROP TABLE IF EXISTS exhibition;
CREATE TABLE exhibition
(
exhibition_name VARCHAR(70) NOT NULL,
start_date VARCHAR(20) NOT NULL,
end_date VARCHAR(20) NOT NULL,
PRIMARY KEY (exhibition_name)
);


DROP TABLE IF EXISTS artist;
CREATE TABLE artist
(
artist_name VARCHAR(30) NOT NULL,
date_born VARCHAR(20),
date_died VARCHAR(20),
epoch VARCHAR(20),
main_style VARCHAR(50),
artist_description VARCHAR(1000),
PRIMARY KEY (artist_name),
UNIQUE (artist_name)
);

DROP TABLE IF EXISTS art_object;
CREATE TABLE art_object
(
id_no VARCHAR(20) NOT NULL,
year_of_creation INT(4),
object_title VARCHAR(100) NOT NULL,
object_description VARCHAR(1000),
country_or_culture_of_origin VARCHAR(50),
epoch VARCHAR(20),
artist_name VARCHAR(30),
exhibition VARCHAR(70),
PRIMARY KEY (id_no),
UNIQUE (id_no),
foreign key(exhibition) references Exhibition(exhibition_name)
on update cascade
);

DROP TABLE IF EXISTS permanent_collection;
CREATE TABLE permanent_collection
(
id_no VARCHAR(20) NOT NULL,
date_aquired VARCHAR(20) NOT NULL,
object_status VARCHAR(20) NOT NULL,
cost VARCHAR(20) NOT NULL,
PRIMARY KEY (id_no),
FOREIGN KEY (id_no) REFERENCES art_object(id_no)
ON DELETE cascade
ON UPDATE CASCADE
);

DROP TABLE IF EXISTS collection;
CREATE TABLE collection
(
collection_name VARCHAR(100) NOT NULL,
collection_type VARCHAR(20) NOT NULL,
collection_description VARCHAR(1000) NOT NULL,
address VARCHAR(100) NOT NULL,
phone VARCHAR(20) NOT NULL,
contact_person  VARCHAR(20) NOT NULL,
PRIMARY KEY (collection_name),
UNIQUE (collection_name)
);

DROP TABLE IF EXISTS borrowed;
CREATE TABLE borrowed
(
id_no VARCHAR(20) NOT NULL,
date_borrowed VARCHAR(20) NOT NULL,
date_returned VARCHAR(20) NOT NULL,
PRIMARY KEY (id_no),
FOREIGN KEY (id_no) REFERENCES art_object(id_no)
ON DELETE cascade
ON UPDATE CASCADE
);

DROP TABLE IF EXISTS borrowed_from;
CREATE TABLE borrowed_from
(
id_no VARCHAR(20) NOT NULL,
collection_name VARCHAR(100) NOT NULL,
PRIMARY KEY (id_no,collection_name), 
FOREIGN KEY (id_no) REFERENCES borrowed(id_no),
FOREIGN KEY (collection_name) REFERENCES collection(collection_name)
ON DELETE cascade
ON UPDATE CASCADE
);

DROP TABLE IF EXISTS sculpture;
CREATE TABLE sculpture
(
id_no VARCHAR(20) NOT NULL,
weight VARCHAR(20) NOT NULL,
height VARCHAR(20) NOT NULL,
material VARCHAR(20) NOT NULL,
style VARCHAR(20) NOT NULL,
PRIMARY KEY (id_no),
FOREIGN KEY (id_no) REFERENCES art_object(id_no)
ON DELETE cascade
ON UPDATE CASCADE
);

DROP TABLE IF EXISTS statue;
CREATE TABLE statue
(
id_no VARCHAR(20) NOT NULL,
weight VARCHAR(20) NOT NULL,
height VARCHAR(20) NOT NULL,
material VARCHAR(20) NOT NULL,
style VARCHAR(20) NOT NULL,
PRIMARY KEY (id_no),
FOREIGN KEY (id_no) REFERENCES art_object(id_no)
ON DELETE cascade
ON UPDATE CASCADE
);

DROP TABLE IF EXISTS painting;
CREATE TABLE painting
(
id_no VARCHAR(20) NOT NULL,
style VARCHAR(20) NOT NULL,
paint_type VARCHAR(20) NOT NULL,
drawn_on VARCHAR(20) NOT NULL,
PRIMARY KEY (id_no),
FOREIGN KEY (id_no) REFERENCES art_object(id_no)
ON DELETE cascade
ON UPDATE CASCADE
);

DROP TABLE IF EXISTS other;
CREATE TABLE other
(
id_no VARCHAR(20) NOT NULL,
type_of_other VARCHAR(20) NOT NULL,
style VARCHAR(20) NOT NULL,
PRIMARY KEY (id_no),
FOREIGN KEY (id_no) REFERENCES art_object(id_no)
ON DELETE cascade
ON UPDATE CASCADE
);

INSERT INTO exhibition (exhibition_name, start_date, end_date)
Values
('The Tudors: Art and Majesty in Renaissance England','October 10, 2022','January 8, 2023'),
('Cubism and the Trompe l’Oeil Tradition','October 20, 2022','January 22, 2023'),
('Hear Me Now: The Black Potters of Old Edgefield, South Carolina','September 9, 2022','February 5, 2023');

INSERT INTO artist (artist_name, date_born, date_died, epoch, main_style, artist_description)
VALUES
('Benedetto da Rovezzano', '1474', '1552', 'Renaissance', 'Sculptures', 'Italian architect and sculptor who worked mainly in Florence.'),
('Hans Holbein the Younger','1497','1543','Renaissance','Paintings','Hans Holbein the Younger was a German-Swiss painter and printmaker. He is considered one of the greatest portraitists of the 16th century.'),
('Pablo Picasso','1881','1973','Modern','Cubism','Pablo Ruiz Picasso was a Spanish painter, sculptor, printmaker, ceramicist and theatre designer who spent most of his adult life in France.'),
('Georges Braque','1882','1963','Modern','Fauvist','Georges Braque was a major 20th-century French painter, collagist, draughtsman, printmaker and sculptor.'),
('Jefferson D. Chalfant','1856','1931','Modern','Still-life Paintings','Jefferson David Chalfant was an American painter who is remembered mostly for his still life paintings.'),
('Guillim Scrots',NULL,'1553','Renaissance','Mannerist','William Scrots was a painter of the Tudor court and an exponent of the Mannerist style of painting in the Netherlands.'),
('Affabel Partridge',NULL,'1583','Renaissance','Jewlery','Affabel Partridge was a London goldsmith who served Elizabeth I.'),
('Simone Leigh','1967',NULL,'Modern','Traditional and Cultural','Simone Leigh is an American artist from Chicago who works in New York City in the United States.'),
('Theaster Gates','1973',NULL,'Modern','Installation','Theaster Gates is an American social practice installation artist and a professor in the Department of Visual Arts at the University of Chicago.'),
('Gaspard van Wittel','1652','1736','Baroque','Paintings','Dutch painter/draughtsman who had a long career in Rome. He played a pivotal role in the development of the genre of painting known as veduta.'),
('Giovanni Paolo Panini','1691','1756','Baroque','Paintings','Italian painter and architect who worked in Rome and is primarily known as one of the vedutisti (view painters).'),
('Eugenio Landesio','1810','1879','Realistic','Paintings','Italian painter and a pupil of the Hungarian landscape painter Károly Markó the Elder. Influenced later exponents of Mexican landscape painting.'),
('John II Cleveley','1747','1786','Neoclassical','Paintings','He trained under the artist Paul Sandby at Woolwich. His sketches were worked into watercolour, some of which were placed with the British Museum.'),
('Jakob Blanck','1650','1740','Baroque','Chests','He was a prominent figure in his time with his skills of chest making.'),
('Paolo Veronese','1528','1588','Renaissance','Paintings','Italian Renaissance painter based in Venice, known for extremely large history paintings of religion and mythology, such as The Wedding at Cana (1563).');


INSERT INTO art_object (id_no, year_of_creation, object_title, object_description, country_or_culture_of_origin,epoch, artist_name,exhibition)
Values
('001',1524,'Angel Bearing Candlestick','Statue','Italian','Renaissance','Benedetto da Rovezzano','The Tudors: Art and Majesty in Renaissance England'),
('002',1500,'Candelabrum','statue','Italian','Renaissance','Benedetto da Rovezzano','The Tudors: Art and Majesty in Renaissance England'),
('003',1537,'Henry VIII', 'Painting_Oil_On_Panel' , 'German','Renaissance','Hans Holbein the Younger','The Tudors: Art and Majesty in Renaissance England'),
('004',1544,'Field Armor of King Henry VIII of England','statue','Italian, Milan or Brescia','Renaissance','Hans Holbein the Younger','The Tudors: Art and Majesty in Renaissance England'),
('005',1912,'Still Life with Chair Caning','Painting_Oil_On_Canvas','Spanish','Modern','Pablo Picasso','Cubism and the Trompe l’Oeil Tradition'),
('006',1909,'Violin and Palette','Painting_Oil_On_Canvas','French','Modern','Georges Braque','Cubism and the Trompe l’Oeil Tradition'),
('007',1890,'Which is Which?','Painting_Oil_On_Woodpanel','American','Modern','Jefferson D. Chalfant', 'Cubism and the Trompe l’Oeil Tradition'),
('008',1547,'Edward VI', 'Painting_Oil_On_Panel', 'Felmish', 'Renaissance','Guillim Scrots','The Tudors: Art and Majesty in Renaissance England'),
('009',1562,'Ewer', 'Sculpture','British','Renaissance','Affabel Partridge','The Tudors: Art and Majesty in Renaissance England'),
('010',1590,'Cup With Cover','Sculpture','British','Renaissance',NULL,'The Tudors: Art and Majesty in Renaissance England'),
('011',1914,'Still Life with a Bottle, Playing Cards, and a Wineglass on a Table','Painting_Oil_On_Woodpanel','Spanish','Modern','Pablo Picasso','Cubism and the Trompe l’Oeil Tradition'),
('012',1914,'The Absinthe Glass','Sculpture','Spanish','Modern','Pablo Picasso','Cubism and the Trompe l’Oeil Tradition'),
('013',1914,'Still Life','Sculpture','Spanish','Modern','Pablo Picasso','Cubism and the Trompe l’Oeil Tradition'),
('014',1850,'Face jug','Other','American','Modern',NULL,'Hear Me Now: The Black Potters of Old Edgefield, South Carolina'),
('015',1850,'Face Cup','Other','American','Modern',NULL,'Hear Me Now: The Black Potters of Old Edgefield, South Carolina'),
('016',1850,'Power figure','Sculpture','Kongo','Modern','Vili','Hear Me Now: The Black Potters of Old Edgefield, South Carolina'),
('017',2020,'Signature Study','Sculpture','American','Modern','Theaster Gates','Hear Me Now: The Black Potters of Old Edgefield, South Carolina'),
('018',1700,'View of the Port of Messina','Painting_Oil_On_Canvas','Italy','Baroque','Gaspard van Wittel',NULL),
('019',1740,'View of the Forum in Rome','Painting_Oil_On_Canvas','Italy','Baroque','Giovanni Paolo Panini',NULL), 
('020',1857,'View of Real del Monte, province of Hidalgo (Mexico)','Painting_Oil_On_Canvas','Italy','Realistic','Eugenio Landesio',NULL),
('021',1764,'View of the Thames','Painting_Oil_On_Canvas','England','Neoclassical','John II Cleveley',NULL), 
('022',1675,'Chest of jewels of Louis XIV','Chest','France','Baroque','Jacob Blanck',NULL), 
('023',1600,'The Wedding at Cana','Painting_Oil_On_Canvas','Italy','Renaissance','Paolo Veronese',NULL);

INSERT INTO statue (id_no, weight, height, material, style) VALUES 
('001','141','101','Bronze','Renaissance'), 
('002','622','340','Bronze','Renaissance'), 
('004','22.91','184.2','Steel','Medeival');

INSERT INTO sculpture(id_no,weight,height,material,style) 
Values 
('009',0.4,22.5,'silver','British'), 
('010',0.34,19.7,'silver','British'), 
('012',2,22.5,'bronze','Spanish'), 
('013',3,6,'wood','Spanich'), 
('016',18.1,103,'iron and wood','Kongo'), 
('017',40,54.9,'iron and wood','Kongo');

INSERT INTO painting (id_no, style, paint_type, drawn_on)
VALUES
('003','Renaissance','Oil','Panel'),
('005','Modern','Oil','Canvas'),
('006','Modern','Oil','Canvas'),
('007','Modern','Oil','Woodpanel'),
('008','Rensaissance','Oil','Panel'),
('011','Modern','Oil','Woodpanel'),
('018', 'Baroque', 'Oil', 'Canvas'),
('019', 'Baroque', 'Oil', 'Canvas'),
('020', 'Realistic', 'Oil', 'Canvas'),
('021', 'Neoclassical', 'Oil', 'Woodpanel'),
('023', 'Renaissance', 'Oil', 'Panel');


INSERT INTO other (id_no, type_of_other, style) 
VALUES 
('014','Jug','Modern'), 
('015','Cup','Modern'), 
('022', 'Chest', 'Baroque');

INSERT INTO collection (collection_name, collection_type, collection_description,address,phone,contact_person)
Values
('National Museums Recovery','Historical Antiques','Artifacts recovered after WWII that were retrieved in Germany and brought back to France.', '1000 Fifth Avenue at 82nd Street New York, NY 10028', '212-535-7710', 'Janina Poskrobko'), 
('Masterpieces of the Louvre', 'Historical Antiques', 'Collection with a wide range of artistic practices used around the world.', '1000 Fifth Avenue at 82nd Street New York, NY 10028', '212-535-7710', 'Janina Poskrobko');

INSERT INTO borrowed (id_no, date_borrowed, date_returned) 
Values 
('018', 'January 6, 1951', 'July 6, 2022'), 
('019', 'June 29, 2018', 'January 13, 2019'), 
('020', 'October 30, 1990', 'January 3, 2000'), 
('021', 'July 6, 1880', 'March 12, 2009'), 
('022', 'June 11, 1997', 'September 1, 2022'), 
('023', 'July 22,1995', 'November 5, 2007');

INSERT INTO borrowed_from (id_no, collection_name)
Values
('018', 'National Museums Recovery'), 
('019', 'National Museums Recovery'), 
('020', 'National Museums Recovery'), 
('021', 'National Museums Recovery'), 
('022', 'Masterpieces of the Louvre'), 
('023', 'Masterpieces of the Louvre');
INSERT INTO permanent_collection (id_no,date_aquired,object_status,cost)
Values
('001', 'January 13, 1993 ', 'on loan', '10000'),
('002', 'March, 17 1990', 'on display', '74850'),
('003',  'April 12, 1998', 'on display', '1100000' ),
('004', 'April 14, 2004', 'stored', '24000'),
('005', 'December 8, 1899', 'stored', '63000000'),
('006', 'November 7, 1998', 'on display', '20000'),
('007', 'August 30, 1992', 'on display', '30000'),
('008', 'May 5, 2003', 'on loan', '1000000'),
('009', 'May 21, 1994', 'on loan', '34000'),
('010','July 23, 1891', 'on display', '65000'),
('011', 'November 20, 1880', 'on display', '58000000'),
('012', 'February 8, 1889 ', 'on display', '69000000'),
('013', 'June 22, 1990', 'on loan', '61000000'),
('014', 'October 25, 1999', 'on loan', '2000000'),
('015', 'January 2, 1888', 'on display', '8000000'),
('016', 'October 9, 2000', 'stored', '5500000'),
('017', 'July 5, 2002', 'on display', '2163000');


