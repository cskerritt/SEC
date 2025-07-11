#!/usr/bin/env python3
"""
Generate business valuation analyst pages for top 15 cities in all 50 states
"""
import os
import json
from datetime import datetime

# Top 15 cities by population for each state
CITIES_BY_STATE = {
    'AL': [
        ('Birmingham', 'al', 33.5186, -86.8104),
        ('Montgomery', 'al', 32.3617, -86.2792),
        ('Mobile', 'al', 30.6944, -88.0431),
        ('Huntsville', 'al', 34.7304, -86.5861),
        ('Tuscaloosa', 'al', 33.2098, -87.5692),
        ('Hoover', 'al', 33.4053, -86.8111),
        ('Dothan', 'al', 31.2232, -85.3905),
        ('Decatur', 'al', 34.6059, -86.9833),
        ('Auburn', 'al', 32.6010, -85.4808),
        ('Madison', 'al', 34.6993, -86.7483),
        ('Florence', 'al', 34.7998, -87.6773),
        ('Gadsden', 'al', 34.0143, -86.0066),
        ('Vestavia Hills', 'al', 33.4487, -86.7872),
        ('Prattville', 'al', 32.4640, -86.4597),
        ('Phenix City', 'al', 32.4709, -85.0008)
    ],
    'AK': [
        ('Anchorage', 'ak', 61.2181, -149.9003),
        ('Fairbanks', 'ak', 64.8401, -147.7200),
        ('Juneau', 'ak', 58.3019, -134.4197),
        ('Wasilla', 'ak', 61.5819, -149.4394),
        ('Sitka', 'ak', 57.0531, -135.3300),
        ('Ketchikan', 'ak', 55.3422, -131.6461),
        ('Kenai', 'ak', 60.5544, -151.2583),
        ('Kodiak', 'ak', 57.7900, -152.4072),
        ('Bethel', 'ak', 60.7922, -161.7558),
        ('Palmer', 'ak', 61.5997, -149.1128),
        ('Homer', 'ak', 59.6425, -151.5483),
        ('Soldotna', 'ak', 60.4878, -151.0581),
        ('Valdez', 'ak', 61.1308, -146.3483),
        ('Unalaska', 'ak', 53.8758, -166.5347),
        ('Nome', 'ak', 64.5011, -165.4064)
    ],
    'AZ': [
        ('Phoenix', 'az', 33.4484, -112.0740),
        ('Tucson', 'az', 32.2226, -110.9747),
        ('Mesa', 'az', 33.4152, -111.8315),
        ('Chandler', 'az', 33.3062, -111.8413),
        ('Scottsdale', 'az', 33.4942, -111.9261),
        ('Glendale', 'az', 33.5387, -112.1860),
        ('Gilbert', 'az', 33.3528, -111.7890),
        ('Tempe', 'az', 33.4255, -111.9400),
        ('Peoria', 'az', 33.5806, -112.2374),
        ('Surprise', 'az', 33.6292, -112.3679),
        ('Yuma', 'az', 32.6927, -114.6277),
        ('Avondale', 'az', 33.4356, -112.3496),
        ('Flagstaff', 'az', 35.1983, -111.6513),
        ('Goodyear', 'az', 33.4355, -112.3576),
        ('Buckeye', 'az', 33.3703, -112.5838)
    ],
    'AR': [
        ('Little Rock', 'ar', 34.7465, -92.2896),
        ('Fayetteville', 'ar', 36.0625, -94.1574),
        ('Fort Smith', 'ar', 35.3859, -94.3985),
        ('Springdale', 'ar', 36.1867, -94.1288),
        ('Jonesboro', 'ar', 35.8423, -90.7043),
        ('North Little Rock', 'ar', 34.7695, -92.2671),
        ('Conway', 'ar', 35.0887, -92.4421),
        ('Rogers', 'ar', 36.3320, -94.1185),
        ('Pine Bluff', 'ar', 34.2284, -92.0032),
        ('Bentonville', 'ar', 36.3729, -94.2088),
        ('Hot Springs', 'ar', 34.5037, -93.0552),
        ('Benton', 'ar', 34.5645, -92.5868),
        ('Sherwood', 'ar', 34.8148, -92.2243),
        ('Texarkana', 'ar', 33.4418, -94.0377),
        ('Jacksonville', 'ar', 34.8665, -92.1101)
    ],
    'CA': [
        ('Los Angeles', 'ca', 34.0522, -118.2437),
        ('San Diego', 'ca', 32.7157, -117.1611),
        ('San Jose', 'ca', 37.3382, -121.8863),
        ('San Francisco', 'ca', 37.7749, -122.4194),
        ('Fresno', 'ca', 36.7378, -119.7871),
        ('Sacramento', 'ca', 38.5816, -121.4944),
        ('Long Beach', 'ca', 33.7701, -118.1937),
        ('Oakland', 'ca', 37.8044, -122.2712),
        ('Bakersfield', 'ca', 35.3733, -119.0187),
        ('Anaheim', 'ca', 33.8366, -117.9143),
        ('Santa Ana', 'ca', 33.7455, -117.8677),
        ('Riverside', 'ca', 33.9533, -117.3962),
        ('Stockton', 'ca', 37.9577, -121.2908),
        ('Irvine', 'ca', 33.6846, -117.8265),
        ('Chula Vista', 'ca', 32.6401, -117.0842)
    ],
    'CO': [
        ('Denver', 'co', 39.7392, -104.9903),
        ('Colorado Springs', 'co', 38.8339, -104.8214),
        ('Aurora', 'co', 39.7294, -104.8319),
        ('Fort Collins', 'co', 40.5853, -105.0844),
        ('Lakewood', 'co', 39.7047, -105.0814),
        ('Thornton', 'co', 39.8681, -104.9719),
        ('Arvada', 'co', 39.8028, -105.0875),
        ('Westminster', 'co', 39.8367, -105.0372),
        ('Pueblo', 'co', 38.2544, -104.6091),
        ('Centennial', 'co', 39.5807, -104.8760),
        ('Boulder', 'co', 40.0150, -105.2705),
        ('Greeley', 'co', 40.4233, -104.7091),
        ('Longmont', 'co', 40.1672, -105.1019),
        ('Loveland', 'co', 40.3978, -105.0748),
        ('Grand Junction', 'co', 39.0639, -108.5506)
    ],
    'CT': [
        ('Bridgeport', 'ct', 41.1865, -73.1952),
        ('New Haven', 'ct', 41.3083, -72.9279),
        ('Hartford', 'ct', 41.7658, -72.6734),
        ('Stamford', 'ct', 41.0534, -73.5387),
        ('Waterbury', 'ct', 41.5581, -73.0515),
        ('Norwalk', 'ct', 41.1177, -73.4079),
        ('Danbury', 'ct', 41.3948, -73.4540),
        ('New Britain', 'ct', 41.6612, -72.7795),
        ('West Haven', 'ct', 41.2706, -72.9473),
        ('Greenwich', 'ct', 41.0262, -73.6282),
        ('Meriden', 'ct', 41.5387, -72.8070),
        ('Bristol', 'ct', 41.6712, -72.9493),
        ('Milford', 'ct', 41.2229, -73.0565),
        ('Middletown', 'ct', 41.5623, -72.6506),
        ('Norwich', 'ct', 41.5242, -72.0759)
    ],
    'DE': [
        ('Wilmington', 'de', 39.7391, -75.5398),
        ('Dover', 'de', 39.1612, -75.5264),
        ('Newark', 'de', 39.6837, -75.7497),
        ('Middletown', 'de', 39.4496, -75.7163),
        ('Smyrna', 'de', 39.2998, -75.6046),
        ('Milford', 'de', 38.9126, -75.4277),
        ('Seaford', 'de', 38.6412, -75.6110),
        ('Georgetown', 'de', 38.6901, -75.3854),
        ('Elsmere', 'de', 39.7390, -75.5949),
        ('New Castle', 'de', 39.6620, -75.5666),
        ('Laurel', 'de', 38.5565, -75.5716),
        ('Harrington', 'de', 38.9240, -75.5777),
        ('Camden', 'de', 39.1101, -75.5466),
        ('Clayton', 'de', 39.2901, -75.6335),
        ('Millsboro', 'de', 38.5912, -75.2927)
    ],
    'FL': [
        ('Jacksonville', 'fl', 30.3322, -81.6557),
        ('Miami', 'fl', 25.7617, -80.1918),
        ('Tampa', 'fl', 27.9506, -82.4572),
        ('Orlando', 'fl', 28.5383, -81.3792),
        ('St. Petersburg', 'fl', 27.7676, -82.6403),
        ('Hialeah', 'fl', 25.8576, -80.2781),
        ('Tallahassee', 'fl', 30.4518, -84.2807),
        ('Fort Lauderdale', 'fl', 26.1224, -80.1373),
        ('Port St. Lucie', 'fl', 27.2939, -80.3501),
        ('Cape Coral', 'fl', 26.5629, -81.9495),
        ('Hollywood', 'fl', 26.0112, -80.1495),
        ('Gainesville', 'fl', 29.6516, -82.3248),
        ('Miramar', 'fl', 25.9723, -80.2320),
        ('Coral Springs', 'fl', 26.2712, -80.2706),
        ('Pembroke Pines', 'fl', 26.0070, -80.2962)
    ],
    'GA': [
        ('Atlanta', 'ga', 33.7490, -84.3880),
        ('Augusta', 'ga', 33.4734, -82.0105),
        ('Columbus', 'ga', 32.4609, -84.9877),
        ('Savannah', 'ga', 32.0835, -81.0998),
        ('Athens', 'ga', 33.9519, -83.3576),
        ('Sandy Springs', 'ga', 33.9304, -84.3733),
        ('Roswell', 'ga', 34.0232, -84.3616),
        ('Macon', 'ga', 32.8407, -83.6324),
        ('Johns Creek', 'ga', 34.0289, -84.1986),
        ('Albany', 'ga', 31.5804, -84.1557),
        ('Warner Robins', 'ga', 32.6130, -83.6241),
        ('Alpharetta', 'ga', 34.0754, -84.2941),
        ('Marietta', 'ga', 33.9526, -84.5499),
        ('Valdosta', 'ga', 30.8327, -83.2785),
        ('Smyrna', 'ga', 33.8840, -84.5144)
    ],
    'HI': [
        ('Honolulu', 'hi', 21.3099, -157.8581),
        ('East Honolulu', 'hi', 21.2770, -157.7181),
        ('Pearl City', 'hi', 21.3972, -157.9753),
        ('Hilo', 'hi', 19.7297, -155.0900),
        ('Kailua', 'hi', 21.4022, -157.7394),
        ('Waipahu', 'hi', 21.3861, -158.0097),
        ('Kaneohe', 'hi', 21.4181, -157.8025),
        ('Mililani', 'hi', 21.4511, -158.0103),
        ('Kahului', 'hi', 20.8893, -156.4700),
        ('Ewa Beach', 'hi', 21.3156, -158.0072),
        ('Kailua-Kona', 'hi', 19.6400, -155.9969),
        ('Mililani Town', 'hi', 21.4511, -158.0103),
        ('Ewa Gentry', 'hi', 21.3406, -158.0419),
        ('Schofield Barracks', 'hi', 21.4994, -158.0636),
        ('Wahiawa', 'hi', 21.5031, -158.0250)
    ],
    'ID': [
        ('Boise', 'id', 43.6150, -116.2023),
        ('Meridian', 'id', 43.6121, -116.3915),
        ('Nampa', 'id', 43.5407, -116.5635),
        ('Idaho Falls', 'id', 43.4666, -112.0340),
        ('Pocatello', 'id', 42.8713, -112.4455),
        ('Caldwell', 'id', 43.6629, -116.6874),
        ('Coeur d\'Alene', 'id', 47.6777, -116.7804),
        ('Twin Falls', 'id', 42.5630, -114.4609),
        ('Lewiston', 'id', 46.4165, -117.0177),
        ('Post Falls', 'id', 47.7180, -116.9516),
        ('Rexburg', 'id', 43.8261, -111.7897),
        ('Moscow', 'id', 46.7324, -117.0002),
        ('Kuna', 'id', 43.4913, -116.4204),
        ('Ammon', 'id', 43.4855, -111.9463),
        ('Eagle', 'id', 43.6955, -116.3543)
    ],
    'IL': [
        ('Chicago', 'il', 41.8781, -87.6298),
        ('Aurora', 'il', 41.7606, -88.3201),
        ('Joliet', 'il', 41.5251, -88.0817),
        ('Naperville', 'il', 41.7508, -88.1535),
        ('Rockford', 'il', 42.2711, -89.0940),
        ('Elgin', 'il', 42.0354, -88.2826),
        ('Peoria', 'il', 40.6936, -89.5890),
        ('Champaign', 'il', 40.1164, -88.2434),
        ('Waukegan', 'il', 42.3637, -87.8448),
        ('Cicero', 'il', 41.8456, -87.7539),
        ('Bloomington', 'il', 40.4842, -88.9937),
        ('Arlington Heights', 'il', 42.0884, -87.9806),
        ('Evanston', 'il', 42.0451, -87.6877),
        ('Decatur', 'il', 39.8403, -88.9548),
        ('Schaumburg', 'il', 42.0334, -88.0834)
    ],
    'IN': [
        ('Indianapolis', 'in', 39.7684, -86.1581),
        ('Fort Wayne', 'in', 41.0793, -85.1394),
        ('Evansville', 'in', 37.9716, -87.5710),
        ('South Bend', 'in', 41.6764, -86.2520),
        ('Carmel', 'in', 39.9784, -86.1180),
        ('Fishers', 'in', 39.9568, -85.9685),
        ('Bloomington', 'in', 39.1653, -86.5264),
        ('Hammond', 'in', 41.5834, -87.5000),
        ('Gary', 'in', 41.5868, -87.3464),
        ('Muncie', 'in', 40.1934, -85.3863),
        ('Lafayette', 'in', 40.4167, -86.8753),
        ('Terre Haute', 'in', 39.4667, -87.4139),
        ('Kokomo', 'in', 40.4864, -86.1336),
        ('Anderson', 'in', 40.1053, -85.6803),
        ('Noblesville', 'in', 40.0456, -86.0086)
    ],
    'IA': [
        ('Des Moines', 'ia', 41.5868, -93.6250),
        ('Cedar Rapids', 'ia', 41.9778, -91.6656),
        ('Davenport', 'ia', 41.5236, -90.5776),
        ('Sioux City', 'ia', 42.4999, -96.4003),
        ('Iowa City', 'ia', 41.6611, -91.5302),
        ('Waterloo', 'ia', 42.4928, -92.3426),
        ('Council Bluffs', 'ia', 41.2619, -95.8608),
        ('Ames', 'ia', 42.0308, -93.6319),
        ('Dubuque', 'ia', 42.5006, -90.6648),
        ('West Des Moines', 'ia', 41.5772, -93.7114),
        ('Ankeny', 'ia', 41.7297, -93.6058),
        ('Urbandale', 'ia', 41.6266, -93.7121),
        ('Cedar Falls', 'ia', 42.5347, -92.4453),
        ('Marion', 'ia', 42.0345, -91.5985),
        ('Bettendorf', 'ia', 41.5245, -90.5151)
    ],
    'KS': [
        ('Wichita', 'ks', 37.6872, -97.3301),
        ('Overland Park', 'ks', 38.9822, -94.6708),
        ('Kansas City', 'ks', 39.1142, -94.6275),
        ('Topeka', 'ks', 39.0473, -95.6890),
        ('Olathe', 'ks', 38.8814, -94.8191),
        ('Lawrence', 'ks', 38.9717, -95.2353),
        ('Shawnee', 'ks', 39.0228, -94.7202),
        ('Manhattan', 'ks', 39.1836, -96.5717),
        ('Lenexa', 'ks', 38.9536, -94.7336),
        ('Salina', 'ks', 38.8403, -97.6114),
        ('Hutchinson', 'ks', 38.0608, -97.9297),
        ('Leavenworth', 'ks', 39.3111, -94.9225),
        ('Leawood', 'ks', 38.9167, -94.6169),
        ('Dodge City', 'ks', 37.7528, -100.0171),
        ('Garden City', 'ks', 37.9717, -100.8737)
    ],
    'KY': [
        ('Louisville', 'ky', 38.2527, -85.7585),
        ('Lexington', 'ky', 38.0406, -84.5037),
        ('Bowling Green', 'ky', 36.9685, -86.4808),
        ('Owensboro', 'ky', 37.7719, -87.1111),
        ('Covington', 'ky', 39.0837, -84.5086),
        ('Richmond', 'ky', 37.7276, -84.2941),
        ('Georgetown', 'ky', 38.2098, -84.5588),
        ('Florence', 'ky', 38.9989, -84.6266),
        ('Hopkinsville', 'ky', 36.8656, -87.4886),
        ('Nicholasville', 'ky', 37.8806, -84.5730),
        ('Elizabethtown', 'ky', 37.6940, -85.8691),
        ('Henderson', 'ky', 37.8361, -87.5903),
        ('Jeffersontown', 'ky', 38.1942, -85.5644),
        ('Frankfort', 'ky', 38.2009, -84.8733),
        ('Paducah', 'ky', 37.0886, -88.6000)
    ],
    'LA': [
        ('New Orleans', 'la', 29.9511, -90.0715),
        ('Baton Rouge', 'la', 30.4515, -91.1871),
        ('Shreveport', 'la', 32.5252, -93.7502),
        ('Lafayette', 'la', 30.2241, -92.0198),
        ('Lake Charles', 'la', 30.2266, -93.2174),
        ('Kenner', 'la', 29.9941, -90.2417),
        ('Bossier City', 'la', 32.5160, -93.7321),
        ('Monroe', 'la', 32.5093, -92.1193),
        ('Alexandria', 'la', 31.3112, -92.4426),
        ('Houma', 'la', 29.5958, -90.7195),
        ('Marrero', 'la', 29.8999, -90.1023),
        ('New Iberia', 'la', 30.0035, -91.8187),
        ('Laplace', 'la', 30.0669, -90.4809),
        ('Slidell', 'la', 30.2752, -89.7812),
        ('Prairieville', 'la', 30.3027, -90.9718)
    ],
    'ME': [
        ('Portland', 'me', 43.6591, -70.2568),
        ('Lewiston', 'me', 44.1004, -70.2148),
        ('Bangor', 'me', 44.8016, -68.7712),
        ('South Portland', 'me', 43.6414, -70.2409),
        ('Auburn', 'me', 44.0979, -70.2311),
        ('Biddeford', 'me', 43.4926, -70.4533),
        ('Sanford', 'me', 43.4397, -70.7739),
        ('Augusta', 'me', 44.3106, -69.7795),
        ('Westbrook', 'me', 43.6770, -70.3712),
        ('Waterville', 'me', 44.5523, -69.6317),
        ('Presque Isle', 'me', 46.6819, -68.0161),
        ('Saco', 'me', 43.5009, -70.4428),
        ('Caribou', 'me', 46.8611, -68.0142),
        ('Orono', 'me', 44.8834, -68.6717),
        ('Brewer', 'me', 44.7967, -68.7642)
    ],
    'MD': [
        ('Baltimore', 'md', 39.2904, -76.6122),
        ('Frederick', 'md', 39.4143, -77.4105),
        ('Rockville', 'md', 39.0840, -77.1528),
        ('Gaithersburg', 'md', 39.1434, -77.2014),
        ('Bowie', 'md', 39.0068, -76.7791),
        ('Hagerstown', 'md', 39.6418, -77.7200),
        ('Annapolis', 'md', 38.9784, -76.4951),
        ('College Park', 'md', 38.9807, -76.9370),
        ('Salisbury', 'md', 38.3607, -75.5994),
        ('Laurel', 'md', 39.0993, -76.8483),
        ('Greenbelt', 'md', 38.9962, -76.8755),
        ('Cumberland', 'md', 39.6526, -78.7625),
        ('Hyattsville', 'md', 38.9559, -76.9456),
        ('Takoma Park', 'md', 38.9779, -77.0075),
        ('Westminster', 'md', 39.5754, -76.9958)
    ],
    'MA': [
        ('Boston', 'ma', 42.3601, -71.0589),
        ('Worcester', 'ma', 42.2626, -71.8023),
        ('Springfield', 'ma', 42.1015, -72.5898),
        ('Cambridge', 'ma', 42.3736, -71.1097),
        ('Lowell', 'ma', 42.6334, -71.3162),
        ('Brockton', 'ma', 42.0834, -71.0184),
        ('New Bedford', 'ma', 41.6362, -70.9342),
        ('Quincy', 'ma', 42.2529, -71.0023),
        ('Lynn', 'ma', 42.4668, -70.9495),
        ('Fall River', 'ma', 41.7015, -71.1550),
        ('Newton', 'ma', 42.3370, -71.2092),
        ('Lawrence', 'ma', 42.7070, -71.1631),
        ('Somerville', 'ma', 42.3876, -71.0995),
        ('Framingham', 'ma', 42.2793, -71.4162),
        ('Haverhill', 'ma', 42.7762, -71.0773)
    ],
    'MI': [
        ('Detroit', 'mi', 42.3314, -83.0458),
        ('Grand Rapids', 'mi', 42.9634, -85.6681),
        ('Warren', 'mi', 42.5145, -83.0146),
        ('Sterling Heights', 'mi', 42.5803, -83.0302),
        ('Ann Arbor', 'mi', 42.2808, -83.7430),
        ('Lansing', 'mi', 42.3314, -84.5467),
        ('Flint', 'mi', 43.0125, -83.6875),
        ('Dearborn', 'mi', 42.3223, -83.1763),
        ('Livonia', 'mi', 42.3684, -83.3527),
        ('Troy', 'mi', 42.6064, -83.1498),
        ('Farmington Hills', 'mi', 42.4989, -83.3677),
        ('Kalamazoo', 'mi', 42.2917, -85.5872),
        ('Southfield', 'mi', 42.4734, -83.2219),
        ('Rochester Hills', 'mi', 42.6583, -83.1499),
        ('Taylor', 'mi', 42.2407, -83.2696)
    ],
    'MN': [
        ('Minneapolis', 'mn', 44.9778, -93.2650),
        ('Saint Paul', 'mn', 44.9537, -93.0900),
        ('Rochester', 'mn', 44.0121, -92.4802),
        ('Duluth', 'mn', 46.7867, -92.1005),
        ('Bloomington', 'mn', 44.8408, -93.2982),
        ('Brooklyn Park', 'mn', 45.0941, -93.3563),
        ('Plymouth', 'mn', 45.0105, -93.4555),
        ('Saint Cloud', 'mn', 45.5579, -94.1632),
        ('Eagan', 'mn', 44.8041, -93.1668),
        ('Burnsville', 'mn', 44.7678, -93.2777),
        ('Eden Prairie', 'mn', 44.8547, -93.4708),
        ('Coon Rapids', 'mn', 45.1200, -93.3030),
        ('Maple Grove', 'mn', 45.0725, -93.4557),
        ('Minnetonka', 'mn', 44.9211, -93.4687),
        ('Blaine', 'mn', 45.1607, -93.2349)
    ],
    'MS': [
        ('Jackson', 'ms', 32.2988, -90.1848),
        ('Gulfport', 'ms', 30.3674, -89.0928),
        ('Southaven', 'ms', 34.9890, -90.0126),
        ('Hattiesburg', 'ms', 31.3071, -89.2903),
        ('Biloxi', 'ms', 30.3960, -88.8853),
        ('Meridian', 'ms', 32.3643, -88.7034),
        ('Tupelo', 'ms', 34.2576, -88.7034),
        ('Greenville', 'ms', 33.4151, -91.0618),
        ('Olive Branch', 'ms', 34.9617, -89.8598),
        ('Horn Lake', 'ms', 34.9551, -90.0368),
        ('Clinton', 'ms', 32.3412, -90.3218),
        ('Madison', 'ms', 32.4618, -90.1151),
        ('Pearl', 'ms', 32.2746, -90.1364),
        ('Ridgeland', 'ms', 32.4279, -90.1364),
        ('Starkville', 'ms', 33.4504, -88.8184)
    ],
    'MO': [
        ('Kansas City', 'mo', 39.0997, -94.5786),
        ('Saint Louis', 'mo', 38.6270, -90.1994),
        ('Springfield', 'mo', 37.2089, -93.2923),
        ('Columbia', 'mo', 38.9517, -92.3341),
        ('Independence', 'mo', 39.0911, -94.4155),
        ('Lee\'s Summit', 'mo', 38.9109, -94.3822),
        ('O\'Fallon', 'mo', 38.8106, -90.6999),
        ('Saint Joseph', 'mo', 39.7391, -94.8469),
        ('Saint Charles', 'mo', 38.7881, -90.4974),
        ('Saint Peters', 'mo', 38.7873, -90.6298),
        ('Blue Springs', 'mo', 39.0169, -94.2816),
        ('Florissant', 'mo', 38.7892, -90.3223),
        ('Joplin', 'mo', 37.0842, -94.5133),
        ('Chesterfield', 'mo', 38.6631, -90.5770),
        ('Jefferson City', 'mo', 38.5767, -92.1735)
    ],
    'MT': [
        ('Billings', 'mt', 45.7833, -108.5007),
        ('Missoula', 'mt', 46.8721, -113.9940),
        ('Great Falls', 'mt', 47.4941, -111.2833),
        ('Bozeman', 'mt', 45.6770, -111.0429),
        ('Butte', 'mt', 46.0038, -112.5348),
        ('Helena', 'mt', 46.5958, -112.0362),
        ('Kalispell', 'mt', 48.1958, -114.3137),
        ('Havre', 'mt', 48.5500, -109.6841),
        ('Anaconda', 'mt', 46.1284, -112.9420),
        ('Miles City', 'mt', 46.4083, -105.8406),
        ('Belgrade', 'mt', 45.7766, -111.177),
        ('Lewistown', 'mt', 47.0624, -109.4285),
        ('Livingston', 'mt', 45.6627, -110.5610),
        ('Laurel', 'mt', 45.6694, -108.7712),
        ('Whitefish', 'mt', 48.4108, -114.3375)
    ],
    'NE': [
        ('Omaha', 'ne', 41.2565, -95.9345),
        ('Lincoln', 'ne', 40.8136, -96.7026),
        ('Bellevue', 'ne', 41.1370, -95.9145),
        ('Grand Island', 'ne', 40.9264, -98.3420),
        ('Kearney', 'ne', 40.6993, -99.0817),
        ('Fremont', 'ne', 41.4333, -96.4981),
        ('Hastings', 'ne', 40.5861, -98.3887),
        ('North Platte', 'ne', 41.1239, -100.7654),
        ('Norfolk', 'ne', 42.0281, -97.4170),
        ('Columbus', 'ne', 41.4300, -97.3683),
        ('Papillion', 'ne', 41.1544, -96.0442),
        ('La Vista', 'ne', 41.1833, -96.0336),
        ('Beatrice', 'ne', 40.2681, -96.7470),
        ('South Sioux City', 'ne', 42.4541, -96.4128),
        ('Scottsbluff', 'ne', 41.8661, -103.6672)
    ],
    'NV': [
        ('Las Vegas', 'nv', 36.1699, -115.1398),
        ('Henderson', 'nv', 36.0397, -114.9817),
        ('Reno', 'nv', 39.5296, -119.8138),
        ('North Las Vegas', 'nv', 36.1989, -115.1175),
        ('Sparks', 'nv', 39.5349, -119.7527),
        ('Carson City', 'nv', 39.1638, -119.7674),
        ('Fernley', 'nv', 39.6080, -119.2519),
        ('Elko', 'nv', 40.8324, -115.7631),
        ('Mesquite', 'nv', 36.8055, -114.0672),
        ('Boulder City', 'nv', 35.9786, -114.832),
        ('Fallon', 'nv', 39.4735, -118.7774),
        ('Winnemucca', 'nv', 40.9730, -117.7357),
        ('West Wendover', 'nv', 40.7391, -114.0733),
        ('Ely', 'nv', 39.2472, -114.8886),
        ('Yerington', 'nv', 38.9875, -119.1638)
    ],
    'NH': [
        ('Manchester', 'nh', 42.9956, -71.4548),
        ('Nashua', 'nh', 42.7654, -71.4676),
        ('Concord', 'nh', 43.2081, -71.5376),
        ('Derry', 'nh', 42.8801, -71.3273),
        ('Rochester', 'nh', 43.3042, -70.9756),
        ('Dover', 'nh', 43.1979, -70.8737),
        ('Keene', 'nh', 42.9342, -72.2781),
        ('Portsmouth', 'nh', 43.0718, -70.7626),
        ('Laconia', 'nh', 43.5278, -71.4703),
        ('Lebanon', 'nh', 43.6422, -72.2517),
        ('Claremont', 'nh', 43.3767, -72.3317),
        ('Berlin', 'nh', 44.4689, -71.1850),
        ('Hudson', 'nh', 42.7654, -71.4342),
        ('Merrimack', 'nh', 42.8653, -71.4912),
        ('Salem', 'nh', 42.7881, -71.2009)
    ],
    'NJ': [
        ('Newark', 'nj', 40.7357, -74.1724),
        ('Jersey City', 'nj', 40.7178, -74.0431),
        ('Paterson', 'nj', 40.9168, -74.1718),
        ('Elizabeth', 'nj', 40.6640, -74.2107),
        ('Edison', 'nj', 40.5187, -74.4121),
        ('Woodbridge', 'nj', 40.5576, -74.2846),
        ('Lakewood', 'nj', 40.0979, -74.2179),
        ('Toms River', 'nj', 39.9537, -74.1979),
        ('Hamilton', 'nj', 40.2298, -74.7429),
        ('Trenton', 'nj', 40.2206, -74.7565),
        ('Clifton', 'nj', 40.8584, -74.1638),
        ('Camden', 'nj', 39.9259, -75.1196),
        ('Brick', 'nj', 40.0434, -74.1015),
        ('Cherry Hill', 'nj', 39.9348, -75.0307),
        ('Passaic', 'nj', 40.8568, -74.1285)
    ],
    'NM': [
        ('Albuquerque', 'nm', 35.0844, -106.6504),
        ('Las Cruces', 'nm', 32.3199, -106.7637),
        ('Rio Rancho', 'nm', 35.2328, -106.6630),
        ('Santa Fe', 'nm', 35.6870, -105.9378),
        ('Roswell', 'nm', 33.3943, -104.5230),
        ('Farmington', 'nm', 36.7281, -108.2187),
        ('Clovis', 'nm', 34.4048, -103.2052),
        ('Hobbs', 'nm', 32.7026, -103.1360),
        ('Alamogordo', 'nm', 32.8995, -105.9603),
        ('Carlsbad', 'nm', 32.4207, -104.2288),
        ('Gallup', 'nm', 35.5281, -108.7426),
        ('Deming', 'nm', 32.2687, -107.7586),
        ('Los Alamos', 'nm', 35.8869, -106.3056),
        ('Chaparral', 'nm', 32.0229, -106.3844),
        ('Sunland Park', 'nm', 31.7948, -106.5811)
    ],
    'NY': [
        ('New York', 'ny', 40.7128, -74.0060),
        ('Buffalo', 'ny', 42.8864, -78.8784),
        ('Rochester', 'ny', 43.1566, -77.6088),
        ('Yonkers', 'ny', 40.9312, -73.8988),
        ('Syracuse', 'ny', 43.0481, -76.1474),
        ('Albany', 'ny', 42.6526, -73.7562),
        ('New Rochelle', 'ny', 40.9115, -73.7824),
        ('Mount Vernon', 'ny', 40.9126, -73.8370),
        ('Schenectady', 'ny', 42.8142, -73.9396),
        ('Utica', 'ny', 43.1009, -75.2327),
        ('White Plains', 'ny', 41.0340, -73.7629),
        ('Hempstead', 'ny', 40.7062, -73.6187),
        ('Troy', 'ny', 42.7284, -73.6918),
        ('Niagara Falls', 'ny', 43.0942, -79.0567),
        ('Binghamton', 'ny', 42.0987, -75.9180)
    ],
    'NC': [
        ('Charlotte', 'nc', 35.2271, -80.8431),
        ('Raleigh', 'nc', 35.7796, -78.6382),
        ('Greensboro', 'nc', 36.0726, -79.7920),
        ('Durham', 'nc', 35.9940, -78.8986),
        ('Winston-Salem', 'nc', 36.0999, -80.2442),
        ('Fayetteville', 'nc', 35.0527, -78.8784),
        ('Cary', 'nc', 35.7915, -78.7811),
        ('Wilmington', 'nc', 34.2257, -77.9447),
        ('High Point', 'nc', 35.9557, -80.0053),
        ('Concord', 'nc', 35.4087, -80.5792),
        ('Asheville', 'nc', 35.5951, -82.5515),
        ('Gastonia', 'nc', 35.2620, -81.1873),
        ('Jacksonville', 'nc', 34.7540, -77.4302),
        ('Chapel Hill', 'nc', 35.9132, -79.0558),
        ('Rocky Mount', 'nc', 35.9382, -77.7905)
    ],
    'ND': [
        ('Fargo', 'nd', 46.8772, -96.7898),
        ('Bismarck', 'nd', 46.8083, -100.7837),
        ('Grand Forks', 'nd', 47.9253, -97.0329),
        ('Minot', 'nd', 48.2330, -101.2957),
        ('West Fargo', 'nd', 46.8747, -96.9003),
        ('Williston', 'nd', 48.1470, -103.6179),
        ('Dickinson', 'nd', 46.8789, -102.7890),
        ('Mandan', 'nd', 46.8266, -100.8896),
        ('Jamestown', 'nd', 46.9108, -98.7084),
        ('Wahpeton', 'nd', 46.2652, -96.6059),
        ('Devils Lake', 'nd', 48.1128, -98.8648),
        ('Grafton', 'nd', 48.4097, -97.4131),
        ('Valley City', 'nd', 46.9233, -98.0031),
        ('Beulah', 'nd', 47.2642, -101.7782),
        ('Watford City', 'nd', 47.8014, -103.2840)
    ],
    'OH': [
        ('Columbus', 'oh', 39.9612, -82.9988),
        ('Cleveland', 'oh', 41.4993, -81.6944),
        ('Cincinnati', 'oh', 39.1031, -84.5120),
        ('Toledo', 'oh', 41.6528, -83.5379),
        ('Akron', 'oh', 41.0814, -81.5190),
        ('Dayton', 'oh', 39.7589, -84.1916),
        ('Parma', 'oh', 41.4047, -81.7229),
        ('Canton', 'oh', 40.7989, -81.3785),
        ('Lorain', 'oh', 41.4528, -82.1821),
        ('Hamilton', 'oh', 39.3995, -84.5613),
        ('Youngstown', 'oh', 41.0998, -80.6495),
        ('Springfield', 'oh', 39.9242, -83.8088),
        ('Kettering', 'oh', 39.6895, -84.1686),
        ('Elyria', 'oh', 41.3683, -82.1077),
        ('Lakewood', 'oh', 41.4820, -81.7982)
    ],
    'OK': [
        ('Oklahoma City', 'ok', 35.4676, -97.5164),
        ('Tulsa', 'ok', 36.1540, -95.9928),
        ('Norman', 'ok', 35.2226, -97.4395),
        ('Broken Arrow', 'ok', 36.0526, -95.7969),
        ('Lawton', 'ok', 34.6087, -98.3959),
        ('Edmond', 'ok', 35.6528, -97.4781),
        ('Moore', 'ok', 35.3396, -97.4867),
        ('Midwest City', 'ok', 35.4495, -97.3967),
        ('Enid', 'ok', 36.3956, -97.8784),
        ('Stillwater', 'ok', 36.1156, -97.0583),
        ('Muskogee', 'ok', 35.7479, -95.3697),
        ('Bartlesville', 'ok', 36.7473, -95.9808),
        ('Owasso', 'ok', 36.2695, -95.8547),
        ('Shawnee', 'ok', 35.3273, -96.9253),
        ('Ponca City', 'ok', 36.7063, -97.0858)
    ],
    'OR': [
        ('Portland', 'or', 45.5152, -122.6784),
        ('Eugene', 'or', 44.0521, -123.0868),
        ('Salem', 'or', 44.9429, -123.0351),
        ('Gresham', 'or', 45.4988, -122.4315),
        ('Hillsboro', 'or', 45.5228, -122.9897),
        ('Bend', 'or', 44.0582, -121.3153),
        ('Beaverton', 'or', 45.4871, -122.8037),
        ('Medford', 'or', 42.3265, -122.8756),
        ('Springfield', 'or', 44.0462, -123.0220),
        ('Corvallis', 'or', 44.5646, -123.2620),
        ('Albany', 'or', 44.6365, -123.1059),
        ('Tigard', 'or', 45.4312, -122.7715),
        ('Lake Oswego', 'or', 45.4207, -122.6707),
        ('Keizer', 'or', 44.9901, -123.0262),
        ('Grants Pass', 'or', 42.4390, -123.3284)
    ],
    'PA': [
        ('Philadelphia', 'pa', 39.9526, -75.1652),
        ('Pittsburgh', 'pa', 40.4406, -79.9959),
        ('Allentown', 'pa', 40.6084, -75.4902),
        ('Erie', 'pa', 42.1292, -80.0851),
        ('Reading', 'pa', 40.3356, -75.9269),
        ('Scranton', 'pa', 41.4090, -75.6624),
        ('Bethlehem', 'pa', 40.6259, -75.3705),
        ('Lancaster', 'pa', 40.0379, -76.3055),
        ('Harrisburg', 'pa', 40.2732, -76.8839),
        ('Altoona', 'pa', 40.5187, -78.3947),
        ('York', 'pa', 39.9626, -76.7277),
        ('State College', 'pa', 40.7934, -77.8600),
        ('Wilkes-Barre', 'pa', 41.2459, -75.8813),
        ('Chester', 'pa', 39.8498, -75.3557),
        ('Easton', 'pa', 40.6884, -75.2077)
    ],
    'RI': [
        ('Providence', 'ri', 41.8240, -71.4128),
        ('Warwick', 'ri', 41.7001, -71.4162),
        ('Cranston', 'ri', 41.7798, -71.4371),
        ('Pawtucket', 'ri', 41.8787, -71.3826),
        ('East Providence', 'ri', 41.8137, -71.3701),
        ('Woonsocket', 'ri', 42.0029, -71.5147),
        ('Newport', 'ri', 41.4901, -71.3128),
        ('Central Falls', 'ri', 41.8904, -71.3925),
        ('Westerly', 'ri', 41.3776, -71.8273),
        ('North Providence', 'ri', 41.8518, -71.4662),
        ('Bristol', 'ri', 41.6771, -71.2662),
        ('Coventry', 'ri', 41.7001, -71.6828),
        ('Cumberland', 'ri', 41.9668, -71.4162),
        ('Johnston', 'ri', 41.8296, -71.5162),
        ('North Kingstown', 'ri', 41.5501, -71.4662)
    ],
    'SC': [
        ('Charleston', 'sc', 32.7765, -79.9311),
        ('Columbia', 'sc', 34.0007, -81.0348),
        ('North Charleston', 'sc', 32.8546, -79.9748),
        ('Mount Pleasant', 'sc', 32.8323, -79.8284),
        ('Rock Hill', 'sc', 34.9249, -81.0251),
        ('Greenville', 'sc', 34.8526, -82.3940),
        ('Summerville', 'sc', 33.0185, -80.1756),
        ('Sumter', 'sc', 33.9204, -80.3414),
        ('Goose Creek', 'sc', 32.9810, -80.0326),
        ('Hilton Head Island', 'sc', 32.2163, -80.7526),
        ('Florence', 'sc', 34.1954, -79.7626),
        ('Spartanburg', 'sc', 34.9496, -81.9320),
        ('Anderson', 'sc', 34.5034, -82.6501),
        ('Aiken', 'sc', 33.5557, -81.7290),
        ('Myrtle Beach', 'sc', 33.6891, -78.8867)
    ],
    'SD': [
        ('Sioux Falls', 'sd', 43.5446, -96.7311),
        ('Rapid City', 'sd', 44.0805, -103.2310),
        ('Aberdeen', 'sd', 45.4647, -98.4865),
        ('Brookings', 'sd', 44.3114, -96.7984),
        ('Watertown', 'sd', 44.8997, -97.1142),
        ('Mitchell', 'sd', 43.7094, -98.0298),
        ('Pierre', 'sd', 44.3683, -100.3510),
        ('Yankton', 'sd', 42.8711, -97.3973),
        ('Huron', 'sd', 44.3635, -98.2142),
        ('Vermillion', 'sd', 42.7794, -96.9295),
        ('Madison', 'sd', 44.0061, -97.1142),
        ('Spearfish', 'sd', 44.4906, -103.8590),
        ('Brandon', 'sd', 43.5947, -96.5811),
        ('Box Elder', 'sd', 44.1147, -103.0771),
        ('Sturgis', 'sd', 44.4097, -103.5093)
    ],
    'TN': [
        ('Nashville', 'tn', 36.1627, -86.7816),
        ('Memphis', 'tn', 35.1495, -90.0490),
        ('Knoxville', 'tn', 35.9606, -83.9207),
        ('Chattanooga', 'tn', 35.0456, -85.3097),
        ('Clarksville', 'tn', 36.5298, -87.3595),
        ('Murfreesboro', 'tn', 35.8456, -86.3903),
        ('Franklin', 'tn', 35.9251, -86.8689),
        ('Johnson City', 'tn', 36.3134, -82.3535),
        ('Bartlett', 'tn', 35.2045, -89.8739),
        ('Hendersonville', 'tn', 36.3047, -86.6200),
        ('Kingsport', 'tn', 36.5484, -82.5618),
        ('Collierville', 'tn', 35.0420, -89.6645),
        ('Cleveland', 'tn', 35.1595, -84.8766),
        ('Smyrna', 'tn', 35.9829, -86.5186),
        ('Brentwood', 'tn', 36.0331, -86.7828)
    ],
    'TX': [
        ('Houston', 'tx', 29.7604, -95.3698),
        ('San Antonio', 'tx', 29.4241, -98.4936),
        ('Dallas', 'tx', 32.7767, -96.7970),
        ('Austin', 'tx', 30.2672, -97.7431),
        ('Fort Worth', 'tx', 32.7555, -97.3308),
        ('El Paso', 'tx', 31.7619, -106.4850),
        ('Arlington', 'tx', 32.7357, -97.1081),
        ('Corpus Christi', 'tx', 27.8006, -97.3964),
        ('Plano', 'tx', 33.0198, -96.6989),
        ('Lubbock', 'tx', 33.5779, -101.8552),
        ('Laredo', 'tx', 27.5306, -99.4803),
        ('Garland', 'tx', 32.9126, -96.6389),
        ('Irving', 'tx', 32.8140, -96.9489),
        ('Amarillo', 'tx', 35.2220, -101.8313),
        ('Grand Prairie', 'tx', 32.7460, -96.9978)
    ],
    'UT': [
        ('Salt Lake City', 'ut', 40.7608, -111.8910),
        ('West Valley City', 'ut', 40.6916, -112.0011),
        ('Provo', 'ut', 40.2338, -111.6585),
        ('West Jordan', 'ut', 40.6097, -111.9391),
        ('Orem', 'ut', 40.2969, -111.6946),
        ('Sandy', 'ut', 40.5649, -111.8389),
        ('Ogden', 'ut', 41.2230, -111.9738),
        ('St. George', 'ut', 37.0965, -113.5684),
        ('Layton', 'ut', 41.0602, -111.9711),
        ('Taylorsville', 'ut', 40.6677, -111.9391),
        ('South Jordan', 'ut', 40.5621, -111.9296),
        ('Lehi', 'ut', 40.3916, -111.8507),
        ('Logan', 'ut', 41.7370, -111.8338),
        ('Murray', 'ut', 40.6669, -111.8879),
        ('Draper', 'ut', 40.5246, -111.8638)
    ],
    'VT': [
        ('Burlington', 'vt', 44.4759, -73.2121),
        ('Essex', 'vt', 44.4906, -73.1129),
        ('South Burlington', 'vt', 44.4669, -73.1709),
        ('Colchester', 'vt', 44.5431, -73.1304),
        ('Rutland', 'vt', 43.6106, -72.9726),
        ('Bennington', 'vt', 42.8781, -73.1967),
        ('Brattleboro', 'vt', 42.8509, -72.5579),
        ('Milton', 'vt', 44.6364, -73.1173),
        ('Hartford', 'vt', 43.6481, -72.3317),
        ('Williston', 'vt', 44.4428, -73.0937),
        ('Middlebury', 'vt', 44.0167, -73.1673),
        ('Barre', 'vt', 44.1970, -72.5020),
        ('Montpelier', 'vt', 44.2601, -72.5806),
        ('Winooski', 'vt', 44.4906, -73.1870),
        ('St. Albans', 'vt', 44.8106, -73.0837)
    ],
    'VA': [
        ('Virginia Beach', 'va', 36.8529, -75.9780),
        ('Norfolk', 'va', 36.8468, -76.2852),
        ('Chesapeake', 'va', 36.7682, -76.2875),
        ('Richmond', 'va', 37.5407, -77.4360),
        ('Newport News', 'va', 37.0871, -76.4730),
        ('Alexandria', 'va', 38.8048, -77.0469),
        ('Hampton', 'va', 37.0299, -76.3452),
        ('Portsmouth', 'va', 36.8354, -76.2983),
        ('Suffolk', 'va', 36.7282, -76.5836),
        ('Lynchburg', 'va', 37.4138, -79.1422),
        ('Roanoke', 'va', 37.2710, -79.9414),
        ('Danville', 'va', 36.5860, -79.3956),
        ('Leesburg', 'va', 39.1157, -77.5636),
        ('Harrisonburg', 'va', 38.4496, -78.8689),
        ('Charlottesville', 'va', 38.0293, -78.4767)
    ],
    'WA': [
        ('Seattle', 'wa', 47.6062, -122.3321),
        ('Spokane', 'wa', 47.6587, -117.4260),
        ('Tacoma', 'wa', 47.2529, -122.4443),
        ('Vancouver', 'wa', 45.6387, -122.6615),
        ('Bellevue', 'wa', 47.6101, -122.2015),
        ('Kent', 'wa', 47.3809, -122.2348),
        ('Everett', 'wa', 47.9790, -122.2021),
        ('Renton', 'wa', 47.4829, -122.2171),
        ('Spokane Valley', 'wa', 47.6732, -117.2394),
        ('Federal Way', 'wa', 47.3223, -122.3126),
        ('Bellingham', 'wa', 48.7519, -122.4787),
        ('Kennewick', 'wa', 46.2112, -119.1372),
        ('Auburn', 'wa', 47.3073, -122.2284),
        ('Pasco', 'wa', 46.2396, -119.1006),
        ('Marysville', 'wa', 48.0518, -122.1771)
    ],
    'WV': [
        ('Charleston', 'wv', 38.3498, -81.6326),
        ('Huntington', 'wv', 38.4192, -82.4452),
        ('Morgantown', 'wv', 39.6295, -79.9553),
        ('Parkersburg', 'wv', 39.2667, -81.5615),
        ('Wheeling', 'wv', 40.0640, -80.7209),
        ('Martinsburg', 'wv', 39.4565, -77.9636),
        ('Fairmont', 'wv', 39.4851, -80.1426),
        ('Beckley', 'wv', 37.7782, -81.1887),
        ('Clarksburg', 'wv', 39.2806, -80.3445),
        ('South Charleston', 'wv', 38.3581, -81.7007),
        ('St. Albans', 'wv', 38.3731, -81.8165),
        ('Hurricane', 'wv', 38.4320, -82.0190),
        ('Lewisburg', 'wv', 37.8018, -80.4459),
        ('Charles Town', 'wv', 39.2893, -77.8597),
        ('Buckhannon', 'wv', 38.9931, -80.2312)
    ],
    'WI': [
        ('Milwaukee', 'wi', 43.0389, -87.9065),
        ('Madison', 'wi', 43.0731, -89.4012),
        ('Green Bay', 'wi', 44.5133, -88.0133),
        ('Kenosha', 'wi', 42.5847, -87.8212),
        ('Racine', 'wi', 42.7261, -87.7829),
        ('Appleton', 'wi', 44.2619, -88.4154),
        ('Waukesha', 'wi', 43.0117, -88.2315),
        ('Eau Claire', 'wi', 44.8113, -91.4985),
        ('Oshkosh', 'wi', 44.0247, -88.5426),
        ('Janesville', 'wi', 42.6828, -89.0187),
        ('West Allis', 'wi', 43.0167, -88.0070),
        ('La Crosse', 'wi', 43.8014, -91.2396),
        ('Sheboygan', 'wi', 43.7508, -87.7145),
        ('Wauwatosa', 'wi', 43.0494, -88.0077),
        ('Fond du Lac', 'wi', 43.7730, -88.4470)
    ],
    'WY': [
        ('Cheyenne', 'wy', 41.1400, -104.8197),
        ('Casper', 'wy', 42.8666, -106.3131),
        ('Laramie', 'wy', 41.3114, -105.5911),
        ('Gillette', 'wy', 44.2911, -105.502),
        ('Rock Springs', 'wy', 41.5875, -109.2029),
        ('Sheridan', 'wy', 44.7970, -106.9561),
        ('Green River', 'wy', 41.5253, -109.4662),
        ('Evanston', 'wy', 41.2683, -111.0329),
        ('Riverton', 'wy', 42.9761, -108.3843),
        ('Jackson', 'wy', 43.4799, -110.7624),
        ('Cody', 'wy', 44.5263, -109.0565),
        ('Rawlins', 'wy', 41.7911, -107.2387),
        ('Lander', 'wy', 42.8330, -108.7307),
        ('Torrington', 'wy', 42.0661, -104.1841),
        ('Powell', 'wy', 44.7541, -108.7565)
    ]
}

def create_city_slug(city_name, state):
    """Create URL-friendly slug from city name and state"""
    # Handle special characters and spaces
    slug = city_name.lower()
    slug = slug.replace("'", "")
    slug = slug.replace(".", "")
    slug = slug.replace(" ", "-")
    slug = slug.replace("st-", "st-")  # Keep St. as st-
    return f"{slug}-{state}-business-valuation-analyst"

def generate_page_content(city_name, state, lat, lng):
    """Generate HTML content for business valuation analyst page"""
    state_full_names = {
        'al': 'Alabama', 'ak': 'Alaska', 'az': 'Arizona', 'ar': 'Arkansas', 'ca': 'California',
        'co': 'Colorado', 'ct': 'Connecticut', 'de': 'Delaware', 'fl': 'Florida', 'ga': 'Georgia',
        'hi': 'Hawaii', 'id': 'Idaho', 'il': 'Illinois', 'in': 'Indiana', 'ia': 'Iowa',
        'ks': 'Kansas', 'ky': 'Kentucky', 'la': 'Louisiana', 'me': 'Maine', 'md': 'Maryland',
        'ma': 'Massachusetts', 'mi': 'Michigan', 'mn': 'Minnesota', 'ms': 'Mississippi', 'mo': 'Missouri',
        'mt': 'Montana', 'ne': 'Nebraska', 'nv': 'Nevada', 'nh': 'New Hampshire', 'nj': 'New Jersey',
        'nm': 'New Mexico', 'ny': 'New York', 'nc': 'North Carolina', 'nd': 'North Dakota', 'oh': 'Ohio',
        'ok': 'Oklahoma', 'or': 'Oregon', 'pa': 'Pennsylvania', 'ri': 'Rhode Island', 'sc': 'South Carolina',
        'sd': 'South Dakota', 'tn': 'Tennessee', 'tx': 'Texas', 'ut': 'Utah', 'vt': 'Vermont',
        'va': 'Virginia', 'wa': 'Washington', 'wv': 'West Virginia', 'wi': 'Wisconsin', 'wy': 'Wyoming'
    }
    
    state_name = state_full_names.get(state, state.upper())
    page_slug = create_city_slug(city_name, state)
    
    # Industries to focus on for business valuation
    major_industries = {
        'ca': ['technology', 'entertainment', 'agriculture', 'aerospace', 'biotechnology'],
        'tx': ['energy', 'technology', 'aerospace', 'agriculture', 'manufacturing'],
        'ny': ['finance', 'real estate', 'media', 'technology', 'healthcare'],
        'fl': ['tourism', 'agriculture', 'aerospace', 'international trade', 'real estate'],
        'il': ['manufacturing', 'agriculture', 'technology', 'transportation', 'finance'],
        'pa': ['manufacturing', 'agriculture', 'energy', 'healthcare', 'finance'],
        'oh': ['manufacturing', 'agriculture', 'aerospace', 'automotive', 'healthcare'],
        'ga': ['agriculture', 'aerospace', 'automotive', 'logistics', 'technology'],
        'nc': ['agriculture', 'textiles', 'technology', 'aerospace', 'biotechnology'],
        'mi': ['automotive', 'manufacturing', 'agriculture', 'technology', 'healthcare'],
        'nj': ['pharmaceuticals', 'finance', 'telecommunications', 'agriculture', 'manufacturing'],
        'va': ['technology', 'agriculture', 'defense', 'tourism', 'shipbuilding'],
        'wa': ['technology', 'aerospace', 'agriculture', 'maritime', 'biotechnology'],
        'az': ['technology', 'aerospace', 'mining', 'tourism', 'agriculture'],
        'ma': ['technology', 'biotechnology', 'finance', 'education', 'healthcare'],
        'tn': ['automotive', 'music', 'agriculture', 'logistics', 'healthcare'],
        'in': ['manufacturing', 'agriculture', 'pharmaceutical', 'automotive', 'steel'],
        'mo': ['agriculture', 'aerospace', 'transportation', 'biotechnology', 'financial services'],
        'md': ['biotechnology', 'federal contracting', 'cybersecurity', 'maritime', 'agriculture'],
        'wi': ['agriculture', 'manufacturing', 'technology', 'paper products', 'tourism'],
        'mn': ['agriculture', 'mining', 'manufacturing', 'technology', 'healthcare'],
        'co': ['aerospace', 'technology', 'energy', 'agriculture', 'tourism'],
        'al': ['aerospace', 'automotive', 'steel', 'agriculture', 'technology'],
        'sc': ['automotive', 'aerospace', 'textiles', 'agriculture', 'tourism'],
        'la': ['energy', 'petrochemicals', 'agriculture', 'maritime', 'tourism'],
        'ky': ['automotive', 'agriculture', 'aerospace', 'bourbon', 'healthcare'],
        'or': ['technology', 'agriculture', 'forestry', 'renewable energy', 'manufacturing'],
        'ok': ['energy', 'agriculture', 'aerospace', 'biotechnology', 'telecommunications'],
        'ct': ['insurance', 'aerospace', 'finance', 'pharmaceuticals', 'manufacturing'],
        'ut': ['technology', 'mining', 'agriculture', 'aerospace', 'financial services'],
        'nv': ['tourism', 'mining', 'agriculture', 'logistics', 'renewable energy'],
        'ar': ['agriculture', 'manufacturing', 'transportation', 'energy', 'aerospace'],
        'ms': ['agriculture', 'manufacturing', 'aerospace', 'energy', 'shipbuilding'],
        'ks': ['agriculture', 'aerospace', 'manufacturing', 'energy', 'technology'],
        'ne': ['agriculture', 'transportation', 'manufacturing', 'telecommunications', 'insurance'],
        'wv': ['energy', 'chemicals', 'aerospace', 'agriculture', 'tourism'],
        'id': ['agriculture', 'technology', 'manufacturing', 'mining', 'forestry'],
        'nh': ['technology', 'manufacturing', 'tourism', 'agriculture', 'aerospace'],
        'me': ['agriculture', 'forestry', 'fishing', 'tourism', 'technology'],
        'hi': ['tourism', 'agriculture', 'military', 'renewable energy', 'technology'],
        'ri': ['manufacturing', 'technology', 'tourism', 'maritime', 'healthcare'],
        'mt': ['agriculture', 'mining', 'energy', 'tourism', 'technology'],
        'de': ['finance', 'chemicals', 'agriculture', 'pharmaceuticals', 'technology'],
        'sd': ['agriculture', 'tourism', 'manufacturing', 'financial services', 'healthcare'],
        'nd': ['energy', 'agriculture', 'manufacturing', 'technology', 'aerospace'],
        'ak': ['energy', 'fishing', 'tourism', 'mining', 'military'],
        'vt': ['agriculture', 'tourism', 'manufacturing', 'technology', 'renewable energy'],
        'wy': ['energy', 'mining', 'agriculture', 'tourism', 'manufacturing']
    }
    
    industries = major_industries.get(state, ['manufacturing', 'agriculture', 'technology', 'healthcare', 'services'])
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{city_name} Business Valuation Analyst | {state_name} Business Valuation Expert | Skerritt Economics</title>
    <meta name="description" content="Expert business valuation analyst in {city_name}. Certified valuation expert providing comprehensive valuations, financial analysis, and litigation support for {state_name} attorneys and businesses.">
    <meta name="keywords" content="business valuation analyst {city_name}, business valuation expert {state_name}, business valuation {city_name}, certified valuation analyst, company valuation, asset valuation, business worth, business evaluation {state}">
    <link rel="canonical" href="https://skerritteconomics.com/locations/cities/{page_slug}.html">
    <meta property="og:title" content="{city_name} Business Valuation Analyst | {state_name} Business Valuation Expert | Skerritt Economics">
    <meta property="og:description" content="Expert business valuation analyst in {city_name}. Certified valuation expert providing comprehensive valuations and litigation support.">
    <meta property="og:url" content="https://skerritteconomics.com/locations/cities/{page_slug}.html">
    <meta property="og:type" content="website">
    <meta property="og:locale" content="en_US">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="geo.region" content="US-{state.upper()}">
    <meta name="geo.placename" content="{city_name}">
    <meta name="geo.position" content="{lat};{lng}">
    <meta name="ICBM" content="{lat}, {lng}">
    <link rel="icon" type="image/x-icon" href="../../favicon.ico">
    <link rel="stylesheet" href="../../css/styles.css">
    <link rel="stylesheet" href="../../css/locations.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- Structured Data for AI Search Engines -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "name": "Skerritt Economics & Consulting - {city_name} Business Valuation Analyst",
        "description": "Expert business valuation analyst serving {city_name} attorneys and businesses with certified business valuations, company evaluations, and litigation support.",
        "url": "https://skerritteconomics.com/locations/cities/{page_slug}.html",
        "telephone": "+12036052814",
        "email": "chris@skerritteconomics.com",
        "address": {{
            "@type": "PostalAddress",
            "streetAddress": "400 Putnam Pike Ste J",
            "addressLocality": "Smithfield",
            "addressRegion": "RI",
            "postalCode": "02917",
            "addressCountry": "US"
        }},
        "areaServed": {{
            "@type": "City",
            "name": "{city_name}",
            "addressRegion": "{state.upper()}",
            "addressCountry": "US"
        }},
        "serviceType": "Business Valuation Analysis",
        "provider": {{
            "@type": "Person",
            "name": "Christopher Skerritt",
            "jobTitle": "Business Valuation Analyst",
            "description": "Certified business valuation analyst with extensive experience in {', '.join(industries[:3])} sectors."
        }},
        "geo": {{
            "@type": "GeoCoordinates",
            "latitude": {lat},
            "longitude": {lng}
        }},
        "offers": {{
            "@type": "Offer",
            "description": "Professional business valuation services including company evaluations, asset valuations, and expert witness testimony."
        }}
    }}
    </script>
</head>
<body>
    <!-- Navigation -->
    <nav class="main-nav">
        <div class="container">
            <div class="nav-wrapper">
                <a href="../../index.html" class="logo">
                    <strong>Skerritt Economics</strong>
                    <span>& Consulting</span>
                </a>
                <button class="mobile-menu-toggle" aria-label="Toggle menu">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
                <ul class="nav-menu">
                    <li><a href="../../index.html">Home</a></li>
                    <li class="has-dropdown">
                        <a href="../../services/">Services</a>
                        <ul class="dropdown">
                            <li><a href="../../services/forensic-economics/">Forensic Economics</a></li>
                            <li><a href="../../services/business-valuation/">Business Valuation</a></li>
                        </ul>
                    </li>
                    <li class="has-dropdown">
                        <a href="../../practice-areas/">Practice Areas</a>
                        <ul class="dropdown">
                            <li><a href="../../practice-areas/personal-injury/">Personal Injury & Wrongful Death</a></li>
                            <li><a href="../../practice-areas/medical-malpractice/">Medical Malpractice</a></li>
                            <li><a href="../../practice-areas/employment/">Employment Litigation</a></li>
                            <li><a href="../../practice-areas/commercial-disputes/">Commercial Disputes</a></li>
                        </ul>
                    </li>
                    <li><a href="../../case-studies/">Case Studies</a></li>
                    <li><a href="../../about/">About</a></li>
                    <li><a href="../../resources/">Resources</a></li>
                    <li><a href="../../contact/" class="nav-cta">Contact</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="location-hero">
        <div class="container">
            <div class="hero-content">
                <h1>Expert Business Valuation Analyst in {city_name}, {state_name}</h1>
                <p class="lead">Certified business valuation expert providing comprehensive company valuations, asset evaluations, and expert witness testimony for {city_name} attorneys, businesses, and financial institutions.</p>
                <div class="hero-stats">
                    <div class="stat">
                        <span class="stat-number">CVA</span>
                        <span class="stat-label">Valuation Expert</span>
                    </div>
                    <div class="stat">
                        <span class="stat-number">500+</span>
                        <span class="stat-label">Valuations Completed</span>
                    </div>
                    <div class="stat">
                        <span class="stat-number">15+</span>
                        <span class="stat-label">Years Experience</span>
                    </div>
                </div>
                <div class="hero-cta">
                    <a href="../../contact/" class="btn btn-primary">Free Consultation</a>
                    <a href="tel:+12036052814" class="btn btn-secondary">Call (203) 605-2814</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Services Overview -->
    <section class="services-overview">
        <div class="container">
            <h2>Business Valuation Services in {city_name}</h2>
            <p>As a certified business valuation analyst serving the {city_name} market, I provide comprehensive valuation services for various purposes and industries throughout {state_name}.</p>
            
            <div class="services-grid">
                <div class="service-card">
                    <div class="service-icon">📊</div>
                    <h3>Company Valuations</h3>
                    <p>Complete business valuations for merger & acquisition, litigation support, tax planning, and strategic decision-making purposes.</p>
                </div>
                <div class="service-card">
                    <div class="service-icon">🏭</div>
                    <h3>Asset Valuations</h3>
                    <p>Tangible and intangible asset valuations including equipment, intellectual property, real estate, and inventory assessments.</p>
                </div>
                <div class="service-card">
                    <div class="service-icon">⚖️</div>
                    <h3>Litigation Support</h3>
                    <p>Expert witness testimony and business valuations for divorce proceedings, shareholder disputes, and commercial litigation.</p>
                </div>
                <div class="service-card">
                    <div class="service-icon">📈</div>
                    <h3>Financial Analysis</h3>
                    <p>Comprehensive financial modeling, cash flow analysis, and market comparisons to determine accurate business values.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Industry Expertise -->
    <section class="industry-expertise">
        <div class="container">
            <h2>Industry Expertise in {city_name}</h2>
            <p>Specialized knowledge of {state_name}'s key business sectors ensures accurate and relevant valuations:</p>
            
            <div class="industries-grid">
                {' '.join([f'<div class="industry-item"><strong>{industry.title()}</strong></div>' for industry in industries])}
            </div>
            
            <div class="valuation-methods">
                <h3>Valuation Methodologies</h3>
                <div class="methods-grid">
                    <div class="method">
                        <h4>Asset Approach</h4>
                        <p>Book value, adjusted net worth, and liquidation value methods for asset-heavy businesses.</p>
                    </div>
                    <div class="method">
                        <h4>Market Approach</h4>
                        <p>Comparative analysis using recent sales of similar businesses and market multiples.</p>
                    </div>
                    <div class="method">
                        <h4>Income Approach</h4>
                        <p>Discounted cash flow and capitalization methods based on earning potential.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Why Choose Section -->
    <section class="why-choose">
        <div class="container">
            <div class="content-split">
                <div class="content-text">
                    <h2>Why Choose Our Business Valuation Services in {city_name}?</h2>
                    
                    <div class="credential">
                        <h4>🎯 Certified Business Valuation Expert</h4>
                        <ul>
                            <li><strong>Professional Certification</strong> - Advanced valuation credentials</li>
                            <li><strong>USPAP Compliance</strong> - Uniform Standards adherence</li>
                            <li><strong>Continuing Education</strong> - Current on valuation standards</li>
                            <li><strong>Professional Ethics</strong> - Independent and objective analysis</li>
                        </ul>
                    </div>

                    <div class="credential">
                        <h4>📋 Comprehensive Valuation Process</h4>
                        <ul>
                            <li><strong>Financial Analysis</strong> - Historical and projected performance</li>
                            <li><strong>Market Research</strong> - Industry and economic conditions</li>
                            <li><strong>Risk Assessment</strong> - Business and market risk factors</li>
                            <li><strong>Quality Control</strong> - Detailed review and validation</li>
                        </ul>
                    </div>

                    <div class="credential">
                        <h4>⚖️ Litigation Experience</h4>
                        <ul>
                            <li><strong>Expert Witness Testimony</strong> - State and federal courts</li>
                            <li><strong>Deposition Experience</strong> - Clear, professional presentation</li>
                            <li><strong>Cross-Examination Tested</strong> - Proven under pressure</li>
                            <li><strong>Report Writing</strong> - Detailed, defensible documentation</li>
                        </ul>
                    </div>
                </div>

                <div class="content-sidebar">
                    <div class="contact-card">
                        <h3>Get Your Business Valued</h3>
                        <p>Professional business valuation services in {city_name} for attorneys, businesses, and financial institutions.</p>
                        
                        <div class="contact-methods">
                            <a href="tel:+12036052814" class="contact-method">
                                <span class="method-icon">📞</span>
                                <span class="method-text">(203) 605-2814</span>
                            </a>
                            <a href="mailto:chris@skerritteconomics.com" class="contact-method">
                                <span class="method-icon">✉️</span>
                                <span class="method-text">chris@skerritteconomics.com</span>
                            </a>
                        </div>
                        
                        <a href="../../contact/" class="btn btn-primary btn-block">Schedule Consultation</a>
                        
                        <div class="response-time">
                            <small>✓ 24-hour response time guaranteed</small>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Service Areas -->
    <section class="service-areas">
        <div class="container">
            <h2>Business Valuation Services Throughout {state_name}</h2>
            <p>While based in Rhode Island, I provide business valuation services to attorneys and businesses throughout {state_name}, with particular expertise in the {city_name} market.</p>
            
            <div class="coverage-stats">
                <div class="coverage-stat">
                    <span class="stat-number">Statewide</span>
                    <span class="stat-label">Coverage</span>
                </div>
                <div class="coverage-stat">
                    <span class="stat-number">Remote</span>
                    <span class="stat-label">Capabilities</span>
                </div>
                <div class="coverage-stat">
                    <span class="stat-number">24hr</span>
                    <span class="stat-label">Response</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact CTA -->
    <section class="contact-cta">
        <div class="container">
            <div class="cta-content">
                <h2>Need a Business Valuation in {city_name}?</h2>
                <p>Contact Skerritt Economics & Consulting for professional business valuation services. Free initial consultation for attorneys and qualified businesses.</p>
                <div class="cta-buttons">
                    <a href="../../contact/" class="btn btn-primary">Free Consultation</a>
                    <a href="tel:+12036052814" class="btn btn-secondary">Call Now</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="main-footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>Skerritt Economics & Consulting</h3>
                    <p>Expert business valuation analyst serving {city_name} and throughout {state_name}.</p>
                    <div class="contact-info">
                        <p>📍 400 Putnam Pike Ste J, Smithfield, RI 02917</p>
                        <p>📞 <a href="tel:+12036052814">(203) 605-2814</a></p>
                        <p>✉️ <a href="mailto:chris@skerritteconomics.com">chris@skerritteconomics.com</a></p>
                    </div>
                </div>
                
                <div class="footer-section">
                    <h4>Services</h4>
                    <ul>
                        <li><a href="../../services/business-valuation/">Business Valuation</a></li>
                        <li><a href="../../services/forensic-economics/">Forensic Economics</a></li>
                        <li><a href="../../practice-areas/commercial-disputes/">Commercial Disputes</a></li>
                        <li><a href="../../practice-areas/employment/">Employment Litigation</a></li>
                    </ul>
                </div>
                
                <div class="footer-section">
                    <h4>Practice Areas</h4>
                    <ul>
                        <li><a href="../../practice-areas/personal-injury/">Personal Injury</a></li>
                        <li><a href="../../practice-areas/medical-malpractice/">Medical Malpractice</a></li>
                        <li><a href="../../practice-areas/employment/">Employment Law</a></li>
                        <li><a href="../../practice-areas/commercial-disputes/">Commercial Litigation</a></li>
                    </ul>
                </div>
                
                <div class="footer-section">
                    <h4>Company</h4>
                    <ul>
                        <li><a href="../../about/">About</a></li>
                        <li><a href="../../case-studies/">Case Studies</a></li>
                        <li><a href="../../resources/">Resources</a></li>
                        <li><a href="../../contact/">Contact</a></li>
                    </ul>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>&copy; 2024 Skerritt Economics & Consulting. All rights reserved.</p>
                <p>Professional business valuation analyst serving {city_name}, {state_name}</p>
            </div>
        </div>
    </footer>

    <script src="../../js/main.js"></script>
</body>
</html>'''

def main():
    """Generate all business valuation analyst pages"""
    print("Generating business valuation analyst pages for top 15 cities in all 50 states...")
    
    base_dir = "/Users/chrisskerritt/SEC/locations/cities"
    os.makedirs(base_dir, exist_ok=True)
    
    total_pages = 0
    generated_pages = []
    
    for state_code, cities in CITIES_BY_STATE.items():
        print(f"Generating pages for {state_code.upper()}...")
        
        for city_name, state, lat, lng in cities:
            page_slug = create_city_slug(city_name, state)
            file_path = os.path.join(base_dir, f"{page_slug}.html")
            
            # Generate page content
            content = generate_page_content(city_name, state, lat, lng)
            
            # Write file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            generated_pages.append({
                'name': f"{city_name}, {state.upper()}",
                'path': f"locations/cities/{page_slug}.html",
                'type': 'business-valuation'
            })
            total_pages += 1
    
    print(f"Generated {total_pages} business valuation analyst pages")
    
    # Create a summary file
    summary = {
        'generated_at': datetime.now().isoformat(),
        'total_pages': total_pages,
        'pages': generated_pages
    }
    
    with open('/Users/chrisskerritt/SEC/business_valuation_pages_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"Summary saved to business_valuation_pages_summary.json")
    print(f"Total business valuation analyst pages generated: {total_pages}")

if __name__ == "__main__":
    main()