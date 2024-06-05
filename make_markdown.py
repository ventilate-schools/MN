import os
import pandas as pd

schools = {
    "Atwater Cosmos Grove City School District": [
        {
            "school_name": "Atwater Cosmos Grove City High School",
            "address": "27250 Minnesota Hwy 4, Grove City, MN 56243",
            "phone": "320-244-4730",
            "website": "https://www.acgcschools.org/o/acgc-high-school",
            "students": 300
        },
        {
            "school_name": "Atwater Cosmos Grove City Elementary Grades 5 and 6",
            "address": "27250 Minnesota Hwy 4, Grove City, MN 56243",
            "phone": "320-244-4677",
            "website": "https://www.acgc.k12.mn.us",
            "students": 150
        }
    ],
    "Academia Cesar Chavez Charter School": [
        {
            "school_name": "Academia Cesar Chavez School",
            "address": "1801 Lacrosse Ave, St Paul, MN 55119",
            "phone": "651-778-2940",
            "website": "https://www.cesarchavezschool.com",
            "students": 500
        }
    ],
    "Academic Arts High School": [
        {
            "school_name": "Academic Arts High School",
            "address": "60 Marie Ave East Suite 220, West Saint Paul, MN 55118",
            "phone": "651-457-7427",
            "website": "https://www.academicarts.org",
            "students": 104
        }
    ],
    "Academy Of Construction And Engineering": [
        {
            "school_name": "Academy Of Construction And Engineering",
            "address": "1500 James Ave N, Minneapolis, MN 55411",
            "phone": "612-668-1700",
            "website": "https://ace.mpls.k12.mn.us",
            "students": 200
        }
    ],
    "Achieve Language Academy": [
        {
            "school_name": "Achieve Language Academy",
            "address": "2169 Stillwater Ave E, St Paul, MN 55119",
            "phone": "651-738-4875",
            "website": "https://www.achievemn.org",
            "students": 400
        }
    ],
    "Ada-Borup Public School District": [
        {
            "school_name": "Ada-Borup High School",
            "address": "604 West Thorpe Ave, Ada, MN 56510",
            "phone": "218-784-5300",
            "website": "https://www.ada.k12.mn.us",
            "students": 300
        }
    ],
    "Adrian Public School District": [
        {
            "school_name": "Adrian High School",
            "address": "415 Kentucky Ave, Adrian, MN 56110",
            "phone": "507-483-2232",
            "website": "https://www.isd511.net",
            "students": 250
        }
    ],
    "The Academy for Sciences and Agriculture High School": [
        {
            "school_name": "The Academy for Sciences and Agriculture High School",
            "address": "100 Vadnais Blvd, Vadnais Heights, MN 55127",
            "phone": "651-209-3910",
            "website": "https://www.afsahighschool.com",
            "students": 300
        }
    ],
    "Agamim Classical Academy": [
        {
            "school_name": "Agamim Classical Academy",
            "address": "5300 France Ave S, Edina, MN 55410",
            "phone": "952-856-2531",
            "website": "https://www.agamim.org",
            "students": 200
        }
    ],
    "Aitkin Public School District": [
        {
            "school_name": "Aitkin High School",
            "address": "306 2nd St NW, Aitkin, MN 56431",
            "phone": "218-927-2115",
            "website": "https://www.isd1.org",
            "students": 400
        }
    ],
    "Albany Public School District": [
        {
            "school_name": "Albany High School",
            "address": "30 Forest Ave, Albany, MN 56307",
            "phone": "320-845-2171",
            "website": "https://www.district745.org",
            "students": 500
        }
    ],
    "Albert Lea Public School District": [
        {
            "school_name": "Albert Lea High School",
            "address": "2000 Tiger Ln, Albert Lea, MN 56007",
            "phone": "507-379-5340",
            "website": "https://www.alschools.org",
            "students": 1200
        }
    ],
    "Alden-Conger Public School District": [
        {
            "school_name": "Alden-Conger High School",
            "address": "215 N Broadway, Alden, MN 56009",
            "phone": "507-874-3240",
            "website": "https://www.acps.k12.mn.us",
            "students": 300
        }
    ],
    "Alexandria Public School District": [
        {
            "school_name": "Alexandria Area High School",
            "address": "4300 Pioneer Rd SE, Alexandria, MN 56308",
            "phone": "320-762-2142",
            "website": "https://www.alexschools.org",
            "students": 1300
        }
    ],
    "Annandale Public School District": [
        {
            "school_name": "Annandale High School",
            "address": "855 Hemlock St E, Annandale, MN 55302",
            "phone": "320-274-8208",
            "website": "https://www.isd876.org",
            "students": 600
        }
    ],
    "Anoka-Hennepin Public School Dist.": [
        {
            "school_name": "Anoka High School",
            "address": "3939 7th Ave N, Anoka, MN 55303",
            "phone": "763-506-6200",
            "website": "https://www.ahschools.us",
            "students": 2400
        }
    ],
    "Arcadia Charter School": [
        {
            "school_name": "Arcadia Charter School",
            "address": "1719 Cannon Rd, Northfield, MN 55057",
            "phone": "507-663-8806",
            "website": "https://www.arcadiacharterschool.org",
            "students": 120
        }
    ],
    "Art And Science Academy": [
        {
            "school_name": "Art And Science Academy",
            "address": "903 6th Ave NE, Isanti, MN 55040",
            "phone": "763-444-0342",
            "website": "https://www.artandscienceacademy.k12.mn.us",
            "students": 300
        }
    ],
    "Ashby Public School District": [
        {
            "school_name": "Ashby High School",
            "address": "300 Birch Ave, Ashby, MN 56309",
            "phone": "218-747-2257",
            "website": "https://www.ashby.k12.mn.us",
            "students": 150
        }
    ],
    "Aspen Academy": [
        {
            "school_name": "Aspen Academy",
            "address": "14825 Zinran Ave, Savage, MN 55378",
            "phone": "952-226-5940",
            "website": "https://www.aspenacademymn.org",
            "students": 500
        }
    ],
    "Athlos Academy Of Saint Cloud": [
        {
            "school_name": "Athlos Academy Of Saint Cloud",
            "address": "3701 33rd St S, St Cloud, MN 56301",
            "phone": "320-281-4430",
            "website": "https://www.athlosstcloud.org",
            "students": 800
        }
    ],
    "Athlos Leadership Academy": [
        {
            "school_name": "Athlos Leadership Academy",
            "address": "10100 Noble Pkwy N, Brooklyn Park, MN 55443",
            "phone": "763-777-8942",
            "website": "https://www.athlosbrooklynpark.org",
            "students": 900
        }
    ],
    "Augsburg Fairview Academy": [
        {
            "school_name": "Augsburg Fairview Academy",
            "address": "2504 Columbus Ave, Minneapolis, MN 55404",
            "phone": "612-333-1614",
            "website": "https://www.afa.tc",
            "students": 150
        }
    ],
    "Aurora Charter School": [
        {
            "school_name": "Aurora Charter School",
            "address": "2101 E 26th St, Minneapolis, MN 55404",
            "phone": "612-722-1999",
            "website": "https://www.auroracharterschool.org",
            "students": 400
        }
    ],
    "Aurora Waasakone Community of Learning": [
        {
            "school_name": "Aurora Waasakone Community of Learning",
            "address": "208 Central Ave, Bemidji, MN 56601",
            "phone": "218-444-0220",
            "website": "https://www.awclmn.org",
            "students": 100
        }
    ],
    "Austin Albert Lea Area Special Education": [
        {
            "school_name": "Austin Albert Lea Area Special Education Cooperative",
            "address": "401 3rd Ave NW, Austin, MN 55912",
            "phone": "507-460-1800",
            "website": "https://www.austin.k12.mn.us",
            "students": "N/A"
        }
    ],
    "Austin Public School District": [
        {
            "school_name": "Austin High School",
            "address": "301 3rd St NW, Austin, MN 55912",
            "phone": "507-460-1800",
            "website": "https://www.austin.k12.mn.us",
            "students": 1200
        }
    ],
    "Avalon School": [
        {
            "school_name": "Avalon School",
            "address": "700 Glendale St, St Paul, MN 55114",
            "phone": "651-649-5495",
            "website": "https://www.avalonschool.org",
            "students": 200
        }
    ],
    "Badger Public School District": [
        {
            "school_name": "Badger High School",
            "address": "110 Carpenter Ave, Badger, MN 56714",
            "phone": "218-528-3201",
            "website": "https://www.badger.k12.mn.us",
            "students": 224
        },
        {
            "school_name": "Badger Elementary School",
            "address": "110 Carpenter Ave, Badger, MN 56714",
            "phone": "218-528-3201",
            "website": "https://www.badger.k12.mn.us",
            "students": 224
        }
    ],
    "Bagley Public School District": [
        {
            "school_name": "Bagley High School",
            "address": "202 Bagley Ave NW, Bagley, MN 56621",
            "phone": "218-694-3120",
            "website": "https://www.bagley.k12.mn.us",
            "students": 935
        },
        {
            "school_name": "Bagley Elementary School",
            "address": "202 Bagley Ave NW, Bagley, MN 56621",
            "phone": "218-694-6528",
            "website": "https://www.bagley.k12.mn.us",
            "students": 935
        }
    ],
    "Barnesville Public School Dist.": [
        {
            "school_name": "Barnesville High School",
            "address": "302 3rd Street SE, Barnesville, MN 56514",
            "phone": "218-354-2228",
            "website": "https://www.barnesville.k12.mn.us",
            "students": 400
        },
        {
            "school_name": "Barnesville Elementary School",
            "address": "302 3rd Street SE, Barnesville, MN 56514",
            "phone": "218-354-2300",
            "website": "https://www.barnesville.k12.mn.us",
            "students": 400
        }
    ],
    "Barnum Public School District": [
        {
            "school_name": "Barnum High School",
            "address": "3675 County Road 140, Barnum, MN 55707",
            "phone": "218-389-6978",
            "website": "https://www.isd91.org",
            "students": 300
        },
        {
            "school_name": "Barnum Elementary School",
            "address": "3675 County Road 140, Barnum, MN 55707",
            "phone": "218-389-6978",
            "website": "https://www.isd91.org",
            "students": 300
        }
    ],
    "Battle Lake Public School District": [
        {
            "school_name": "Battle Lake High School",
            "address": "402 Summit St W, Battle Lake, MN 56515",
            "phone": "218-864-5215",
            "website": "https://www.battlelake.k12.mn.us",
            "students": 250
        },
        {
            "school_name": "Battle Lake Elementary School",
            "address": "402 Summit St W, Battle Lake, MN 56515",
            "phone": "218-864-5215",
            "website": "https://www.battlelake.k12.mn.us",
            "students": 250
        }
    ],
    "Bdote Learning Center": [
        {
            "school_name": "Bdote Learning Center",
            "address": "3216 E 29th St, Minneapolis, MN 55406",
            "phone": "612-729-9266",
            "website": "https://www.bdote.org",
            "students": 150
        }
    ],
    "Beacon Academy": [
        {
            "school_name": "Beacon Academy",
            "address": "3415 Louisiana Ave N, Crystal, MN 55427",
            "phone": "763-546-9999",
            "website": "https://www.beaconacademy.com",
            "students": 500
        }
    ],
    "Becker Public School District": [
        {
            "school_name": "Becker High School",
            "address": "12000 Hancock St, Becker, MN 55308",
            "phone": "763-261-4501",
            "website": "https://www.becker.k12.mn.us",
            "students": 800
        },
        {
            "school_name": "Becker Middle School",
            "address": "12000 Hancock St, Becker, MN 55308",
            "phone": "763-261-4501",
            "website": "https://www.becker.k12.mn.us",
            "students": 700
        },
        {
            "school_name": "Becker Elementary School",
            "address": "12000 Hancock St, Becker, MN 55308",
            "phone": "763-261-4501",
            "website": "https://www.becker.k12.mn.us",
            "students": 600
        }
    ],
    "Belgrade-Brooten-Elrosa School Dist.": [
        {
            "school_name": "Belgrade-Brooten-Elrosa High School",
            "address": "710 Washburn Ave, Belgrade, MN 56312",
            "phone": "320-254-8211",
            "website": "https://www.bbe.k12.mn.us",
            "students": 400
        },
        {
            "school_name": "Belgrade-Brooten-Elrosa Elementary School",
            "address": "710 Washburn Ave, Belgrade, MN 56312",
            "phone": "320-254-8211",
            "website": "https://www.bbe.k12.mn.us",
            "students": 300
        }
    ],
    "Belle Plaine Public School District": [
        {
            "school_name": "Belle Plaine High School",
            "address": "220 S Market St, Belle Plaine, MN 56011",
            "phone": "952-873-2403",
            "website": "https://www.belleplaine.k12.mn.us",
            "students": 500
        },
        {
            "school_name": "Belle Plaine Elementary School",
            "address": "220 S Market St, Belle Plaine, MN 56011",
            "phone": "952-873-2403",
            "website": "https://www.belleplaine.k12.mn.us",
            "students": 400
        }
    ],
    "Bemidji Public School District": [
        {
            "school_name": "Bemidji High School",
            "address": "2900 Division St W, Bemidji, MN 56601",
            "phone": "218-444-1600",
            "website": "https://www.bemidji.k12.mn.us",
            "students": 1500
        },
        {
            "school_name": "Bemidji Middle School",
            "address": "1910 Middle School Ave NW, Bemidji, MN 56601",
            "phone": "218-333-3215",
            "website": "https://www.bemidji.k12.mn.us",
            "students": 1200
        },
        {
            "school_name": "Bemidji Elementary School",
            "address": "1910 Middle School Ave NW, Bemidji, MN 56601",
            "phone": "218-333-3215",
            "website": "https://www.bemidji.k12.mn.us",
            "students": 1000
        }
    ],
    "Benson Public School District": [
        {
            "school_name": "Benson High School",
            "address": "1400 Montana Ave, Benson, MN 56215",
            "phone": "320-843-2710",
            "website": "https://www.benson.k12.mn.us",
            "students": 400
        },
        {
            "school_name": "Benson Elementary School",
            "address": "1400 Montana Ave, Benson, MN 56215",
            "phone": "320-843-2710",
            "website": "https://www.benson.k12.mn.us",
            "students": 300
        }
    ],
    "Benton-Stearns Ed. District": [
        {
            "school_name": "Benton-Stearns Education District",
            "address": "517 2nd St S, Sartell, MN 56377",
            "phone": "320-252-8427",
            "website": "https://www.bentonstearns.k12.mn.us",
            "students": 200
        }
    ],
    "Bertha-Hewitt Public School Dist.": [
        {
            "school_name": "Bertha-Hewitt High School",
            "address": "310 Central Ave S, Bertha, MN 56437",
            "phone": "218-924-2500",
            "website": "https://www.bertha.k12.mn.us",
            "students": 300
        },
        {
            "school_name": "Bertha-Hewitt Elementary School",
            "address": "310 Central Ave S, Bertha, MN 56437",
            "phone": "218-924-2500",
            "website": "https://www.bertha.k12.mn.us",
            "students": 200
        }
    ],
    "Best Academy": [
        {
            "school_name": "Best Academy",
            "address": "1300 Olson Memorial Hwy, Minneapolis, MN 55411",
            "phone": "612-876-4105",
            "website": "https://www.thebestacademy.org",
            "students": 500
        }
    ],
    "Big Lake Schools": [
        {
            "school_name": "Big Lake High School",
            "address": "501 Minnesota Ave, Big Lake, MN 55309",
            "phone": "763-262-2547",
            "website": "https://www.biglakeschools.org",
            "students": 1000
        },
        {
            "school_name": "Big Lake Middle School",
            "address": "501 Minnesota Ave, Big Lake, MN 55309",
            "phone": "763-262-2547",
            "website": "https://www.biglakeschools.org",
            "students": 800
        },
        {
            "school_name": "Big Lake Elementary School",
            "address": "501 Minnesota Ave, Big Lake, MN 55309",
            "phone": "763-262-2547",
            "website": "https://www.biglakeschools.org",
            "students": 600
        }
    ],
    "Big Picture Twin Cities": [
        {
            "school_name": "Big Picture Twin Cities",
            "address": "5929 Brooklyn Blvd, Brooklyn Center, MN 55429",
            "phone": "763-200-2200",
            "website": "https://www.bigpicturetwincities.org",
            "students": 150
        }
    ],
    "Birch Grove Community School": [
        {
            "school_name": "Birch Grove Community School",
            "address": "27 Cedar Grove Ln, Tofte, MN 55615",
            "phone": "218-663-0170",
            "website": "https://www.birchgroveschool.com",
            "students": 50
        }
    ],
    "Bird Island-Olivia-Lake Lillian School District": [
        {
            "school_name": "BOLD High School",
            "address": "701 S 9th St, Olivia, MN 56277",
            "phone": "320-523-1031",
            "website": "https://www.bold.k12.mn.us",
            "students": 400
        },
        {
            "school_name": "BOLD Elementary School",
            "address": "701 S 9th St, Olivia, MN 56277",
            "phone": "320-523-1031",
            "website": "https://www.bold.k12.mn.us",
            "students": 300
        }
    ],
    "Blackduck Public School District": [
        {
            "school_name": "Blackduck High School",
            "address": "156 1st St NE, Blackduck, MN 56630",
            "phone": "218-835-5200",
            "website": "https://www.blackduck.k12.mn.us",
            "students": 300
        },
        {
            "school_name": "Blackduck Elementary School",
            "address": "156 1st St NE, Blackduck, MN 56630",
            "phone": "218-835-5200",
            "website": "https://www.blackduck.k12.mn.us",
            "students": 200
        }
    ],
    "Blooming Prairie Public School Dist.": [
        {
            "school_name": "Blooming Prairie High School",
            "address": "202 4th Ave NW, Blooming Prairie, MN 55917",
            "phone": "507-583-4426",
            "website": "https://www.bpschools.org",
            "students": 400
        },
        {
            "school_name": "Blooming Prairie Elementary School",
            "address": "202 4th Ave NW, Blooming Prairie, MN 55917",
            "phone": "507-583-4426",
            "website": "https://www.bpschools.org",
            "students": 300
        }
    ],
    "Bloomington Public School District": [
        {
            "school_name": "Jefferson High School",
            "address": "4001 W 102nd St, Bloomington, MN 55437",
            "phone": "952-806-7600",
            "website": "https://www.bloomington.k12.mn.us",
            "students": 1600
        },
        {
            "school_name": "Kennedy High School",
            "address": "9701 Nicollet Ave S, Bloomington, MN 55420",
            "phone": "952-681-5000",
            "website": "https://www.bloomington.k12.mn.us",
            "students": 1500
        },
        {
            "school_name": "Oak Grove Middle School",
            "address": "1300 W 106th St, Bloomington, MN 55431",
            "phone": "952-681-6600",
            "website": "https://www.bloomington.k12.mn.us",
            "students": 800
        },
        {
            "school_name": "Valley View Middle School",
            "address": "8900 Portland Ave S, Bloomington, MN 55420",
            "phone": "952-681-5800",
            "website": "https://www.bloomington.k12.mn.us",
            "students": 700
        },
        {
            "school_name": "Olson Middle School",
            "address": "4551 W 102nd St, Bloomington, MN 55437",
            "phone": "952-806-8600",
            "website": "https://www.bloomington.k12.mn.us",
            "students": 600
        }
    ],
    "Blue Earth Area Public School": [
        {
            "school_name": "Blue Earth Area High School",
            "address": "1125 Highway 169 N, Blue Earth, MN 56013",
            "phone": "507-526-3201",
            "website": "https://www.beaschools.org",
            "students": 500
        },
        {
            "school_name": "Blue Earth Area Elementary School",
            "address": "1125 Highway 169 N, Blue Earth, MN 56013",
            "phone": "507-526-3201",
            "website": "https://www.beaschools.org",
            "students": 400
        }
    ],
    "Bluesky Charter School": [
        {
            "school_name": "Bluesky Charter School",
            "address": "33 Wentworth Ave E, West St Paul, MN 55118",
            "phone": "651-642-0888",
            "website": "https://www.blueskyschool.org",
            "students": 500
        }
    ],
    "Bluffview Montessori": [
        {
            "school_name": "Bluffview Montessori School",
            "address": "1321 Gilmore Ave, Winona, MN 55987",
            "phone": "507-452-2807",
            "website": "https://www.bluffviewmontessori.org",
            "students": 200
        }
    ],
    "Braham Public School District": [
        {
            "school_name": "Braham High School",
            "address": "531 Elmhurst Ave S, Braham, MN 55006",
            "phone": "320-396-4444",
            "website": "https://www.braham.k12.mn.us",
            "students": 400
        },
        {
            "school_name": "Braham Elementary School",
            "address": "531 Elmhurst Ave S, Braham, MN 55006",
            "phone": "320-396-4444",
            "website": "https://www.braham.k12.mn.us",
            "students": 300
        }
    ],
    "Brainerd Public School District": [
        {
            "school_name": "Brainerd High School",
            "address": "702 S 5th St, Brainerd, MN 56401",
            "phone": "218-454-6200",
            "website": "https://www.isd181.org",
            "students": 1800
        },
        {
            "school_name": "Brainerd Middle School",
            "address": "702 S 5th St, Brainerd, MN 56401",
            "phone": "218-454-6200",
            "website": "https://www.isd181.org",
            "students": 1500
        },
        {
            "school_name": "Brainerd Elementary School",
            "address": "702 S 5th St, Brainerd, MN 56401",
            "phone": "218-454-6200",
            "website": "https://www.isd181.org",
            "students": 1200
        }
    ],
"Brandon-Evansville Public Schools": [
        {
            "school_name": "Brandon-Evansville High School",
            "address": "206 W 3rd St, Brandon, MN 56315",
            "phone": "320-834-4084",
            "website": "https://www.b-e.k12.mn.us",
            "students": 300
        },
        {
            "school_name": "Brandon-Evansville Elementary School",
            "address": "123 2nd Ave, Evansville, MN 56326",
            "phone": "320-834-4084",
            "website": "https://www.b-e.k12.mn.us",
            "students": 200
        }
    ],
    "Breckenridge Public School District": [
        {
            "school_name": "Breckenridge High School",
            "address": "710 13th St N, Breckenridge, MN 56520",
            "phone": "218-643-2694",
            "website": "https://www.breckenridge.k12.mn.us",
            "students": 300
        },
        {
            "school_name": "Breckenridge Elementary School",
            "address": "810 Beede Ave, Breckenridge, MN 56520",
            "phone": "218-643-6681",
            "website": "https://www.breckenridge.k12.mn.us",
            "students": 200
        }
    ],
    "Brooklyn Center School District": [
        {
            "school_name": "Brooklyn Center High School",
            "address": "6500 Humboldt Ave N, Brooklyn Center, MN 55430",
            "phone": "763-561-2120",
            "website": "https://www.bccs286.org",
            "students": 800
        },
        {
            "school_name": "Earle Brown Elementary School",
            "address": "1500 59th Ave N, Brooklyn Center, MN 55430",
            "phone": "763-561-4480",
            "website": "https://www.bccs286.org",
            "students": 600
        }
    ],
    "Browerville Public School District": [
        {
            "school_name": "Browerville High School",
            "address": "620 Park Ave N, Browerville, MN 56438",
            "phone": "320-594-2272",
            "website": "https://www.browerville.k12.mn.us",
            "students": 200
        },
        {
            "school_name": "Browerville Elementary School",
            "address": "620 Park Ave N, Browerville, MN 56438",
            "phone": "320-594-2272",
            "website": "https://www.browerville.k12.mn.us",
            "students": 150
        }
    ],
    "Browns Valley Public School Dist.": [
        {
            "school_name": "Browns Valley School",
            "address": "118 Church St, Browns Valley, MN 56219",
            "phone": "320-695-2103",
            "website": "https://www.brownsvalley.k12.mn.us",
            "students": 100
        }
    ],
    "Buffalo Lk-Hector-Stewart Public School": [
        {
            "school_name": "Buffalo Lake-Hector-Stewart High School",
            "address": "220 3rd St E, Hector, MN 55342",
            "phone": "320-848-2233",
            "website": "https://www.blhsd.org",
            "students": 300
        },
        {
            "school_name": "Buffalo Lake-Hector-Stewart Elementary School",
            "address": "211 3rd St E, Hector, MN 55342",
            "phone": "320-848-2233",
            "website": "https://www.blhsd.org",
            "students": 200
        }
    ],
    "Buffalo-Hanover-Montrose Public School": [
        {
            "school_name": "Buffalo High School",
            "address": "877 Bison Blvd, Buffalo, MN 55313",
            "phone": "763-682-8100",
            "website": "https://www.bhmschools.org",
            "students": 1600
        },
        {
            "school_name": "Buffalo Middle School",
            "address": "1300 MN-25, Buffalo, MN 55313",
            "phone": "763-682-8200",
            "website": "https://www.bhmschools.org",
            "students": 1200
        },
        {
            "school_name": "Tatanka Elementary School",
            "address": "703 8th St NE, Buffalo, MN 55313",
            "phone": "763-682-8600",
            "website": "https://www.bhmschools.org",
            "students": 600
        }
    ],
    "Bug-O-Nay-Ge-Shig School": [
        {
            "school_name": "Bug-O-Nay-Ge-Shig School",
            "address": "15353 Silver Eagle Dr NW, Bena, MN 56626",
            "phone": "218-665-3000",
            "website": "https://www.bugonaygeshig.org",
            "students": 200
        }
    ],
    "Burnsville Public School District": [
        {
            "school_name": "Burnsville High School",
            "address": "600 E Hwy 13, Burnsville, MN 55337",
            "phone": "952-707-2100",
            "website": "https://www.isd191.org",
            "students": 2500
        },
        {
            "school_name": "Eagle Ridge Middle School",
            "address": "13955 Glendale Rd, Savage, MN 55378",
            "phone": "952-707-2800",
            "website": "https://www.isd191.org",
            "students": 1000
        },
        {
            "school_name": "Gideon Pond Elementary School",
            "address": "613 E 130th St, Burnsville, MN 55337",
            "phone": "952-707-3000",
            "website": "https://www.isd191.org",
            "students": 500
        }
    ],
    "Butterfield Public School District": [
        {
            "school_name": "Butterfield-Odin High School",
            "address": "440 Hubbard Ave, Butterfield, MN 56120",
            "phone": "507-956-2771",
            "website": "https://www.butterfield.k12.mn.us",
            "students": 150
        },
        {
            "school_name": "Butterfield-Odin Elementary School",
            "address": "440 Hubbard Ave, Butterfield, MN 56120",
            "phone": "507-956-2771",
            "website": "https://www.butterfield.k12.mn.us",
            "students": 100
        }
    ],
    "Byron Public School District": [
        {
            "school_name": "Byron High School",
            "address": "1887 2nd Ave NW, Byron, MN 55920",
            "phone": "507-775-2301",
            "website": "https://www.bears.byron.k12.mn.us",
            "students": 600
        },
        {
            "school_name": "Byron Middle School",
            "address": "601 4th St NW, Byron, MN 55920",
            "phone": "507-775-2189",
            "website": "https://www.bears.byron.k12.mn.us",
            "students": 500
        },
        {
            "school_name": "Byron Elementary School",
            "address": "820 7th St NE, Byron, MN 55920",
            "phone": "507-775-6620",
            "website": "https://www.bears.byron.k12.mn.us",
            "students": 400
        }
    ],
    "Caledonia Public School District": [
        {
            "school_name": "Caledonia High School",
            "address": "825 N Warrior Ave, Caledonia, MN 55921",
            "phone": "507-725-3316",
            "website": "https://www.cps.k12.mn.us",
            "students": 300
        },
        {
            "school_name": "Caledonia Elementary School",
            "address": "511 W Main St, Caledonia, MN 55921",
            "phone": "507-725-5205",
            "website": "https://www.cps.k12.mn.us",
            "students": 200
        }
    ],
    "Cambridge-Isanti Public School Dist.": [
        {
            "school_name": "Cambridge-Isanti High School",
            "address": "430 NW 8th Ave, Cambridge, MN 55008",
            "phone": "763-689-6066",
            "website": "https://www.c-ischools.org",
            "students": 1200
        },
        {
            "school_name": "Cambridge Middle School",
            "address": "31374 Xylite St NE, Cambridge, MN 55008",
            "phone": "763-552-6300",
            "website": "https://www.c-ischools.org",
            "students": 800
        },
        {
            "school_name": "Isanti Intermediate School",
            "address": "101 9th Ave NE, Isanti, MN 55040",
            "phone": "763-552-8800",
            "website": "https://www.c-ischools.org",
            "students": 600
        }
    ],
    "Campbell-Tintah Public School Dist.": [
        {
            "school_name": "Campbell-Tintah High School",
            "address": "430 Connecticut Ave, Campbell, MN 56522",
            "phone": "218-630-5311",
            "website": "https://www.campbell.k12.mn.us",
            "students": 100
        },
        {
            "school_name": "Campbell-Tintah Elementary School",
            "address": "430 Connecticut Ave, Campbell, MN 56522",
            "phone": "218-630-5311",
            "website": "https://www.campbell.k12.mn.us",
            "students": 50
        }
    ],
    "Canby Public School District": [
        {
            "school_name": "Canby High School",
            "address": "307 1st St W, Canby, MN 56220",
            "phone": "507-223-2002",
            "website": "https://www.canbymn.org",
            "students": 300
        },
        {
            "school_name": "Canby Elementary School",
            "address": "307 1st St W, Canby, MN 56220",
            "phone": "507-223-2002",
            "website": "https://www.canbymn.org",
            "students": 200
        }
    ],
    "Cannon Falls Public School District": [
        {
            "school_name": "Cannon Falls High School",
            "address": "820 E Minnesota St, Cannon Falls, MN 55009",
            "phone": "507-263-6800",
            "website": "https://www.cannonfallsschools.com",
            "students": 400
        },
        {
            "school_name": "Cannon Falls Elementary School",
            "address": "820 E Minnesota St, Cannon Falls, MN 55009",
            "phone": "507-263-6800",
            "website": "https://www.cannonfallsschools.com",
            "students": 300
        }
    ],
    "Cannon River Stem School": [
        {
            "school_name": "Cannon River STEM School",
            "address": "1800 14th St NE, Faribault, MN 55021",
            "phone": "507-331-7836",
            "website": "https://www.cannonriverstemschool.org",
            "students": 300
        }
    ],
    "Career Pathways": [
        {
            "school_name": "Career Pathways",
            "address": "1355 Pierce Butler Route, St Paul, MN 55104",
            "phone": "651-400-1781",
            "website": "https://www.cpathmn.org",
            "students": 150
        }
    ],
    "Carlton Public School District": [
        {
            "school_name": "Carlton High School",
            "address": "405 School Ave, Carlton, MN 55718",
            "phone": "218-384-4225",
            "website": "https://www.carlton.k12.mn.us",
            "students": 200
        },
        {
            "school_name": "South Terrace Elementary School",
            "address": "530 Stine Dr, Carlton, MN 55718",
            "phone": "218-384-4225",
            "website": "https://www.carlton.k12.mn.us",
            "students": 150
        }
    ],
    "Cass Lake-Bena Public Schools": [
        {
            "school_name": "Cass Lake-Bena High School",
            "address": "15314 State Hwy 371 NW, Cass Lake, MN 56633",
            "phone": "218-335-2203",
            "website": "https://www.clbs.k12.mn.us",
            "students": 400
        },
        {
            "school_name": "Cass Lake-Bena Elementary School",
            "address": "15314 State Hwy 371 NW, Cass Lake, MN 56633",
            "phone": "218-335-2203",
            "website": "https://www.clbs.k12.mn.us",
            "students": 300
        }
    ],
    "Cedar Mountain School District": [
        {
            "school_name": "Cedar Mountain High School",
            "address": "310 Somerville Ave N, Morgan, MN 56266",
            "phone": "507-249-5880",
            "website": "https://www.cms.mntm.org",
            "students": 200
        },
        {
            "school_name": "Cedar Mountain Elementary School",
            "address": "310 Somerville Ave N, Morgan, MN 56266",
            "phone": "507-249-5880",
            "website": "https://www.cms.mntm.org",
            "students": 150
        }
    ],
    "Cedar Riverside Community School": [
        {
            "school_name": "Cedar Riverside Community School",
            "address": "1610 S 6th St, Minneapolis, MN 55454",
            "phone": "612-339-5767",
            "website": "https://www.crcs-school.org",
            "students": 200
        }
    ],
    "Centennial Public School District": [
        {
            "school_name": "Centennial High School",
            "address": "4757 North Rd, Circle Pines, MN 55014",
            "phone": "763-792-5000",
            "website": "https://www.isd12.org",
            "students": 2000
        },
        {
            "school_name": "Centennial Middle School",
            "address": "399 Elm St, Lino Lakes, MN 55014",
            "phone": "763-792-5400",
            "website": "https://www.isd12.org",
            "students": 1500
        },
        {
            "school_name": "Centennial Elementary School",
            "address": "399 Elm St, Lino Lakes, MN 55014",
            "phone": "763-792-5400",
            "website": "https://www.isd12.org",
            "students": 1000
        }
    ],
    "Central Minnesota Jt. Powers District": [
        {
            "school_name": "Central Minnesota Joint Powers District",
            "address": "415 4th St NW, Willmar, MN 56201",
            "phone": "320-231-5184",
            "website": "https://www.cmjpd.org",
            "students": 100
        }
    ],
    "Central Public School District": [
        {
            "school_name": "Central High School",
            "address": "531 Central Ave, Norwood Young America, MN 55368",
            "phone": "952-467-7100",
            "website": "https://www.central.k12.mn.us",
            "students": 400
        },
        {
            "school_name": "Central Elementary School",
            "address": "531 Central Ave, Norwood Young America, MN 55368",
            "phone": "952-467-7100",
            "website": "https://www.central.k12.mn.us",
            "students": 300
        }
    ],
    "Chatfield Public Schools": [
        {
            "school_name": "Chatfield High School",
            "address": "205 Union St NE, Chatfield, MN 55923",
            "phone": "507-867-4210",
            "website": "https://www.chatfield.k12.mn.us",
            "students": 400
        },
        {
            "school_name": "Chatfield Elementary School",
            "address": "205 Union St NE, Chatfield, MN 55923",
            "phone": "507-867-4210",
            "website": "https://www.chatfield.k12.mn.us",
            "students": 300
        }
    ],
    "Chisago Lakes School District": [
        {
            "school_name": "Chisago Lakes High School",
            "address": "29400 Olinda Trail, Lindstrom, MN 55045",
            "phone": "651-213-2500",
            "website": "https://www.isd2144.org",
            "students": 1000
        },
        {
            "school_name": "Chisago Lakes Middle School",
            "address": "13750 Lake Blvd, Lindstrom, MN 55045",
            "phone": "651-213-2400",
            "website": "https://www.isd2144.org",
            "students": 800
        },
        {
            "school_name": "Chisago Lakes Elementary School",
            "address": "11009 284th St, Chisago City, MN 55013",
            "phone": "651-213-2200",
            "website": "https://www.isd2144.org",
            "students": 600
        }
    ],
    "Chisholm Public School District": [
        {
            "school_name": "Chisholm High School",
            "address": "301 4th St SW, Chisholm, MN 55719",
            "phone": "218-254-5726",
            "website": "https://www.chisholm.k12.mn.us",
            "students": 300
        },
        {
            "school_name": "Vaughan-Steffensrud Elementary School",
            "address": "1000 1st Ave SW, Chisholm, MN 55719",
            "phone": "218-254-5726",
            "website": "https://www.chisholm.k12.mn.us",
            "students": 200
        }
    ],
    "Chokio-Alberta Public School Dist.": [
        {
            "school_name": "Chokio-Alberta High School",
            "address": "311 1st St W, Chokio, MN 56221",
            "phone": "320-324-7131",
            "website": "https://www.chokioalberta.k12.mn.us",
            "students": 100
        },
        {
            "school_name": "Chokio-Alberta Elementary School",
            "address": "311 1st St W, Chokio, MN 56221",
            "phone": "320-324-7131",
            "website": "https://www.chokioalberta.k12.mn.us",
            "students": 50
        }
    ],
    "Circle Of Life Academy": [
        {
            "school_name": "Circle Of Life Academy",
            "address": "15353 Silver Eagle Dr NW, Bena, MN 56626",
            "phone": "218-665-3000",
            "website": "https://www.circleoflifeacademy.org",
            "students": 200
        }
    ],
    "City Academy": [
        {
            "school_name": "City Academy",
            "address": "958 Jessie St, St Paul, MN 55130",
            "phone": "651-298-4624",
            "website": "https://www.cityacademy.org",
            "students": 150
        }
    ],
    "Clarkfield Charter School": [
        {
            "school_name": "Clarkfield Charter School",
            "address": "301 13th St, Clarkfield, MN 56223",
            "phone": "320-669-4655",
            "website": "https://www.clarkfieldcharterschool.org",
            "students": 100
        }
    ],
    "Clearbrook-Gonvick School District": [
        {
            "school_name": "Clearbrook-Gonvick High School",
            "address": "16770 Clearwater Lake Rd, Clearbrook, MN 56634",
            "phone": "218-776-3112",
            "website": "https://www.clearbrook-gonvick.k12.mn.us",
            "students": 300
        },
        {
            "school_name": "Clearbrook-Gonvick Elementary School",
            "address": "16770 Clearwater Lake Rd, Clearbrook, MN 56634",
            "phone": "218-776-3112",
            "website": "https://www.clearbrook-gonvick.k12.mn.us",
            "students": 200
        }
    ],
    "Cleveland Public School District": [
        {
            "school_name": "Cleveland High School",
            "address": "400 6th St, Cleveland, MN 56017",
            "phone": "507-931-5953",
            "website": "https://www.cleveland.k12.mn.us",
            "students": 200
        },
        {
            "school_name": "Cleveland Elementary School",
            "address": "400 6th St, Cleveland, MN 56017",
            "phone": "507-931-5953",
            "website": "https://www.cleveland.k12.mn.us",
            "students": 150
        }
    ],
    "Climax-Shelly Public Schools": [
        {
            "school_name": "Climax-Shelly High School",
            "address": "111 E Broadway, Climax, MN 56523",
            "phone": "218-857-2385",
            "website": "https://www.climax.k12.mn.us",
            "students": 100
        },
        {
            "school_name": "Climax-Shelly Elementary School",
            "address": "111 E Broadway, Climax, MN 56523",
            "phone": "218-857-2385",
            "website": "https://www.climax.k12.mn.us",
            "students": 50
        }
    ],
    "Clinton-Graceville-Beardsley School District": [
        {
            "school_name": "Clinton-Graceville-Beardsley High School",
            "address": "712 3rd St, Clinton, MN 56225",
            "phone": "320-325-5224",
            "website": "https://www.cgb.k12.mn.us",
            "students": 150
        },
        {
            "school_name": "Clinton-Graceville-Beardsley Elementary School",
            "address": "712 3rd St, Clinton, MN 56225",
            "phone": "320-325-5224",
            "website": "https://www.cgb.k12.mn.us",
            "students": 100
        }
    ],
    "Cloquet Public School District": [
        {
            "school_name": "Cloquet High School",
            "address": "1000 18th St, Cloquet, MN 55720",
            "phone": "218-879-3393",
            "website": "https://www.isd94.org",
            "students": 800
        },
        {
            "school_name": "Cloquet Middle School",
            "address": "509 Carlton Ave, Cloquet, MN 55720",
            "phone": "218-879-3328",
            "website": "https://www.isd94.org",
            "students": 600
        },
        {
            "school_name": "Churchill Elementary School",
            "address": "515 Granite St, Cloquet, MN 55720",
            "phone": "218-879-3308",
            "website": "https://www.isd94.org",
            "students": 400
        }
    ],
    "College Preparatory Elementary": [
        {
            "school_name": "College Preparatory Elementary",
            "address": "355 Randolph Ave, St Paul, MN 55102",
            "phone": "651-605-2360",
            "website": "https://www.cpe-k6.org",
            "students": 200
        }
    ],
    "Cologne Academy": [
        {
            "school_name": "Cologne Academy",
            "address": "1221 Village Pkwy, Cologne, MN 55322",
            "phone": "952-466-2276",
            "website": "https://www.cologneacademy.org",
            "students": 400
        }
    ],
    "Columbia Heights Public School Dist.": [
        {
            "school_name": "Columbia Heights High School",
            "address": "1400 49th Ave NE, Columbia Heights, MN 55421",
            "phone": "763-528-4600",
            "website": "https://www.colheights.k12.mn.us",
            "students": 800
        },
        {
            "school_name": "Columbia Heights Middle School",
            "address": "1300 49th Ave NE, Columbia Heights, MN 55421",
            "phone": "763-528-4700",
            "website": "https://www.colheights.k12.mn.us",
            "students": 600
        },
        {
            "school_name": "Highland Elementary School",
            "address": "1500 49th Ave NE, Columbia Heights, MN 55421",
            "phone": "763-528-4400",
            "website": "https://www.colheights.k12.mn.us",
            "students": 400
        }
    ],
    "Comfrey Public School District": [
        {
            "school_name": "Comfrey High School",
            "address": "305 Ochre St W, Comfrey, MN 56019",
            "phone": "507-877-3491",
            "website": "https://www.comfrey.k12.mn.us",
            "students": 100
        },
        {
            "school_name": "Comfrey Elementary School",
            "address": "305 Ochre St W, Comfrey, MN 56019",
            "phone": "507-877-3491",
            "website": "https://www.comfrey.k12.mn.us",
            "students": 50
        }
    ],
    "Community Of Peace Academy": [
        {
            "school_name": "Community Of Peace Academy",
            "address": "471 Magnolia Ave E, St Paul, MN 55130",
            "phone": "651-776-5151",
            "website": "https://www.cpa.charter.k12.mn.us",
            "students": 800
        }
    ],
    "Community School Of Excellence": [
        {
            "school_name": "Community School Of Excellence",
            "address": "270 Larpenteur Ave W, St Paul, MN 55113",
            "phone": "651-917-0073",
            "website": "https://www.csemn.org",
            "students": 1000
        }
    ],
    "Cook County Public Schools": [
        {
            "school_name": "Cook County High School",
            "address": "101 W 5th St, Grand Marais, MN 55604",
            "phone": "218-387-2271",
            "website": "https://www.cookcountyschools.org",
            "students": 200
        },
        {
            "school_name": "Cook County Elementary School",
            "address": "101 W 5th St, Grand Marais, MN 55604",
            "phone": "218-387-2271",
            "website": "https://www.cookcountyschools.org",
            "students": 150
        }
    ],
    "Cornerstone Montessori Elementary": [
        {
            "school_name": "Cornerstone Montessori Elementary",
            "address": "1611 Ames Ave, St Paul, MN 55106",
            "phone": "651-774-5000",
            "website": "https://www.cornerstone-elementary.org",
            "students": 100
        }
    ],
    "Cromwell-Wright Public Schools": [
        {
            "school_name": "Cromwell-Wright High School",
            "address": "5624 Hwy 210, Cromwell, MN 55726",
            "phone": "218-644-3716",
            "website": "https://www.isd95.org",
            "students": 200
        },
        {
            "school_name": "Cromwell-Wright Elementary School",
            "address": "5624 Hwy 210, Cromwell, MN 55726",
            "phone": "218-644-3716",
            "website": "https://www.isd95.org",
            "students": 150
        }
    ],
    "Crookston Public School District": [
        {
            "school_name": "Crookston High School",
            "address": "402 Fisher Ave, Crookston, MN 56716",
            "phone": "218-281-2144",
            "website": "https://www.crookston.k12.mn.us",
            "students": 400
        },
        {
            "school_name": "Highland Elementary School",
            "address": "801 Central Ave N, Crookston, MN 56716",
            "phone": "218-281-5600",
            "website": "https://www.crookston.k12.mn.us",
            "students": 300
        }
    ],
    "Crosby-Ironton Public School Dist.": [
        {
            "school_name": "Crosby-Ironton High School",
            "address": "711 Poplar St, Crosby, MN 56441",
            "phone": "218-545-8800",
            "website": "https://www.ci.k12.mn.us",
            "students": 400
        },
        {
            "school_name": "Crosby-Ironton Elementary School",
            "address": "711 Poplar St, Crosby, MN 56441",
            "phone": "218-545-8800",
            "website": "https://www.ci.k12.mn.us",
            "students": 300
        }
    ],
    "Crosslake Community Charter School": [
        {
            "school_name": "Crosslake Community Charter School",
            "address": "35808 Co Rd 66, Crosslake, MN 56442",
            "phone": "218-692-5437",
            "website": "https://www.crosslakekids.org",
            "students": 200
        }
    ],
    "Crosswinds Arts And Science School": [
        {
            "school_name": "Crosswinds Arts And Science School",
            "address": "600 Weir Dr, Woodbury, MN 55125",
            "phone": "651-379-2600",
            "website": "https://www.crosswindsmn.org",
            "students": 300
        }
    ],
    "Cyber Village Academy": [
        {
            "school_name": "Cyber Village Academy",
            "address": "768 Hamline Ave S, St Paul, MN 55116",
            "phone": "651-523-7170",
            "website": "https://www.cybervillageacademy.org",
            "students": 200
        }
    ],
    "Dassel-Cokato Public School Dist.": [
        {
            "school_name": "Dassel-Cokato High School",
            "address": "4852 Reardon Ave SW, Cokato, MN 55321",
            "phone": "320-286-4100",
            "website": "https://www.dc.k12.mn.us",
            "students": 600
        },
        {
            "school_name": "Dassel-Cokato Middle School",
            "address": "4852 Reardon Ave SW, Cokato, MN 55321",
            "phone": "320-286-4100",
            "website": "https://www.dc.k12.mn.us",
            "students": 500
        },
        {
            "school_name": "Dassel Elementary School",
            "address": "4852 Reardon Ave SW, Cokato, MN 55321",
            "phone": "320-286-4100",
            "website": "https://www.dc.k12.mn.us",
            "students": 400
        }
    ],
    "Davinci Academy": [
        {
            "school_name": "Davinci Academy",
            "address": "532 Bunker Lake Blvd NE, Ham Lake, MN 55304",
            "phone": "763-754-6577",
            "website": "https://www.davincicharterschool.org",
            "students": 800
        }
    ],
    "Dawson-Boyd Public School District": [
        {
            "school_name": "Dawson-Boyd High School",
            "address": "848 Chestnut St, Dawson, MN 56232",
            "phone": "320-769-2955",
            "website": "https://www.dawsonboyd.k12.mn.us",
            "students": 300
        },
        {
            "school_name": "Dawson-Boyd Elementary School",
            "address": "848 Chestnut St, Dawson, MN 56232",
            "phone": "320-769-2955",
            "website": "https://www.dawsonboyd.k12.mn.us",
            "students": 200
        }
    ],
    "Deer River Public School District": [
        {
            "school_name": "Deer River High School",
            "address": "101 1st Ave NE, Deer River, MN 56636",
            "phone": "218-246-2420",
            "website": "https://www.isd317.org",
            "students": 400
        },
        {
            "school_name": "King Elementary School",
            "address": "500 5th St SE, Deer River, MN 56636",
            "phone": "218-246-8860",
            "website": "https://www.isd317.org",
            "students": 300
        }
    ],
    "Delano Public School District": [
        {
            "school_name": "Delano High School",
            "address": "700 Elm Ave E, Delano, MN 55328",
            "phone": "763-972-3365",
            "website": "https://www.delano.k12.mn.us",
            "students": 800
        },
        {
            "school_name": "Delano Middle School",
            "address": "700 Elm Ave E, Delano, MN 55328",
            "phone": "763-972-3365",
            "website": "https://www.delano.k12.mn.us",
            "students": 600
        },
        {
            "school_name": "Delano Elementary School",
            "address": "678 Tiger Dr, Delano, MN 55328",
            "phone": "763-972-6200",
            "website": "https://www.delano.k12.mn.us",
            "students": 500
        }
    ],
    "Detroit Lakes Public School Dist.": [
        {
            "school_name": "Detroit Lakes High School",
            "address": "1301 Roosevelt Ave, Detroit Lakes, MN 56501",
            "phone": "218-847-4491",
            "website": "https://www.dlschools.net",
            "students": 1000
        },
        {
            "school_name": "Detroit Lakes Middle School",
            "address": "510 11th Ave, Detroit Lakes, MN 56501",
            "phone": "218-847-9228",
            "website": "https://www.dlschools.net",
            "students": 800
        },
        {
            "school_name": "Rossman Elementary School",
            "address": "1221 Rossman Ave, Detroit Lakes, MN 56501",
            "phone": "218-847-1106",
            "website": "https://www.dlschools.net",
            "students": 600
        }
    ],
    "Dilworth-Glyndon-Felton School District": [
        {
            "school_name": "Dilworth-Glyndon-Felton High School",
            "address": "513 Parke Ave, Glyndon, MN 56547",
            "phone": "218-477-6800",
            "website": "https://www.dgf.k12.mn.us",
            "students": 600
        },
        {
            "school_name": "Dilworth-Glyndon-Felton Middle School",
            "address": "108 Main St, Dilworth, MN 56529",
            "phone": "218-477-6800",
            "website": "https://www.dgf.k12.mn.us",
            "students": 400
        },
        {
            "school_name": "Dilworth-Glyndon-Felton Elementary School",
            "address": "108 Main St, Dilworth, MN 56529",
            "phone": "218-477-6800",
            "website": "https://www.dgf.k12.mn.us",
            "students": 300
        }
    ],
    "Discovery Charter School": [
        {
            "school_name": "Discovery Charter School",
            "address": "4100 66th St E, Inver Grove Heights, MN 55076",
            "phone": "651-444-8464",
            "website": "https://www.discoverymn.org",
            "students": 200
        }
    ],
    "Discovery Public School Faribault": [
        {
            "school_name": "Discovery Public School of Faribault",
            "address": "126 8th St NW, Faribault, MN 55021",
            "phone": "507-331-5423",
            "website": "https://www.discoverypublicschool.org",
            "students": 100
        }
    ],
    "Discovery Woods Montessori School": [
        {
            "school_name": "Discovery Woods Montessori School",
            "address": "210 NW 2nd Ave, Brainerd, MN 56401",
            "phone": "218-828-8200",
            "website": "https://www.discoverywoods.org",
            "students": 150
        }
    ],
    "Dover-Eyota Public School District": [
        {
            "school_name": "Dover-Eyota High School",
            "address": "615 South Ave SW, Eyota, MN 55934",
            "phone": "507-545-2631",
            "website": "https://www.desch.org",
            "students": 400
        },
        {
            "school_name": "Dover-Eyota Elementary School",
            "address": "615 South Ave SW, Eyota, MN 55934",
            "phone": "507-545-2631",
            "website": "https://www.desch.org",
            "students": 300
        }
    ],
    "Duluth Public School District": [
        {
            "school_name": "Duluth East High School",
            "address": "301 N 40th Ave E, Duluth, MN 55804",
            "phone": "218-336-8845",
            "website": "https://www.isd709.org",
            "students": 1500
        },
        {
            "school_name": "Denfeld High School",
            "address": "401 N 44th Ave W, Duluth, MN 55807",
            "phone": "218-336-8830",
            "website": "https://www.isd709.org",
            "students": 1200
        },
        {
            "school_name": "Lincoln Park Middle School",
            "address": "3215 W 3rd St, Duluth, MN 55806",
            "phone": "218-336-8880",
            "website": "https://www.isd709.org",
            "students": 800
        }
    ],
    "Duluth Public Schools Academy": [
        {
            "school_name": "Duluth Public Schools Academy",
            "address": "3301 Technology Dr, Duluth, MN 55811",
            "phone": "218-728-9556",
            "website": "https://www.duluthedison.org",
            "students": 600
        }
    ],
    "E.C.H.O. Charter School": [
        {
            "school_name": "E.C.H.O. Charter School",
            "address": "101 Rocket Ave, Echo, MN 56237",
            "phone": "507-925-4143",
            "website": "https://www.echo.charter.k12.mn.us",
            "students": 100
        }
    ],
    "Eagle Ridge Academy Charter School": [
        {
            "school_name": "Eagle Ridge Academy",
            "address": "11111 Bren Rd W, Minnetonka, MN 55343",
            "phone": "952-746-7760",
            "website": "https://www.eagleridgeacademy.org",
            "students": 1300
        }
    ],
    "Eagle Valley Public School District": [
        {
            "school_name": "Eagle Valley High School",
            "address": "106 Frank St, Clarissa, MN 56440",
            "phone": "218-756-3631",
            "website": "https://www.evps.k12.mn.us",
            "students": 200
        },
        {
            "school_name": "Eagle Valley Elementary School",
            "address": "106 Frank St, Clarissa, MN 56440",
            "phone": "218-756-3631",
            "website": "https://www.evps.k12.mn.us",
            "students": 150
        }
    ],
    "East Central School District": [
        {
            "school_name": "East Central High School",
            "address": "61085 State Hwy 23, Finlayson, MN 55735",
            "phone": "320-245-2289",
            "website": "https://www.eastcentral.k12.mn.us",
            "students": 300
        },
        {
            "school_name": "East Central Elementary School",
            "address": "61085 State Hwy 23, Finlayson, MN 55735",
            "phone": "320-245-2289",
            "website": "https://www.eastcentral.k12.mn.us",
            "students": 200
        }
    ],
    "East Grand Forks Public School Dist.": [
        {
            "school_name": "East Grand Forks Senior High School",
            "address": "1420 4th Ave NW, East Grand Forks, MN 56721",
            "phone": "218-773-2405",
            "website": "https://www.egf.k12.mn.us",
            "students": 600
        },
        {
            "school_name": "Central Middle School",
            "address": "1827 Bygland Rd SE, East Grand Forks, MN 56721",
            "phone": "218-773-1141",
            "website": "https://www.egf.k12.mn.us",
            "students": 400
        },
        {
            "school_name": "South Point Elementary School",
            "address": "1900 13th St SE, East Grand Forks, MN 56721",
            "phone": "218-773-1141",
            "website": "https://www.egf.k12.mn.us",
            "students": 300
        }
    ],
    "East Range Academy Of Tech-Science": [
        {
            "school_name": "East Range Academy of Technology and Science",
            "address": "2000 Siegel Blvd, Eveleth, MN 55734",
            "phone": "218-744-7965",
            "website": "https://www.erats.org",
            "students": 150
        }
    ],
    "East Range Sec. Technical Center": [
        {
            "school_name": "East Range Secondary Technical Center",
            "address": "4115 Enterprise Dr, Eveleth, MN 55734",
            "phone": "218-744-2211",
            "website": "https://www.erstc.org",
            "students": 100
        }
    ],
    "Eastern Carver County Public School": [
        {
            "school_name": "Chanhassen High School",
            "address": "2200 Lyman Blvd, Chanhassen, MN 55317",
            "phone": "952-556-3500",
            "website": "https://www.district112.org",
            "students": 1500
        },
        {
            "school_name": "Chaska High School",
            "address": "545 Pioneer Trail, Chaska, MN 55318",
            "phone": "952-556-7100",
            "website": "https://www.district112.org",
            "students": 1400
        },
        {
            "school_name": "Pioneer Ridge Middle School",
            "address": "1085 Pioneer Trail, Chaska, MN 55318",
            "phone": "952-556-7800",
            "website": "https://www.district112.org",
            "students": 800
        }
    ],
    "Eden Prairie Public School District": [
        {
            "school_name": "Eden Prairie High School",
            "address": "17185 Valley View Rd, Eden Prairie, MN 55346",
            "phone": "952-975-8000",
            "website": "https://www.edenpr.org",
            "students": 3000
        },
        {
            "school_name": "Central Middle School",
            "address": "8025 School Rd, Eden Prairie, MN 55344",
            "phone": "952-975-7300",
            "website": "https://www.edenpr.org",
            "students": 1200
        },
        {
            "school_name": "Oak Point Elementary School",
            "address": "13400 Staring Lake Pkwy, Eden Prairie, MN 55347",
            "phone": "952-975-7600",
            "website": "https://www.edenpr.org",
            "students": 800
        }
    ],
    "Eden Valley-Watkins School District": [
        {
            "school_name": "Eden Valley-Watkins High School",
            "address": "298 Brooks St N, Eden Valley, MN 55329",
            "phone": "320-453-2900",
            "website": "https://www.evw.k12.mn.us",
            "students": 400
        },
        {
            "school_name": "Eden Valley-Watkins Elementary School",
            "address": "298 Brooks St N, Eden Valley, MN 55329",
            "phone": "320-453-2900",
            "website": "https://www.evw.k12.mn.us",
            "students": 300
        }
    ],
    "Edgerton Public School District": [
        {
            "school_name": "Edgerton High School",
            "address": "423 1st Ave W, Edgerton, MN 56128",
            "phone": "507-442-7881",
            "website": "https://www.edgertonpublic.com",
            "students": 200
        },
        {
            "school_name": "Edgerton Elementary School",
            "address": "423 1st Ave W, Edgerton, MN 56128",
            "phone": "507-442-7881",
            "website": "https://www.edgertonpublic.com",
            "students": 150
        }
    ],
    "Edina Public School District": [
        {
            "school_name": "Edina High School",
            "address": "6754 Valley View Rd, Edina, MN 55439",
            "phone": "952-848-3800",
            "website": "https://www.edinaschools.org",
            "students": 2700
        },
        {
            "school_name": "South View Middle School",
            "address": "4725 South View Ln, Edina, MN 55424",
            "phone": "952-848-3700",
            "website": "https://www.edinaschools.org",
            "students": 1200
        },
        {
            "school_name": "Concord Elementary School",
            "address": "5900 Concord Ave S, Edina, MN 55424",
            "phone": "952-848-4300",
            "website": "https://www.edinaschools.org",
            "students": 600
        }
    ],
    "Edvisions Off Campus School": [
        {
            "school_name": "Edvisions Off Campus School",
            "address": "501 Main St, Henderson, MN 56044",
            "phone": "507-248-3101",
            "website": "https://www.edvisionshighschool.com",
            "students": 100
        }
    ],
    "El Colegio Charter School": [
        {
            "school_name": "El Colegio Charter School",
            "address": "4137 Bloomington Ave, Minneapolis, MN 55407",
            "phone": "612-728-5728",
            "website": "https://www.el-colegio.org",
            "students": 150
        }
    ],
    "Elk River School District": [
        {
            "school_name": "Elk River High School",
            "address": "900 School St NW, Elk River, MN 55330",
            "phone": "763-241-3434",
            "website": "https://www.isd728.org",
            "students": 1600
        },
        {
            "school_name": "Salk Middle School",
            "address": "11970 Highland Rd, Elk River, MN 55330",
            "phone": "763-241-3455",
            "website": "https://www.isd728.org",
            "students": 800
        },
        {
            "school_name": "Parker Elementary School",
            "address": "500 School St NW, Elk River, MN 55330",
            "phone": "763-241-3490",
            "website": "https://www.isd728.org",
            "students": 600
        }
    ],
    "Ellsworth Public School District": [
        {
            "school_name": "Ellsworth High School",
            "address": "513 S Broadway St, Ellsworth, MN 56129",
            "phone": "507-967-2242",
            "website": "https://www.ellsworth.k12.mn.us",
            "students": 100
        },
        {
            "school_name": "Ellsworth Elementary School",
            "address": "513 S Broadway St, Ellsworth, MN 56129",
            "phone": "507-967-2242",
            "website": "https://www.ellsworth.k12.mn.us",
            "students": 50
        }
    ],
    "Ely Public School District": [
        {
            "school_name": "Ely Memorial High School",
            "address": "600 E Harvey St, Ely, MN 55731",
            "phone": "218-365-6166",
            "website": "https://www.ely.k12.mn.us",
            "students": 200
        },
        {
            "school_name": "Washington Elementary School",
            "address": "600 E Harvey St, Ely, MN 55731",
            "phone": "218-365-6166",
            "website": "https://www.ely.k12.mn.us",
            "students": 150
        }
    ],
    "Esko Public School District": [
        {
            "school_name": "Esko High School",
            "address": "2 E Hwy 61, Esko, MN 55733",
            "phone": "218-879-4673",
            "website": "https://www.esko.k12.mn.us",
            "students": 400
        },
        {
            "school_name": "Winterquist Elementary School",
            "address": "2 E Hwy 61, Esko, MN 55733",
            "phone": "218-879-3361",
            "website": "https://www.esko.k12.mn.us",
            "students": 300
        }
    ],
    "Eveleth-Gilbert School District": [
        {
            "school_name": "Eveleth-Gilbert High School",
            "address": "801 Jones St, Eveleth, MN 55734",
            "phone": "218-744-7706",
            "website": "https://www.evelethgilbert.k12.mn.us",
            "students": 500
        },
        {
            "school_name": "Franklin Elementary School",
            "address": "801 Jones St, Eveleth, MN 55734",
            "phone": "218-744-7706",
            "website": "https://www.evelethgilbert.k12.mn.us",
            "students": 300
        }
    ],
    "Excell Academy Charter": [
        {
            "school_name": "Excell Academy for Higher Learning",
            "address": "6510 Zane Ave N, Brooklyn Park, MN 55429",
            "phone": "763-533-0500",
            "website": "https://www.excellacademy.dreamhosters.com",
            "students": 400
        }
    ],
    "Face To Face Academy": [
        {
            "school_name": "Face To Face Academy",
            "address": "1165 Arcade St, St Paul, MN 55106",
            "phone": "651-772-5555",
            "website": "https://www.f2facademy.org",
            "students": 100
        }
    ],
    "Fairmont Area School District": [
        {
            "school_name": "Fairmont High School",
            "address": "900 Johnson St, Fairmont, MN 56031",
            "phone": "507-238-4411",
            "website": "https://www.fairmont.k12.mn.us",
            "students": 600
        },
        {
            "school_name": "Fairmont Elementary School",
            "address": "714 Victoria St, Fairmont, MN 56031",
            "phone": "507-238-4487",
            "website": "https://www.fairmont.k12.mn.us",
            "students": 500
        }
    ],
    "Family Freedom Academy": [
        {
            "school_name": "Family Freedom Academy",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        }
    ],
    "Faribault Public School District": [
        {
            "school_name": "Faribault High School",
            "address": "330 9th Ave SW, Faribault, MN 55021",
            "phone": "507-333-6100",
            "website": "https://www.faribault.k12.mn.us",
            "students": 1200
        },
        {
            "school_name": "Faribault Middle School",
            "address": "704 17th St SW, Faribault, MN 55021",
            "phone": "507-333-6300",
            "website": "https://www.faribault.k12.mn.us",
            "students": 800
        },
        {
            "school_name": "Jefferson Elementary School",
            "address": "922 Home Pl, Faribault, MN 55021",
            "phone": "507-333-6500",
            "website": "https://www.faribault.k12.mn.us",
            "students": 600
        }
    ],
    "Farmington Public School District": [
        {
            "school_name": "Farmington High School",
            "address": "20655 Flagstaff Ave, Farmington, MN 55024",
            "phone": "651-252-2500",
            "website": "https://www.farmington.k12.mn.us",
            "students": 2000
        },
        {
            "school_name": "Boeckman Middle School",
            "address": "800 Denmark Ave, Farmington, MN 55024",
            "phone": "651-252-2600",
            "website": "https://www.farmington.k12.mn.us",
            "students": 1000
        },
        {
            "school_name": "Akin Road Elementary School",
            "address": "5231 195th St W, Farmington, MN 55024",
            "phone": "651-463-9000",
            "website": "https://www.farmington.k12.mn.us",
            "students": 600
        }
    ],
    "Fergus Falls Area Special Education Cooperative": [
        {
            "school_name": "Fergus Falls Area Special Education Cooperative",
            "address": "518 Friberg Ave, Fergus Falls, MN 56537",
            "phone": "218-998-0544",
            "website": "https://www.fergusotter.org",
            "students": "N/A"
        }
    ],
    "Fergus Falls Public School District": [
        {
            "school_name": "Fergus Falls High School",
            "address": "601 Randolph Ave, Fergus Falls, MN 56537",
            "phone": "218-998-0544",
            "website": "https://www.fergusotter.org",
            "students": 800
        },
        {
            "school_name": "Kennedy Secondary School",
            "address": "601 Randolph Ave, Fergus Falls, MN 56537",
            "phone": "218-998-0544",
            "website": "https://www.fergusotter.org",
            "students": 600
        },
        {
            "school_name": "McKinley Elementary School",
            "address": "724 W Laurel St, Fergus Falls, MN 56537",
            "phone": "218-998-0544",
            "website": "https://www.fergusotter.org",
            "students": 400
        }
    ],
    "Fertile-Beltrami School District": [
        {
            "school_name": "Fertile-Beltrami High School",
            "address": "210 S Mill St, Fertile, MN 56540",
            "phone": "218-945-6933",
            "website": "https://www.fertilebeltrami.k12.mn.us",
            "students": 200
        },
        {
            "school_name": "Fertile-Beltrami Elementary School",
            "address": "210 S Mill St, Fertile, MN 56540",
            "phone": "218-945-6933",
            "website": "https://www.fertilebeltrami.k12.mn.us",
            "students": 150
        }
    ],
    "Fillmore Central School District": [
        {
            "school_name": "Fillmore Central High School",
            "address": "145 Main Ave S, Harmony, MN 55939",
            "phone": "507-886-6464",
            "website": "https://www.fillmorecentral.k12.mn.us",
            "students": 200
        },
        {
            "school_name": "Fillmore Central Elementary School",
            "address": "702 Chatfield St, Preston, MN 55965",
            "phone": "507-765-3809",
            "website": "https://www.fillmorecentral.k12.mn.us",
            "students": 150
        }
    ],
    "Fisher Public School District": [
        {
            "school_name": "Fisher High School",
            "address": "313 Park Ave, Fisher, MN 56723",
            "phone": "218-891-4105",
            "website": "https://www.fisher.k12.mn.us",
            "students": 100
        },
        {
            "school_name": "Fisher Elementary School",
            "address": "313 Park Ave, Fisher, MN 56723",
            "phone": "218-891-4105",
            "website": "https://www.fisher.k12.mn.us",
            "students": 50
        }
    ],
    "Fit Academy": [
        {
            "school_name": "Fit Academy",
            "address": "7200 147th St W, Apple Valley, MN 55124",
            "phone": "952-683-9018",
            "website": "https://www.fitacademymn.org",
            "students": 200
        }
    ],
    "Flex Academy": [
        {
            "school_name": "Flex Academy",
            "address": "100 W 66th St, Richfield, MN 55423",
            "phone": "612-787-4100",
            "website": "https://www.flexacademymn.org",
            "students": 150
        }
    ],
    "Floodwood Public School District": [
        {
            "school_name": "Floodwood High School",
            "address": "115 W 4th Ave, Floodwood, MN 55736",
            "phone": "218-476-2285",
            "website": "https://www.floodwood.k12.mn.us",
            "students": 100
        },
        {
            "school_name": "Floodwood Elementary School",
            "address": "115 W 4th Ave, Floodwood, MN 55736",
            "phone": "218-476-2285",
            "website": "https://www.floodwood.k12.mn.us",
            "students": 50
        }
    ],
    "Foley Public School District": [
        {
            "school_name": "Foley High School",
            "address": "621 Penn St, Foley, MN 56329",
            "phone": "320-968-7246",
            "website": "https://www.foley.k12.mn.us",
            "students": 400
        },
        {
            "school_name": "Foley Intermediate School",
            "address": "621 Penn St, Foley, MN 56329",
            "phone": "320-968-7246",
            "website": "https://www.foley.k12.mn.us",
            "students": 300
        },
        {
            "school_name": "Foley Elementary School",
            "address": "621 Penn St, Foley, MN 56329",
            "phone": "320-968-7246",
            "website": "https://www.foley.k12.mn.us",
            "students": 200
        }
    ],
    "Fond Du Lac Ojibwe School": [
        {
            "school_name": "Fond Du Lac Ojibwe School",
            "address": "49 University Rd, Cloquet, MN 55720",
            "phone": "218-878-7242",
            "website": "https://www.fdlrezk12.com",
            "students": 300
        }
    ],
    "Forest Lake Public School District": [
        {
            "school_name": "Forest Lake Area High School",
            "address": "6101 Scandia Trail N, Forest Lake, MN 55025",
            "phone": "651-982-8400",
            "website": "https://www.flaschools.org",
            "students": 2000
        },
        {
            "school_name": "Century Junior High School",
            "address": "21395 Goodview Ave N, Forest Lake, MN 55025",
            "phone": "651-982-3100",
            "website": "https://www.flaschools.org",
            "students": 800
        },
        {
            "school_name": "Forest View Elementary School",
            "address": "620 SW 4th St, Forest Lake, MN 55025",
            "phone": "651-982-8200",
            "website": "https://www.flaschools.org",
            "students": 600
        }
    ],
    "Fosston Public School District": [
        {
            "school_name": "Fosston High School",
            "address": "301 1st St E, Fosston, MN 56542",
            "phone": "218-435-1909",
            "website": "https://www.fosston.k12.mn.us",
            "students": 200
        },
        {
            "school_name": "Magelssen Elementary School",
            "address": "700 1st St E, Fosston, MN 56542",
            "phone": "218-435-1909",
            "website": "https://www.fosston.k12.mn.us",
            "students": 150
        }
    ],
    "Fraser Academy": [
        {
            "school_name": "Fraser Academy",
            "address": "1534 6th St NE, Minneapolis, MN 55413",
            "phone": "612-465-8600",
            "website": "https://www.fraser.org",
            "students": 100
        }
    ],
    "Frazee-Vergas Public School Dist.": [
        {
            "school_name": "Frazee High School",
            "address": "305 N Lake St, Frazee, MN 56544",
            "phone": "218-334-3181",
            "website": "https://www.frazee.k12.mn.us",
            "students": 300
        },
        {
            "school_name": "Frazee Elementary School",
            "address": "305 N Lake St, Frazee, MN 56544",
            "phone": "218-334-3181",
            "website": "https://www.frazee.k12.mn.us",
            "students": 200
        }
    ],
    "Freedom Academy Charter School": [
        {
            "school_name": "Freedom Academy Charter School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        }
    ],
    "Freshwater Education District": [
        {
            "school_name": "Freshwater Education District",
            "address": "2222 Industrial Dr, Wadena, MN 56482",
            "phone": "218-631-3505",
            "website": "https://www.fed.k12.mn.us",
            "students": "N/A"
        }
    ],
    "Fridley Public School District": [
        {
            "school_name": "Fridley High School",
            "address": "6000 W Moore Lake Dr, Fridley, MN 55432",
            "phone": "763-502-5600",
            "website": "https://www.fridley.k12.mn.us",
            "students": 800
        },
        {
            "school_name": "Fridley Middle School",
            "address": "6100 W Moore Lake Dr, Fridley, MN 55432",
            "phone": "763-502-5400",
            "website": "https://www.fridley.k12.mn.us",
            "students": 600
        },
        {
            "school_name": "Stevenson Elementary School",
            "address": "6080 E River Rd, Fridley, MN 55432",
            "phone": "763-502-5300",
            "website": "https://www.fridley.k12.mn.us",
            "students": 400
        }
    ],
    "Friendship Academy Of Fine Arts Chtr.": [
        {
            "school_name": "Friendship Academy of Fine Arts Charter School",
            "address": "2600 E 38th St, Minneapolis, MN 55406",
            "phone": "612-879-6703",
            "website": "https://www.friendshipacademy.org",
            "students": 200
        }
    ],
    "Fulda Public School District": [
        {
            "school_name": "Fulda High School",
            "address": "410 N College Ave, Fulda, MN 56131",
            "phone": "507-425-2514",
            "website": "https://www.fps.mntm.org",
            "students": 200
        },
        {
            "school_name": "Fulda Elementary School",
            "address": "410 N College Ave, Fulda, MN 56131",
            "phone": "507-425-2514",
            "website": "https://www.fps.mntm.org",
            "students": 150
        }
    ],
    "G.F.W. School District": [
        {
            "school_name": "G.F.W. High School",
            "address": "1001 N Cottonwood St, Winthrop, MN 55396",
            "phone": "507-647-5382",
            "website": "https://www.gfw.k12.mn.us",
            "students": 200
        },
        {
            "school_name": "G.F.W. Elementary School",
            "address": "1001 N Cottonwood St, Winthrop, MN 55396",
            "phone": "507-647-5382",
            "website": "https://www.gfw.k12.mn.us",
            "students": 150
        }
    ],
    "Gateway STEM Academy": [
        {
            "school_name": "Gateway STEM Academy",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        }
    ],
    "Glacial Hills Elementary": [
        {
            "school_name": "Glacial Hills Elementary",
            "address": "33 11th Ave SE, Starbuck, MN 56381",
            "phone": "320-239-4820",
            "website": "https://www.glacialhills.org",
            "students": 100
        }
    ],
    "Glencoe-Silver Lake School District": [
        {
            "school_name": "Glencoe-Silver Lake High School",
            "address": "1825 16th St E, Glencoe, MN 55336",
            "phone": "320-864-2400",
            "website": "https://www.gsl.k12.mn.us",
            "students": 600
        },
        {
            "school_name": "Lincoln Elementary School",
            "address": "1621 16th St E, Glencoe, MN 55336",
            "phone": "320-864-2400",
            "website": "https://www.gsl.k12.mn.us",
            "students": 400
        }
    ],
    "Glenville-Emmons School District": [
        {
            "school_name": "Glenville-Emmons High School",
            "address": "230 5th St SE, Glenville, MN 56036",
            "phone": "507-448-2889",
            "website": "https://www.glenville-emmons.k12.mn.us",
            "students": 200
        },
        {
            "school_name": "Glenville-Emmons Elementary School",
            "address": "230 5th St SE, Glenville, MN 56036",
            "phone": "507-448-2889",
            "website": "https://www.glenville-emmons.k12.mn.us",
            "students": 150
        }
    ],
    "Global Academy": [
        {
            "school_name": "Global Academy",
            "address": "4065 Central Ave NE, Columbia Heights, MN 55421",
            "phone": "763-404-8200",
            "website": "https://www.globalacademy.us",
            "students": 400
        }
    ],
    "Goodhue County Education District": [
        {
            "school_name": "Goodhue County Education District",
            "address": "395 Guernsey Ln, Red Wing, MN 55066",
            "phone": "651-388-4441",
            "website": "https://www.gced.k12.mn.us",
            "students": "N/A"
        }
    ],
    "Goodhue Public School District": [
        {
            "school_name": "Goodhue High School",
            "address": "510 3rd Ave, Goodhue, MN 55027",
            "phone": "651-923-4447",
            "website": "https://www.goodhue.k12.mn.us",
            "students": 300
        },
        {
            "school_name": "Goodhue Elementary School",
            "address": "510 3rd Ave, Goodhue, MN 55027",
            "phone": "651-923-4447",
            "website": "https://www.goodhue.k12.mn.us",
            "students": 200
        }
    ],
    "Goodridge Public School District": [
        {
            "school_name": "Goodridge High School",
            "address": "201 Osmund Ave, Goodridge, MN 56725",
            "phone": "218-378-4134",
            "website": "https://www.goodridge.k12.mn.us",
            "students": 100
        },
        {
            "school_name": "Goodridge Elementary School",
            "address": "201 Osmund Ave, Goodridge, MN 56725",
            "phone": "218-378-4134",
            "website": "https://www.goodridge.k12.mn.us",
            "students": 50
        }
    ],
    "Granada Huntley-East Chain School District": [
        {
            "school_name": "Granada Huntley-East Chain High School",
            "address": "300 Reynolds St, Granada, MN 56039",
            "phone": "507-447-2211",
            "website": "https://www.ghs.k12.mn.us",
            "students": 150
        },
        {
            "school_name": "Granada Huntley-East Chain Elementary School",
            "address": "300 Reynolds St, Granada, MN 56039",
            "phone": "507-447-2211",
            "website": "https://www.ghs.k12.mn.us",
            "students": 100
        }
    ],
    "Grand Meadow Public School District": [
        {
            "school_name": "Grand Meadow High School",
            "address": "710 4th Ave NE, Grand Meadow, MN 55936",
            "phone": "507-754-5318",
            "website": "https://www.gm.k12.mn.us",
            "students": 200
        },
        {
            "school_name": "Grand Meadow Elementary School",
            "address": "710 4th Ave NE, Grand Meadow, MN 55936",
            "phone": "507-754-5318",
            "website": "https://www.gm.k12.mn.us",
            "students": 150
        }
    ],
    "Grand Rapids Public School District": [
        {
            "school_name": "Grand Rapids High School",
            "address": "800 Conifer Dr, Grand Rapids, MN 55744",
            "phone": "218-327-5760",
            "website": "https://www.isd318.org",
            "students": 1200
        },
        {
            "school_name": "Robert J. Elkington Middle School",
            "address": "1000 NE 8th Ave, Grand Rapids, MN 55744",
            "phone": "218-327-5800",
            "website": "https://www.isd318.org",
            "students": 800
        },
        {
            "school_name": "Forest Lake Elementary School",
            "address": "715 NW 7th Ave, Grand Rapids, MN 55744",
            "phone": "218-327-5850",
            "website": "https://www.isd318.org",
            "students": 600
        }
    ],
    "Great Expectations": [
        {
            "school_name": "Great Expectations School",
            "address": "550 Hat Trick Ave, Grand Marais, MN 55604",
            "phone": "218-387-9322",
            "website": "https://www.greatexpectationsschool.com",
            "students": 100
        }
    ],
    "Great Oaks Academy Charter School": [
        {
            "school_name": "Great Oaks Academy",
            "address": "5300 France Ave S, Edina, MN 55410",
            "phone": "952-856-2531",
            "website": "https://www.greatoaksacademymn.org",
            "students": 200
        }
    ],
    "Great River School": [
        {
            "school_name": "Great River School",
            "address": "1326 Energy Park Dr, St Paul, MN 55108",
            "phone": "651-305-2780",
            "website": "https://www.greatriverschool.org",
            "students": 400
        }
    ],
    "Green Isle Community School": [
        {
            "school_name": "Green Isle Community School",
            "address": "190 McGrann St, Green Isle, MN 55338",
            "phone": "507-326-7144",
            "website": "https://www.greenislecommunityschool.org",
            "students": 100
        }
    ],
    "Greenbush-Middle River School Dist.": [
        {
            "school_name": "Greenbush-Middle River High School",
            "address": "401 Park Ave W, Greenbush, MN 56726",
            "phone": "218-782-2232",
            "website": "https://www.gmr.k12.mn.us",
            "students": 150
        },
        {
            "school_name": "Greenbush-Middle River Elementary School",
            "address": "401 Park Ave W, Greenbush, MN 56726",
            "phone": "218-782-2232",
            "website": "https://www.gmr.k12.mn.us",
            "students": 100
        }
    ],
    "Greenway Public School District": [
        {
            "school_name": "Greenway High School",
            "address": "308 Roosevelt Ave, Coleraine, MN 55722",
            "phone": "218-245-1280",
            "website": "https://www.isd316.org",
            "students": 300
        },
        {
            "school_name": "Vandyke Elementary School",
            "address": "300 Cole Ave, Coleraine, MN 55722",
            "phone": "218-245-1280",
            "website": "https://www.isd316.org",
            "students": 200
        }
    ],
    "Grygla Public School District": [
        {
            "school_name": "Grygla High School",
            "address": "114 N Fladeland Ave, Grygla, MN 56727",
            "phone": "218-294-6155",
            "website": "https://www.grygla.k12.mn.us",
            "students": 100
        },
        {
            "school_name": "Grygla Elementary School",
            "address": "114 N Fladeland Ave, Grygla, MN 56727",
            "phone": "218-294-6155",
            "website": "https://www.grygla.k12.mn.us",
            "students": 50
        }
    ],
    "Hancock Public School District": [
        {
            "school_name": "Hancock High School",
            "address": "371 Hancock Ave, Hancock, MN 56244",
            "phone": "320-392-5621",
            "website": "https://www.hancock.k12.mn.us",
            "students": 150
        },
        {
            "school_name": "Hancock Elementary School",
            "address": "371 Hancock Ave, Hancock, MN 56244",
            "phone": "320-392-5621",
            "website": "https://www.hancock.k12.mn.us",
            "students": 100
        }
    ],
    "Harbor City International Charter": [
        {
            "school_name": "Harbor City International School",
            "address": "332 W Michigan St, Duluth, MN 55802",
            "phone": "218-722-7574",
            "website": "https://www.harborcityschool.org",
            "students": 200
        }
    ],
    "Harvest Prep School-Seed Academy": [
        {
            "school_name": "Harvest Preparatory School",
            "address": "1300 Olson Memorial Hwy, Minneapolis, MN 55411",
            "phone": "612-876-4105",
            "website": "https://www.seed-harvest.org",
            "students": 400
        }
    ],
    "Hastings Public School District": [
        {
            "school_name": "Hastings High School",
            "address": "200 General Sieben Dr, Hastings, MN 55033",
            "phone": "651-480-7470",
            "website": "https://www.hastings.k12.mn.us",
            "students": 1500
        },
        {
            "school_name": "Hastings Middle School",
            "address": "1000 11th St W, Hastings, MN 55033",
            "phone": "651-480-7060",
            "website": "https://www.hastings.k12.mn.us",
            "students": 1000
        },
        {
            "school_name": "Pinecrest Elementary School",
            "address": "975 W 12th St, Hastings, MN 55033",
            "phone": "651-480-7280",
            "website": "https://www.hastings.k12.mn.us",
            "students": 600
        }
    ],
    "Hawley Public School District": [
        {
            "school_name": "Hawley High School",
            "address": "714 Joseph St, Hawley, MN 56549",
            "phone": "218-483-3555",
            "website": "https://www.hawley.k12.mn.us",
            "students": 300
        },
        {
            "school_name": "Hawley Elementary School",
            "address": "714 Joseph St, Hawley, MN 56549",
            "phone": "218-483-3555",
            "website": "https://www.hawley.k12.mn.us",
            "students": 200
        }
    ],
    "Hayfield Public School District": [
        {
            "school_name": "Hayfield High School",
            "address": "9 6th Ave SE, Hayfield, MN 55940",
            "phone": "507-477-3235",
            "website": "https://www.hayfield.k12.mn.us",
            "students": 300
        },
        {
            "school_name": "Hayfield Elementary School",
            "address": "9 6th Ave SE, Hayfield, MN 55940",
            "phone": "507-477-3235",
            "website": "https://www.hayfield.k12.mn.us",
            "students": 200
        }
    ],
    "Hendricks Public School District": [
        {
            "school_name": "Hendricks High School",
            "address": "200 E Lincoln St, Hendricks, MN 56136",
            "phone": "507-275-3115",
            "website": "https://www.hendricks.k12.mn.us",
            "students": 100
        },
        {
            "school_name": "Hendricks Elementary School",
            "address": "200 E Lincoln St, Hendricks, MN 56136",
            "phone": "507-275-3115",
            "website": "https://www.hendricks.k12.mn.us",
            "students": 50
        }
    ],
    "Hennepin Elementary School": [
        {
            "school_name": "Hennepin Elementary School",
            "address": "2123 Clinton Ave S, Minneapolis, MN 55404",
            "phone": "612-843-5050",
            "website": "https://www.hennepinelementaryschool.org",
            "students": 300
        }
    ],
    "Henning Public School District": [
        {
            "school_name": "Henning High School",
            "address": "500 School Ave, Henning, MN 56551",
            "phone": "218-583-2927",
            "website": "https://www.henning.k12.mn.us",
            "students": 200
        },
        {
            "school_name": "Henning Elementary School",
            "address": "500 School Ave, Henning, MN 56551",
            "phone": "218-583-2927",
            "website": "https://www.henning.k12.mn.us",
            "students": 150
        }
    ],
    "Herman-Norcross School District": [
        {
            "school_name": "Herman-Norcross High School",
            "address": "504 E 5th St, Herman, MN 56248",
            "phone": "320-677-2291",
            "website": "https://www.herman.k12.mn.us",
            "students": 100
        },
        {
            "school_name": "Herman-Norcross Elementary School",
            "address": "504 E 5th St, Herman, MN 56248",
            "phone": "320-677-2291",
            "website": "https://www.herman.k12.mn.us",
            "students": 50
        }
    ],
    "Hermantown Public School District": [
        {
            "school_name": "Hermantown High School",
            "address": "4335 Hawk Cir Dr, Hermantown, MN 55811",
            "phone": "218-729-8874",
            "website": "https://www.hermantown.k12.mn.us",
            "students": 800
        },
        {
            "school_name": "Hermantown Middle School",
            "address": "4335 Hawk Cir Dr, Hermantown, MN 55811",
            "phone": "218-729-8874",
            "website": "https://www.hermantown.k12.mn.us",
            "students": 600
        },
        {
            "school_name": "Hermantown Elementary School",
            "address": "4335 Hawk Cir Dr, Hermantown, MN 55811",
            "phone": "218-729-8874",
            "website": "https://www.hermantown.k12.mn.us",
            "students": 400
        }
    ],
    "Heron Lake-Okabena School District": [
        {
            "school_name": "Heron Lake-Okabena High School",
            "address": "124 N Minnesota Ave, Okabena, MN 56161",
            "phone": "507-853-4507",
            "website": "https://www.hlo.k12.mn.us",
            "students": 150
        },
        {
            "school_name": "Heron Lake-Okabena Elementary School",
            "address": "124 N Minnesota Ave, Okabena, MN 56161",
            "phone": "507-853-4507",
            "website": "https://www.hlo.k12.mn.us",
            "students": 100
        }
    ],
    "Hiawatha Academies": [
        {
            "school_name": "Hiawatha Collegiate High School",
            "address": "3500 E 28th St, Minneapolis, MN 55406",
            "phone": "612-455-4004",
            "website": "https://www.hiawathaacademies.org",
            "students": 400
        },
        {
            "school_name": "Hiawatha College Prep - Kingfield",
            "address": "3800 Pleasant Ave, Minneapolis, MN 55409",
            "phone": "612-455-4004",
            "website": "https://www.hiawathaacademies.org",
            "students": 300
        }
    ],
    "Hiawatha Valley Ed. District": [
        {
            "school_name": "Hiawatha Valley Education District",
            "address": "1410 Bundy Blvd, Winona, MN 55987",
            "phone": "507-452-1200",
            "website": "https://www.hved.org",
            "students": "N/A"
        }
    ],
    "Hibbing Public School District": [
        {
            "school_name": "Hibbing High School",
            "address": "800 E 21st St, Hibbing, MN 55746",
            "phone": "218-208-0840",
            "website": "https://www.hibbing.k12.mn.us",
            "students": 1000
        },
        {
            "school_name": "Washington Elementary School",
            "address": "800 E 21st St, Hibbing, MN 55746",
            "phone": "218-208-0840",
            "website": "https://www.hibbing.k12.mn.us",
            "students": 600
        }
    ],
    "High School For Recording Arts": [
        {
            "school_name": "High School For Recording Arts",
            "address": "1166 University Ave W, St Paul, MN 55104",
            "phone": "651-287-0890",
            "website": "https://www.hsra.org",
            "students": 200
        }
    ],
    "Higher Ground Academy": [
        {
            "school_name": "Higher Ground Academy",
            "address": "1381 Marshall Ave, St Paul, MN 55104",
            "phone": "651-645-1000",
            "website": "https://www.hgacademy.org",
            "students": 800
        }
    ],
    "Hill City Public School District": [
        {
            "school_name": "Hill City High School",
            "address": "500 Ione Ave, Hill City, MN 55748",
            "phone": "218-697-2394",
            "website": "https://www.hillcity.k12.mn.us",
            "students": 200
        },
        {
            "school_name": "Hill City Elementary School",
            "address": "500 Ione Ave, Hill City, MN 55748",
            "phone": "218-697-2394",
            "website": "https://www.hillcity.k12.mn.us",
            "students": 150
        }
    ],
    "Hills-Beaver Creek School District": [
        {
            "school_name": "Hills-Beaver Creek High School",
            "address": "301 N Summit Ave, Hills, MN 56138",
            "phone": "507-962-3240",
            "website": "https://www.hbcpatriots.com",
            "students": 200
        },
        {
            "school_name": "Hills-Beaver Creek Elementary School",
            "address": "301 N Summit Ave, Hills, MN 56138",
            "phone": "507-962-3240",
            "website": "https://www.hbcpatriots.com",
            "students": 150
        }
    ],
    "Hinckley-Finlayson School District": [
        {
            "school_name": "Hinckley-Finlayson High School",
            "address": "201 Main St E, Hinckley, MN 55037",
            "phone": "320-384-6132",
            "website": "https://www.hf.k12.mn.us",
            "students": 300
        },
        {
            "school_name": "Hinckley-Finlayson Elementary School",
            "address": "201 Main St E, Hinckley, MN 55037",
            "phone": "320-384-6132",
            "website": "https://www.hf.k12.mn.us",
            "students": 200
        }
    ],
    "Hmong College Prep Academy": [
        {
            "school_name": "Hmong College Prep Academy",
            "address": "1515 Brewster St, St Paul, MN 55108",
            "phone": "651-209-8002",
            "website": "https://www.hcpak12.org",
            "students": 1200
        }
    ],
    "Holdingford Public School District": [
        {
            "school_name": "Holdingford High School",
            "address": "900 5th St, Holdingford, MN 56340",
            "phone": "320-746-2221",
            "website": "https://www.isd738.org",
            "students": 400
        },
        {
            "school_name": "Holdingford Elementary School",
            "address": "900 5th St, Holdingford, MN 56340",
            "phone": "320-746-2221",
            "website": "https://www.isd738.org",
            "students": 300
        }
    ],
    "Hope Community Academy": [
        {
            "school_name": "Hope Community Academy",
            "address": "720 Payne Ave, St Paul, MN 55130",
            "phone": "651-796-4500",
            "website": "https://www.hope-communityacademy.org",
            "students": 400
        }
    ],
    "Hopkins Public School District": [
        {
            "school_name": "Hopkins High School",
            "address": "2400 Lindbergh Dr, Minnetonka, MN 55305",
            "phone": "952-988-4500",
            "website": "https://www.hopkinsschools.org",
            "students": 1700
        },
        {
            "school_name": "Hopkins West Junior High School",
            "address": "3830 Baker Rd, Minnetonka, MN 55305",
            "phone": "952-988-4400",
            "website": "https://www.hopkinsschools.org",
            "students": 800
        },
        {
            "school_name": "Alice Smith Elementary School",
            "address": "801 Minnetonka Mills Rd, Hopkins, MN 55343",
            "phone": "952-988-4200",
            "website": "https://www.hopkinsschools.org",
            "students": 500
        }
    ],
    "Horizon Science Academy Twin Cities": [
        {
            "school_name": "Horizon Science Academy Twin Cities",
            "address": "930 Geranium Ave E, St Paul, MN 55106",
            "phone": "651-917-0073",
            "website": "https://www.horizontwincities.org",
            "students": 300
        }
    ],
    "Houston Public School District": [
        {
            "school_name": "Houston High School",
            "address": "306 W Elm St, Houston, MN 55943",
            "phone": "507-896-5323",
            "website": "https://www.houston.k12.mn.us",
            "students": 200
        },
        {
            "school_name": "Houston Elementary School",
            "address": "306 W Elm St, Houston, MN 55943",
            "phone": "507-896-5323",
            "website": "https://www.houston.k12.mn.us",
            "students": 150
        }
    ],
    "Howard Lake-Waverly-Winsted School District": [
        {
            "school_name": "Howard Lake-Waverly-Winsted High School",
            "address": "8700 County Rd 6 SW, Howard Lake, MN 55349",
            "phone": "320-543-4600",
            "website": "https://www.hlww.k12.mn.us",
            "students": 400
        },
        {
            "school_name": "Howard Lake-Waverly-Winsted Middle School",
            "address": "8700 County Rd 6 SW, Howard Lake, MN 55349",
            "phone": "320-543-4600",
            "website": "https://www.hlww.k12.mn.us",
            "students": 300
        },
        {
            "school_name": "Humphrey Elementary School",
            "address": "8700 County Rd 6 SW, Howard Lake, MN 55349",
            "phone": "320-543-4600",
            "website": "https://www.hlww.k12.mn.us",
            "students": 200
        }
    ],
    "Hutchinson Public School District": [
        {
            "school_name": "Hutchinson High School",
            "address": "1200 Roberts Rd SW, Hutchinson, MN 55350",
            "phone": "320-587-2151",
            "website": "https://www.isd423.org",
            "students": 800
        },
        {
            "school_name": "Hutchinson Middle School",
            "address": "1365 South Grade Rd SW, Hutchinson, MN 55350",
            "phone": "320-587-2854",
            "website": "https://www.isd423.org",
            "students": 600
        },
        {
            "school_name": "Park Elementary School",
            "address": "100 Glen St SW, Hutchinson, MN 55350",
            "phone": "320-587-2837",
            "website": "https://www.isd423.org",
            "students": 400
        }
    ],
    "Infinity:Minnesota Digital Academy": [
        {
            "school_name": "Infinity:Minnesota Digital Academy",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        }
    ],
    "Intermediate School District 287": [
        {
            "school_name": "Intermediate School District 287",
            "address": "1820 Xenium Ln N, Plymouth, MN 55441",
            "phone": "763-550-7100",
            "website": "https://www.district287.org",
            "students": "N/A"
        }
    ],
    "Intermediate School District 917": [
        {
            "school_name": "Intermediate School District 917",
            "address": "1300 145th St E, Rosemount, MN 55068",
            "phone": "651-423-8229",
            "website": "https://www.isd917.org",
            "students": "N/A"
        }
    ],
    "International Falls School District": [
        {
            "school_name": "Falls High School",
            "address": "1515 11th St, International Falls, MN 56649",
            "phone": "218-283-2571",
            "website": "https://www.isd361.k12.mn.us",
            "students": 400
        },
        {
            "school_name": "Falls Elementary School",
            "address": "1515 11th St, International Falls, MN 56649",
            "phone": "218-283-2571",
            "website": "https://www.isd361.k12.mn.us",
            "students": 300
        }
    ],
    "International Spanish Language Academy": [
        {
            "school_name": "International Spanish Language Academy",
            "address": "5959 Shady Oak Rd, Minnetonka, MN 55343",
            "phone": "952-746-6020",
            "website": "https://www.isla.school",
            "students": 400
        }
    ],
    "Inver Grove Heights Schools": [
        {
            "school_name": "Simley High School",
            "address": "2920 80th St E, Inver Grove Heights, MN 55076",
            "phone": "651-306-7000",
            "website": "https://www.isd199.org",
            "students": 1200
        },
        {
            "school_name": "Inver Grove Heights Middle School",
            "address": "8167 Cahill Ave, Inver Grove Heights, MN 55076",
            "phone": "651-306-7200",
            "website": "https://www.isd199.org",
            "students": 800
        },
        {
            "school_name": "Hilltop Elementary School",
            "address": "3201 68th St E, Inver Grove Heights, MN 55076",
            "phone": "651-306-7400",
            "website": "https://www.isd199.org",
            "students": 600
        }
    ],
    "Isle Public School District": [
        {
            "school_name": "Isle High School",
            "address": "730 5th Ave S, Isle, MN 56342",
            "phone": "320-676-3146",
            "website": "https://www.isle.k12.mn.us",
            "students": 200
        },
        {
            "school_name": "Isle Elementary School",
            "address": "730 5th Ave S, Isle, MN 56342",
            "phone": "320-676-3146",
            "website": "https://www.isle.k12.mn.us",
            "students": 150
        }
    ],
    "Ivanhoe Public School District": [
        {
            "school_name": "Ivanhoe High School",
            "address": "421 N Rebecca St, Ivanhoe, MN 56142",
            "phone": "507-694-1540",
            "website": "https://www.ivanhoe.k12.mn.us",
            "students": 100
        },
        {
            "school_name": "Ivanhoe Elementary School",
            "address": "421 N Rebecca St, Ivanhoe, MN 56142",
            "phone": "507-694-1540",
            "website": "https://www.ivanhoe.k12.mn.us",
            "students": 50
        }
    ],
    "Jackson County Central School Dist.": [
        {
            "school_name": "Jackson County Central High School",
            "address": "1128 N Hwy, Jackson, MN 56143",
            "phone": "507-847-5310",
            "website": "https://www.jccschools.com",
            "students": 400
        },
        {
            "school_name": "Jackson County Central Middle School",
            "address": "1128 N Hwy, Jackson, MN 56143",
            "phone": "507-847-5310",
            "website": "https://www.jccschools.com",
            "students": 300
        },
        {
            "school_name": "Pleasantview Elementary School",
            "address": "1128 N Hwy, Jackson, MN 56143",
            "phone": "507-847-5310",
            "website": "https://www.jccschools.com",
            "students": 200
        }
    ],
    "Jane Goodall Environmental Science": [
        {
            "school_name": "Jane Goodall Environmental Sciences Academy",
            "address": "8008 83rd St NW, Maple Lake, MN 55358",
            "phone": "320-963-0677",
            "website": "https://www.jgesa.org",
            "students": 100
        }
    ],
    "Janesville-Waldorf-Pemberton School District": [
        {
            "school_name": "Janesville-Waldorf-Pemberton High School",
            "address": "110 E 3rd St, Janesville, MN 56048",
            "phone": "507-234-5181",
            "website": "https://www.jwp.k12.mn.us",
            "students": 200
        },
        {
            "school_name": "Janesville-Waldorf-Pemberton Elementary School",
            "address": "110 E 3rd St, Janesville, MN 56048",
            "phone": "507-234-5181",
            "website": "https://www.jwp.k12.mn.us",
            "students": 150
        }
    ],
    "Jennings Community Learning Center": [
        {
            "school_name": "Jennings Community Learning Center",
            "address": "2455 University Ave W, St Paul, MN 55114",
            "phone": "651-649-5403",
            "website": "https://www.jenningsclc.org",
            "students": 100
        }
    ],
    "Jordan Public School District": [
        {
            "school_name": "Jordan High School",
            "address": "600 Sunset Dr, Jordan, MN 55352",
            "phone": "952-492-4400",
            "website": "https://www.jordan.k12.mn.us",
            "students": 400
        },
        {
            "school_name": "Jordan Middle School",
            "address": "600 Sunset Dr, Jordan, MN 55352",
            "phone": "952-492-4400",
            "website": "https://www.jordan.k12.mn.us",
            "students": 300
        },
        {
            "school_name": "Jordan Elementary School",
            "address": "600 Sunset Dr, Jordan, MN 55352",
            "phone": "952-492-4400",
            "website": "https://www.jordan.k12.mn.us",
            "students": 200
        }
    ],
    "Kaleidoscope Charter School": [
        {
            "school_name": "Kaleidoscope Charter School",
            "address": "7525 Kalland Ave NE, Otsego, MN 55301",
            "phone": "763-428-1890",
            "website": "https://www.kcsmn.org",
            "students": 200
        }
    ],
    "Kasson-Mantorville School District": [
        {
            "school_name": "Kasson-Mantorville High School",
            "address": "101 16th St NE, Kasson, MN 55944",
            "phone": "507-634-2961",
            "website": "https://www.komets.k12.mn.us",
            "students": 600
        },
        {
            "school_name": "Kasson-Mantorville Middle School",
            "address": "1000 16th St NE, Kasson, MN 55944",
            "phone": "507-634-4030",
            "website": "https://www.komets.k12.mn.us",
            "students": 400
        },
        {
            "school_name": "Kasson-Mantorville Elementary School",
            "address": "902 Mantorville Ave, Kasson, MN 55944",
            "phone": "507-634-4060",
            "website": "https://www.komets.k12.mn.us",
            "students": 500
        }
    ],
    "Kato Public Charter School": [
        {
            "school_name": "Kato Public Charter School",
            "address": "800 Bunker Lake Blvd NW, Andover, MN 55304",
            "phone": "763-786-8081",
            "website": "https://www.katopcs.org",
            "students": 150
        }
    ],
    "Kelliher Public School District": [
        {
            "school_name": "Kelliher High School",
            "address": "345 4th St NW, Kelliher, MN 56663",
            "phone": "218-647-8286",
            "website": "https://www.kelliher.k12.mn.us",
            "students": 100
        },
        {
            "school_name": "Kelliher Elementary School",
            "address": "345 4th St NW, Kelliher, MN 56663",
            "phone": "218-647-8286",
            "website": "https://www.kelliher.k12.mn.us",
            "students": 50
        }
    ],
    "Kenyon-Wanamingo School District": [
        {
            "school_name": "Kenyon-Wanamingo High School",
            "address": "400 6th St, Kenyon, MN 55946",
            "phone": "507-789-6186",
            "website": "https://www.kw.k12.mn.us",
            "students": 300
        },
        {
            "school_name": "Kenyon-Wanamingo Elementary School",
            "address": "400 6th St, Kenyon, MN 55946",
            "phone": "507-789-6186",
            "website": "https://www.kw.k12.mn.us",
            "students": 200
        }
    ],
    "Kerkhoven-Murdock-Sunburg School District": [
        {
            "school_name": "KMS High School",
            "address": "132 N Front St, Kerkhoven, MN 56252",
            "phone": "320-264-8811",
            "website": "https://www.kms.k12.mn.us",
            "students": 200
        },
        {
            "school_name": "KMS Elementary School",
            "address": "132 N Front St, Kerkhoven, MN 56252",
            "phone": "320-264-8811",
            "website": "https://www.kms.k12.mn.us",
            "students": 150
        }
    ],
    "Kimball Public School District": [
        {
            "school_name": "Kimball Area High School",
            "address": "3200 W Maple St, Kimball, MN 55353",
            "phone": "320-398-7700",
            "website": "https://www.kimball.k12.mn.us",
            "students": 300
        },
        {
            "school_name": "Kimball Area Elementary School",
            "address": "3200 W Maple St, Kimball, MN 55353",
            "phone": "320-398-7700",
            "website": "https://www.kimball.k12.mn.us",
            "students": 200
        }
    ],
    "Kingsland Public School District": [
        {
            "school_name": "Kingsland High School",
            "address": "115 W Bacon St, Spring Valley, MN 55975",
            "phone": "507-346-7276",
            "website": "https://www.kingsland.k12.mn.us",
            "students": 300
        },
        {
            "school_name": "Kingsland Elementary School",
            "address": "115 W Bacon St, Spring Valley, MN 55975",
            "phone": "507-346-7276",
            "website": "https://www.kingsland.k12.mn.us",
            "students": 200
        }
    ],
    "Kipp Minnesota Charter School": [
        {
            "school_name": "KIPP Minnesota",
            "address": "200 E Lake St, Minneapolis, MN 55408",
            "phone": "612-596-6226",
            "website": "https://kippminnesota.org",
            "students": 400
        }
    ],
    "Kittson Central School District": [
        {
            "school_name": "Kittson Central High School",
            "address": "454 Davis Ave S, Hallock, MN 56728",
            "phone": "218-843-3682",
            "website": "https://www.kittson.k12.mn.us",
            "students": 150
        },
        {
            "school_name": "Kittson Central Elementary School",
            "address": "454 Davis Ave S, Hallock, MN 56728",
            "phone": "218-843-3682",
            "website": "https://www.kittson.k12.mn.us",
            "students": 100
        }
    ],
    "La Crescent-Hokah School District": [
        {
            "school_name": "La Crescent-Hokah High School",
            "address": "1301 Lancer Blvd, La Crescent, MN 55947",
            "phone": "507-895-4484",
            "website": "https://www.lc.k12.mn.us",
            "students": 400
        },
        {
            "school_name": "La Crescent-Hokah Elementary School",
            "address": "1301 Lancer Blvd, La Crescent, MN 55947",
            "phone": "507-895-4484",
            "website": "https://www.lc.k12.mn.us",
            "students": 300
        }
    ],
    "Lac Qui Parle Valley School Dist.": [
        {
            "school_name": "Lac qui Parle Valley High School",
            "address": "500 Dakota Ave N, Madison, MN 56256",
            "phone": "320-598-3193",
            "website": "https://www.lqpv.org",
            "students": 200
        },
        {
            "school_name": "Lac qui Parle Valley Elementary School",
            "address": "500 Dakota Ave N, Madison, MN 56256",
            "phone": "320-598-3193",
            "website": "https://www.lqpv.org",
            "students": 150
        }
    ],
    "Lacrescent Montessori Academy": [
        {
            "school_name": "Lacrescent Montessori Academy",
            "address": "1116 Oak Terrace Dr, La Crescent, MN 55947",
            "phone": "507-895-4054",
            "website": "https://www.lacrescentmontessori.com",
            "students": 100
        }
    ],
    "Lafayette Public Charter School": [
        {
            "school_name": "Lafayette Public Charter School",
            "address": "3501 Fairview Ave N, Robbinsdale, MN 55422",
            "phone": "763-252-5242",
            "website": "https://www.lafayettecharter.org",
            "students": 150
        }
    ],
    "Lake Benton Public School District": [
        {
            "school_name": "Lake Benton High School",
            "address": "314 W Becker St, Lake Benton, MN 56149",
            "phone": "507-368-4263",
            "website": "https://www.lbsd.k12.mn.us",
            "students": 100
        },
        {
            "school_name": "Lake Benton Elementary School",
            "address": "314 W Becker St, Lake Benton, MN 56149",
            "phone": "507-368-4263",
            "website": "https://www.lbsd.k12.mn.us",
            "students": 50
        }
    ],
    "Lake City Public School District": [
        {
            "school_name": "Lincoln High School",
            "address": "1025 Delaware St, Lake City, MN 55041",
            "phone": "651-345-3227",
            "website": "https://www.lc.k12.mn.us",
            "students": 400
        },
        {
            "school_name": "Bluff View Elementary School",
            "address": "1025 Delaware St, Lake City, MN 55041",
            "phone": "651-345-3227",
            "website": "https://www.lc.k12.mn.us",
            "students": 300
        }
    ],
    "Lake Crystal-Wellcome Memorial School District": [
        {
            "school_name": "Lake Crystal Wellcome Memorial Secondary School",
            "address": "273 Mustang Ave, Lake Crystal, MN 56055",
            "phone": "507-726-2320",
            "website": "https://www.lcwm.k12.mn.us",
            "students": 400
        },
        {
            "school_name": "Lake Crystal Wellcome Memorial Elementary School",
            "address": "273 Mustang Ave, Lake Crystal, MN 56055",
            "phone": "507-726-2320",
            "website": "https://www.lcwm.k12.mn.us",
            "students": 300
        }
    ],
    "Lake Of The Woods School District": [
        {
            "school_name": "Lake of the Woods School",
            "address": "236 Cty Rd 1, Baudette, MN 56623",
            "phone": "218-634-2510",
            "website": "https://www.lakeofthewoodsschool.org",
            "students": 400
        }
    ],
    "Lake Park Audubon School District": [
        {
            "school_name": "Lake Park Audubon High School",
            "address": "611 Raider Dr, Lake Park, MN 56554",
            "phone": "218-325-0754",
            "website": "https://www.lakeparkaudubon.com",
            "students": 300
        },
        {
            "school_name": "Lake Park Audubon Elementary School",
            "address": "611 Raider Dr, Lake Park, MN 56554",
            "phone": "218-325-0754",
            "website": "https://www.lakeparkaudubon.com",
            "students": 200
        }
    ],
    "Lake Superior Public School Dist.": [
        {
            "school_name": "Lake Superior High School",
            "address": "5345 Blvd N, Superior, WI 54880",
            "phone": "715-394-8720",
            "website": "https://www.lakesuperiorsd.org",
            "students": 300
        },
        {
            "school_name": "Lake Superior Elementary School",
            "address": "5345 Blvd N, Superior, WI 54880",
            "phone": "715-394-8720",
            "website": "https://www.lakesuperiorsd.org",
            "students": 200
        }
    ],
    "Lakes International Language Admy": [
        {
            "school_name": "Lakes International Language Academy",
            "address": "246 10th Ave SE, Forest Lake, MN 55025",
            "phone": "651-464-0771",
            "website": "https://www.mylila.org",
            "students": 600
        }
    ],
    "Lakeview School District": [
        {
            "school_name": "Lakeview High School",
            "address": "619 Main St N, Cottonwood, MN 56229",
            "phone": "507-423-5164",
            "website": "https://www.lakeview2167.com",
            "students": 200
        },
        {
            "school_name": "Lakeview Elementary School",
            "address": "875 Barstad Rd N, Cottonwood, MN 56229",
            "phone": "507-423-5479",
            "website": "https://www.lakeview2167.com",
            "students": 150
        }
    ],
    "Lakeville Public School District": [
        {
            "school_name": "Lakeville North High School",
            "address": "19600 Ipava Ave, Lakeville, MN 55044",
            "phone": "952-232-3800",
            "website": "https://isd194.org",
            "students": 1800
        },
        {
            "school_name": "Lakeville South High School",
            "address": "21135 Jacquard Ave, Lakeville, MN 55044",
            "phone": "952-232-3700",
            "website": "https://isd194.org",
            "students": 1700
        },
        {
            "school_name": "Century Middle School",
            "address": "18932 Dodd Blvd, Lakeville, MN 55044",
            "phone": "952-232-2800",
            "website": "https://isd194.org",
            "students": 900
        }
    ],
    "Lancaster Public School District": [
        {
            "school_name": "Lancaster Elementary School",
            "address": "1013 Elm St, Lancaster, MN 56735",
            "phone": "218-762-5400",
            "website": "https://www.lancasterschools.org",
            "students": 200
        },
        {
            "school_name": "Lancaster Secondary School",
            "address": "1013 Elm St, Lancaster, MN 56735",
            "phone": "218-762-5400",
            "website": "https://www.lancasterschools.org",
            "students": 150
        }
    ],
    "Lanesboro Public School District": [
        {
            "school_name": "Lanesboro High School",
            "address": "100 Elmwood Ave N, Lanesboro, MN 55949",
            "phone": "507-467-2229",
            "website": "https://www.lanesboro.k12.mn.us",
            "students": 150
        },
        {
            "school_name": "Lanesboro Elementary School",
            "address": "100 Elmwood Ave N, Lanesboro, MN 55949",
            "phone": "507-467-2229",
            "website": "https://www.lanesboro.k12.mn.us",
            "students": 100
        }
    ],
    "Laporte Public School District": [
        {
            "school_name": "Laporte Secondary School",
            "address": "305 Badger Ave, Laporte, MN 56461",
            "phone": "218-224-2288",
            "website": "https://www.laporte.k12.mn.us",
            "students": 150
        },
        {
            "school_name": "Laporte Elementary School",
            "address": "305 Badger Ave, Laporte, MN 56461",
            "phone": "218-224-2288",
            "website": "https://www.laporte.k12.mn.us",
            "students": 100
        }
    ],
    "Laura Jeffrey Academy Charter": [
        {
            "school_name": "Laura Jeffrey Academy",
            "address": "1550 Ames Ave, St Paul, MN 55106",
            "phone": "651-379-9300",
            "website": "https://www.laurajeffreyacademy.org",
            "students": 400
        }
    ],
    "Learning For Leadership Charter": [
        {
            "school_name": "Learning for Leadership Charter School",
            "address": "3005 W 28th St, Minneapolis, MN 55416",
            "phone": "612-465-0935",
            "website": "https://www.learningforleadership.org",
            "students": 200
        }
    ],
    "Legacy of DR Josie R Johnson Montes": [
        {
            "school_name": "Legacy of Dr. Josie R. Johnson Montessori",
            "address": "5140 Fremont Ave N, Minneapolis, MN 55430",
            "phone": "763-971-7417",
            "website": "https://www.jjmontessori.org",
            "students": 150
        }
    ],
    "Leroy-Ostrander Public Schools": [
        {
            "school_name": "LeRoy-Ostrander Secondary School",
            "address": "101 Prospect Ave, LeRoy, MN 55951",
            "phone": "507-324-7142",
            "website": "https://www.leroy.k12.mn.us",
            "students": 200
        },
        {
            "school_name": "LeRoy-Ostrander Elementary School",
            "address": "101 Prospect Ave, LeRoy, MN 55951",
            "phone": "507-324-7142",
            "website": "https://www.leroy.k12.mn.us",
            "students": 150
        }
    ],
    "Lester Prairie Public School Dist.": [
        {
            "school_name": "Lester Prairie Secondary School",
            "address": "131 Woodlawn Ave N, Lester Prairie, MN 55354",
            "phone": "320-395-2521",
            "website": "https://www.lp.k12.mn.us",
            "students": 200
        },
        {
            "school_name": "Lester Prairie Elementary School",
            "address": "131 Woodlawn Ave N, Lester Prairie, MN 55354",
            "phone": "320-395-2521",
            "website": "https://www.lp.k12.mn.us",
            "students": 150
        }
    ],
    "Lesueur-Henderson School District": [
        {
            "school_name": "Le Sueur-Henderson High School",
            "address": "901 E Ferry St, Le Sueur, MN 56058",
            "phone": "507-665-6615",
            "website": "https://www.lesueur.k12.mn.us",
            "students": 400
        },
        {
            "school_name": "Park Elementary School",
            "address": "115 Fairlawn Ave S, Le Sueur, MN 56058",
            "phone": "507-665-4600",
            "website": "https://www.lesueur.k12.mn.us",
            "students": 300
        }
    ],
    "Level Up Academy": [
        {
            "school_name": "Level Up Academy",
            "address": "1801 Lacrosse Ave, St Paul, MN 55119",
            "phone": "651-778-2940",
            "website": "https://www.levelupacademy.org",
            "students": 100
        }
    ],
    "Lewiston-Altura Public School Dist.": [
        {
            "school_name": "Lewiston-Altura High School",
            "address": "3347 US-14, Lewiston, MN 55952",
            "phone": "507-523-2191",
            "website": "https://www.lewalt.k12.mn.us",
            "students": 300
        },
        {
            "school_name": "Lewiston-Altura Elementary School",
            "address": "3347 US-14, Lewiston, MN 55952",
            "phone": "507-523-2194",
            "website": "https://www.lewalt.k12.mn.us",
            "students": 200
        }
    ],
    "Life Prep": [
        {
            "school_name": "Life Prep School of St. Paul",
            "address": "345 32nd St E, St Paul, MN 55107",
            "phone": "651-917-0073",
            "website": "https://www.lifeprep.net",
            "students": 200
        }
    ],
    "Lincoln International School": [
        {
            "school_name": "Lincoln International School",
            "address": "2521 Longfellow Ave, Minneapolis, MN 55406",
            "phone": "612-668-4300",
            "website": "https://lincoln.mpls.k12.mn.us",
            "students": 400
        }
    ],
    "Lionsgate Academy": [
        {
            "school_name": "Lionsgate Academy",
            "address": "8200 Zane Ave N, Brooklyn Park, MN 55443",
            "phone": "763-569-7787",
            "website": "https://www.lionsgate.school",
            "students": 600
        }
    ],
    "Litchfield Public School District": [
        {
            "school_name": "Litchfield High School",
            "address": "615 Cyrus St N, Litchfield, MN 55355",
            "phone": "320-693-2441",
            "website": "https://www.litchfield.k12.mn.us",
            "students": 500
        },
        {
            "school_name": "Litchfield Middle School",
            "address": "703 E Mallard St, Litchfield, MN 55355",
            "phone": "320-693-2436",
            "website": "https://www.litchfield.k12.mn.us",
            "students": 400
        },
        {
            "school_name": "Litchfield Elementary School",
            "address": "1109 N Gilman Ave, Litchfield, MN 55355",
            "phone": "320-693-2432",
            "website": "https://www.litchfield.k12.mn.us",
            "students": 300
        }
    ],
    "Little Falls Public School District": [
        {
            "school_name": "Little Falls Community High School",
            "address": "1001 SE 5th Ave, Little Falls, MN 56345",
            "phone": "320-616-2200",
            "website": "https://www.lfcsk12.org",
            "students": 600
        },
        {
            "school_name": "Little Falls Community Middle School",
            "address": "1001 SE 5th Ave, Little Falls, MN 56345",
            "phone": "320-616-2200",
            "website": "https://www.lfcsk12.org",
            "students": 400
        },
        {
            "school_name": "Little Falls Community Elementary School",
            "address": "1001 SE 5th Ave, Little Falls, MN 56345",
            "phone": "320-616-2200",
            "website": "https://www.lfcsk12.org",
            "students": 300
        }
    ],
    "Littlefork-Big Falls School Dist.": [
        {
            "school_name": "Littlefork-Big Falls Secondary School",
            "address": "615 Main St, Littlefork, MN 56653",
            "phone": "218-278-4135",
            "website": "https://www.lfbf.k12.mn.us",
            "students": 150
        },
        {
            "school_name": "Littlefork-Big Falls Elementary School",
            "address": "615 Main St, Littlefork, MN 56653",
            "phone": "218-278-4135",
            "website": "https://www.lfbf.k12.mn.us",
            "students": 100
        }
    ],
    "Long Prairie-Grey Eagle School Dist.": [
        {
            "school_name": "Long Prairie-Grey Eagle Secondary School",
            "address": "305 2nd St NE, Long Prairie, MN 56347",
            "phone": "320-732-2194",
            "website": "https://www.lpge.k12.mn.us",
            "students": 300
        },
        {
            "school_name": "Long Prairie-Grey Eagle Elementary School",
            "address": "305 2nd St NE, Long Prairie, MN 56347",
            "phone": "320-732-2194",
            "website": "https://www.lpge.k12.mn.us",
            "students": 200
        }
    ],
    "Loveworks Academy For Arts": [
        {
            "school_name": "LoveWorks Academy for Visual & Performing Arts",
            "address": "2805 N 30th Ave, Minneapolis, MN 55411",
            "phone": "612-522-5812",
            "website": "https://www.loveworksacademy.org",
            "students": 200
        }
    ],
    "Luverne Public School District": [
        {
            "school_name": "Luverne High School",
            "address": "709 N Kniss Ave, Luverne, MN 56156",
            "phone": "507-283-8088",
            "website": "https://www.luverne.k12.mn.us",
            "students": 300
        },
        {
            "school_name": "Luverne Elementary School",
            "address": "709 N Kniss Ave, Luverne, MN 56156",
            "phone": "507-283-8088",
            "website": "https://www.luverne.k12.mn.us",
            "students": 200
        }
    ],
    "Lyle Public School District": [
        {
            "school_name": "Lyle Secondary School",
            "address": "700 Main St, Lyle, MN 55953",
            "phone": "507-325-2201",
            "website": "https://www.lyle.k12.mn.us",
            "students": 150
        },
        {
            "school_name": "Lyle Elementary School",
            "address": "700 Main St, Lyle, MN 55953",
            "phone": "507-325-2201",
            "website": "https://www.lyle.k12.mn.us",
            "students": 100
        }
    ],
    "Lynd Public School District": [
        {
            "school_name": "Lynd Public School",
            "address": "175 Maple St, Lynd, MN 56157",
            "phone": "507-865-4404",
            "website": "https://www.lyndschool.org",
            "students": 100
        }
    ],
    "Minnesota Mabel-Canton Public School Dist.": [
        {
            "school_name": "Mabel-Canton Elementary School",
            "address": "316 Fillmore Ave W, Mabel, MN 55954",
            "phone": "(507) 493-5422",
            "website": "https://www.mabelcanton.k12.mn.us/",
            "students": 275
        },
        {
            "school_name": "Mabel-Canton Secondary School",
            "address": "316 Fillmore Ave W, Mabel, MN 55954",
            "phone": "(507) 493-5423",
            "website": "https://www.mabelcanton.k12.mn.us/",
            "students": 225
        }
    ],
    "Maccray School District": [
        {
            "school_name": "MACCRAY Elementary School",
            "address": "711 Wolverine Dr, Clara City, MN 56222",
            "phone": "(320) 847-2154",
            "website": "https://www.maccray.k12.mn.us/",
            "students": 350
        },
        {
            "school_name": "MACCRAY Secondary School",
            "address": "711 Wolverine Dr, Clara City, MN 56222",
            "phone": "(320) 847-2154",
            "website": "https://www.maccray.k12.mn.us/",
            "students": 300
        }
    ],
    "Madelia Public School District": [
        {
            "school_name": "Madelia Elementary School",
            "address": "307 W Ramsey St, Madelia, MN 56062",
            "phone": "(507) 642-3422",
            "website": "https://www.madelia.k12.mn.us/",
            "students": 250
        },
        {
            "school_name": "Madelia Secondary School",
            "address": "307 W Ramsey St, Madelia, MN 56062",
            "phone": "(507) 642-3421",
            "website": "https://www.madelia.k12.mn.us/",
            "students": 200
        }
    ],
    "Mahnomen Public School District": [
        {
            "school_name": "Mahnomen Elementary School",
            "address": "209 1st Ave SW, Mahnomen, MN 56557",
            "phone": "(218) 935-2581",
            "website": "https://www.mahnomen.k12.mn.us/",
            "students": 300
        },
        {
            "school_name": "Mahnomen Secondary School",
            "address": "209 1st Ave SW, Mahnomen, MN 56557",
            "phone": "(218) 935-2582",
            "website": "https://www.mahnomen.k12.mn.us/",
            "students": 250
        }
    ],
    "Mahtomedi Public School District": [
        {
            "school_name": "Mahtomedi Elementary School",
            "address": "8100 75th St N, Mahtomedi, MN 55115",
            "phone": "(651) 407-2100",
            "website": "https://www.mahtomedi.k12.mn.us/",
            "students": 1200
        },
        {
            "school_name": "Mahtomedi Middle School",
            "address": "8530 Wildwood Rd, Mahtomedi, MN 55115",
            "phone": "(651) 407-2400",
            "website": "https://www.mahtomedi.k12.mn.us/",
            "students": 900
        },
        {
            "school_name": "Mahtomedi High School",
            "address": "8000 75th St N, Mahtomedi, MN 55115",
            "phone": "(651) 407-2500",
            "website": "https://www.mahtomedi.k12.mn.us/",
            "students": 1300
        }
    ],
    "Mankato Public School District": [
        {
            "school_name": "Mankato East High School",
            "address": "2600 Hoffman Rd, Mankato, MN 56001",
            "phone": "(507) 387-5671",
            "website": "https://www.mankatoschools.org/",
            "students": 1100
        },
        {
            "school_name": "Mankato West High School",
            "address": "1351 Monks Ave, Mankato, MN 56001",
            "phone": "(507) 387-3461",
            "website": "https://www.mankatoschools.org/",
            "students": 1200
        },
        {
            "school_name": "Mankato Area Public Schools Elementary",
            "address": "Various locations",
            "phone": "(507) 387-1911",
            "website": "https://www.mankatoschools.org/",
            "students": 3500
        }
    ],
    "Maple Lake Public School District": [
        {
            "school_name": "Maple Lake Elementary School",
            "address": "700 Prospect Ave, Maple Lake, MN 55358",
            "phone": "(320) 963-3024",
            "website": "https://www.maplelake.k12.mn.us/",
            "students": 450
        },
        {
            "school_name": "Maple Lake Secondary School",
            "address": "180 Park Ave E, Maple Lake, MN 55358",
            "phone": "(320) 963-3171",
            "website": "https://www.maplelake.k12.mn.us/",
            "students": 500
        }
    ],
    "Maple River School District": [
        {
            "school_name": "Maple River Elementary School",
            "address": "211 Buckeye St, Mapleton, MN 56065",
            "phone": "(507) 524-3918",
            "website": "https://www.isd2135.org/",
            "students": 350
        },
        {
            "school_name": "Maple River Secondary School",
            "address": "101 6th Ave NE, Mapleton, MN 56065",
            "phone": "(507) 524-3918",
            "website": "https://www.isd2135.org/",
            "students": 400
        }
    ],
    "Marine Area Community School": [
        {
            "school_name": "Marine Area Community School",
            "address": "14189 Ostlund Trl N, Marine on St. Croix, MN 55047",
            "phone": "(651) 409-3122",
            "website": "https://marinecs.org/",
            "students": 200
        }
    ],
    "Marshall County Central Schools": [
        {
            "school_name": "Marshall County Central Elementary School",
            "address": "310 W College Dr, Newfolden, MN 56738",
            "phone": "(218) 874-8530",
            "website": "https://www.marshallcountycentral.k12.mn.us/",
            "students": 250
        },
        {
            "school_name": "Marshall County Central Secondary School",
            "address": "310 W College Dr, Newfolden, MN 56738",
            "phone": "(218) 874-8530",
            "website": "https://www.marshallcountycentral.k12.mn.us/",
            "students": 200
        }
    ],
    "Marshall Public School District": [
        {
            "school_name": "Marshall Area Elementary Schools",
            "address": "Various locations, Marshall, MN 56258",
            "phone": "(507) 537-6962",
            "website": "https://www.marshall.k12.mn.us/",
            "students": 1200
        },
        {
            "school_name": "Marshall Middle School",
            "address": "400 Tiger Dr, Marshall, MN 56258",
            "phone": "(507) 537-6938",
            "website": "https://www.marshall.k12.mn.us/",
            "students": 600
        },
        {
            "school_name": "Marshall High School",
            "address": "510 Tiger Dr, Marshall, MN 56258",
            "phone": "(507) 537-6920",
            "website": "https://www.marshall.k12.mn.us/",
            "students": 900
        }
    ],
    "Martin County West School District": [
        {
            "school_name": "Martin County West Elementary School",
            "address": "105 E 5th St, Sherburn, MN 56171",
            "phone": "(507) 764-4661",
            "website": "https://www.mcwmavericks.org/",
            "students": 350
        },
        {
            "school_name": "Martin County West Secondary School",
            "address": "105 E 5th St, Sherburn, MN 56171",
            "phone": "(507) 764-4661",
            "website": "https://www.mcwmavericks.org/",
            "students": 300
        }
    ],
    "Mastery School": [
        {
            "school_name": "Mastery School",
            "address": "4675 Huntington Ave S, St Louis Park, MN 55416",
            "phone": "(952) 591-3719",
            "website": "https://www.masteryschool.org/",
            "students": 150
        }
    ],
    "Math And Science Academy": [
        {
            "school_name": "Math and Science Academy",
            "address": "5625 Shingle Creek Pkwy, Brooklyn Center, MN 55430",
            "phone": "(763) 971-7701",
            "website": "https://www.msa.mncs.k12.mn.us/",
            "students": 500
        }
    ],
    "Mcgregor Public School District": [
        {
            "school_name": "McGregor Elementary School",
            "address": "43543 Cty Rd 200, McGregor, MN 55760",
            "phone": "(218) 768-2107",
            "website": "https://www.isd004.org/",
            "students": 150
        },
        {
            "school_name": "McGregor Secondary School",
            "address": "43543 Cty Rd 200, McGregor, MN 55760",
            "phone": "(218) 768-2107",
            "website": "https://www.isd004.org/",
            "students": 100
        }
    ],
    "Medford Public School District": [
        {
            "school_name": "Medford Elementary School",
            "address": "522 2nd St SE, Medford, MN 55049",
            "phone": "(507) 451-5604",
            "website": "https://www.medford.k12.mn.us/",
            "students": 300
        },
        {
            "school_name": "Medford Secondary School",
            "address": "522 2nd St SE, Medford, MN 55049",
            "phone": "(507) 451-5604",
            "website": "https://www.medford.k12.mn.us/",
            "students": 250
        }
    ],
    "Meeker And Wright Special Education": [
        {
            "school_name": "Meeker and Wright Special Education Cooperative",
            "address": "567 Litchfield Ave SW, Willmar, MN 56201",
            "phone": "(320) 231-8511",
            "website": "https://www.mnmwsec.org/",
            "students": 500
        }
    ],
    "Melrose Public School District": [
        {
            "school_name": "Melrose Elementary School",
            "address": "562 S 7th St W, Melrose, MN 56352",
            "phone": "(320) 256-5180",
            "website": "https://www.melroseschools.org/",
            "students": 400
        },
        {
            "school_name": "Melrose Secondary School",
            "address": "562 S 7th St W, Melrose, MN 56352",
            "phone": "(320) 256-5180",
            "website": "https://www.melroseschools.org/",
            "students": 350
        }
    ],
    "Menahga Public School District": [
        {
            "school_name": "Menahga Elementary School",
            "address": "216 Aspen Ave SE, Menahga, MN 56464",
            "phone": "(218) 564-4907",
            "website": "https://www.menahga.k12.mn.us/",
            "students": 300
        },
        {
            "school_name": "Menahga Secondary School",
            "address": "216 Aspen Ave SE, Menahga, MN 56464",
            "phone": "(218) 564-4907",
            "website": "https://www.menahga.k12.mn.us/",
            "students": 250
        }
    ],
    "Mesabi East School District": [
        {
            "school_name": "Mesabi East Elementary School",
            "address": "1901 E Camp St, Ely, MN 55731",
            "phone": "(218) 365-6166",
            "website": "https://www.isd2711.org/",
            "students": 300
        },
        {
            "school_name": "Mesabi East Secondary School",
            "address": "901 N 9th Ave E, Aurora, MN 55705",
            "phone": "(218) 229-3321",
            "website": "https://www.isd2711.org/",
            "students": 250
        }
    ],
    "Metro Schools Charter": [
        {
            "school_name": "Metro Schools Charter",
            "address": "620 Virginia St, St. Paul, MN 55103",
            "phone": "(651) 379-7600",
            "website": "https://metroschoolsmn.org/",
            "students": 200
        }
    ],
    "Mid State Education District": [
        {
            "school_name": "Mid State Education District",
            "address": "5701 Normandale Rd, Edina, MN 55424",
            "phone": "(952) 567-8000",
            "website": "https://www.midstatesd.org/",
            "students": 500
        }
    ],
    "Midway Star Academy": [
        {
            "school_name": "Midway Star Academy",
            "address": "1633 University Ave W, St Paul, MN 55104",
            "phone": "(651) 379-7600",
            "website": "https://www.midwaystar.org/",
            "students": 150
        }
    ],
    "Milaca Public School District": [
        {
            "school_name": "Milaca Elementary School",
            "address": "25 2nd Ave SW, Milaca, MN 56353",
            "phone": "(320) 982-7286",
            "website": "https://www.milaca.k12.mn.us/",
            "students": 500
        },
        {
            "school_name": "Milaca Secondary School",
            "address": "180 Park Ave E, Maple Lake, MN 55358",
            "phone": "(320) 963-3171",
            "website": "https://www.milaca.k12.mn.us/",
            "students": 1184
        }
    ],
    "Milroy Area Charter School": [
        {
            "school_name": "Milroy Area Charter School",
            "address": "416 Minnesota St, Milroy, MN 56263",
            "phone": "(507) 336-8722",
            "website": "https://www.milroyareacharterschool.org/",
            "students": 50
        }
    ],
    "Milroy Public School District": [
        {
            "school_name": "Milroy Elementary School",
            "address": "416 Minnesota St, Milroy, MN 56263",
            "phone": "(507) 336-2563",
            "website": "https://www.milroy.k12.mn.us/",
            "students": 100
        },
        {
            "school_name": "Milroy Secondary School",
            "address": "416 Minnesota St, Milroy, MN 56263",
            "phone": "(507) 336-2563",
            "website": "https://www.milroy.k12.mn.us/",
            "students": 75
        }
    ],
    "Minisinaakwaang Leadership Academy": [
        {
            "school_name": "Minisinaakwaang Leadership Academy",
            "address": "3629 E 28th St, Minneapolis, MN 55406",
            "phone": "(612) 235-7628",
            "website": "https://www.minisinaakwaang.org/",
            "students": 150
        }
    ],
    "Minneapolis Public School Dist.": [
        {
            "school_name": "Minneapolis Public Schools",
            "address": "1250 W Broadway Ave, Minneapolis, MN 55411",
            "phone": "(612) 668-0000",
            "website": "https://www.mpls.k12.mn.us/",
            "students": 34000
        }
    ],
    "Minneota Public School District": [
        {
            "school_name": "Minneota Elementary School",
            "address": "504 N Monroe St, Minneota, MN 56264",
            "phone": "(507) 872-6175",
            "website": "https://www.minneotaschools.org/",
            "students": 200
        },
        {
            "school_name": "Minneota Secondary School",
            "address": "504 N Monroe St, Minneota, MN 56264",
            "phone": "(507) 872-6175",
            "website": "https://www.minneotaschools.org/",
            "students": 250
        }
    ],
    "Minnesota Department Of Corrections": [
        {
            "school_name": "Minnesota Correctional Facility Schools",
            "address": "Various locations",
            "phone": "(651) 361-7200",
            "website": "https://mn.gov/doc/",
            "students": 1000
        }
    ],
    "Minnesota Excellence In Learning Ac": [
        {
            "school_name": "Minnesota Excellence in Learning Academy",
            "address": "6510 Singletree Ln, Maple Grove, MN 55369",
            "phone": "(763) 235-7900",
            "website": "https://www.emailac.org/",
            "students": 150
        }
    ],
    "Minnesota Internship Center": [
        {
            "school_name": "Minnesota Internship Center",
            "address": "6425 Nicollet Ave S, Richfield, MN 55423",
            "phone": "(612) 501-6379",
            "website": "https://www.interninmn.org/",
            "students": 200
        }
    ],
    "Minnesota Math And Science Academy": [
        {
            "school_name": "Minnesota Math and Science Academy",
            "address": "9400 Cedar Lake Rd, St Louis Park, MN 55426",
            "phone": "(952) 737-6900",
            "website": "https://www.mnmathsciacademy.org/",
            "students": 500
        }
    ],
    "Minnesota New Country School": [
        {
            "school_name": "Minnesota New Country School",
            "address": "210 Main St, Henderson, MN 56044",
            "phone": "(507) 248-3353",
            "website": "https://www.newcountryschool.com/",
            "students": 150
        }
    ],
    "Minnesota Online High School": [
        {
            "school_name": "Minnesota Online High School",
            "address": "Online school",
            "phone": "(952) 388-1599",
            "website": "https://www.mnvs.org/",
            "students": 500
        }
    ],
    "Minnesota Transitions Charter School": [
        {
            "school_name": "Minnesota Transitions Charter School",
            "address": "2872 26th Ave S, Minneapolis, MN 55406",
            "phone": "(612) 722-9013",
            "website": "https://mtcs.org/",
            "students": 300
        }
    ],
    "Minnesota Wildflower Montessori School": [
        {
            "school_name": "Minnesota Wildflower Montessori School",
            "address": "24120 Chippendale Ave W, Farmington, MN 55024",
            "phone": "(651) 460-3835",
            "website": "https://mnwildflower.org/",
            "students": 150
        }
    ],
    "Minnetonka Public School District": [
        {
            "school_name": "Minnetonka Elementary Schools",
            "address": "Various locations, Minnetonka, MN 55345",
            "phone": "(952) 401-5000",
            "website": "https://tonkaschools.org/",
            "students": 3500
        },
        {
            "school_name": "Minnetonka Middle School East",
            "address": "17000 Lake St Ext, Minnetonka, MN 55345",
            "phone": "(952) 401-5300",
            "website": "https://tonkaschools.org/",
            "students": 1100
        },
        {
            "school_name": "Minnetonka Middle School West",
            "address": "6421 Hazeltine Blvd, Excelsior, MN 55331",
            "phone": "(952) 401-5600",
            "website": "https://tonkaschools.org/",
            "students": 1000
        },
        {
            "school_name": "Minnetonka High School",
            "address": "18301 Highway 7, Minnetonka, MN 55345",
            "phone": "(952) 401-5700",
            "website": "https://tonkaschools.org/",
            "students": 3200
        }
    ],
    "Minnewaska School District": [
        {
            "school_name": "Minnewaska Area Elementary School",
            "address": "100 Hwy 29 N, Glenwood, MN 56334",
            "phone": "(320) 239-4800",
            "website": "https://www.minnewaska.k12.mn.us/",
            "students": 500
        },
        {
            "school_name": "Minnewaska Area Secondary School",
            "address": "25808 State Hwy 28, Glenwood, MN 56334",
            "phone": "(320) 239-4820",
            "website": "https://www.minnewaska.k12.mn.us/",
            "students": 600
        }
    ],
    "Mn Academy For Hearing Speech & Lang": [
        {
            "school_name": "Minnesota Academy for the Deaf",
            "address": "615 Olof Hanson Dr, Faribault, MN 55021",
            "phone": "(507) 412-4800",
            "website": "https://mn.gov/deaf-school/",
            "students": 120
        }
    ],
    "Mn International Middle Charter": [
        {
            "school_name": "Minnesota International Middle Charter School",
            "address": "4200 W Broadway Ave, Robbinsdale, MN 55422",
            "phone": "(763) 285-7800",
            "website": "https://mninternatmiddle.org/",
            "students": 300
        }
    ],
    "Mn River Valley Education District": [
        {
            "school_name": "Minnesota River Valley Education District",
            "address": "801 Davis St, Le Sueur, MN 56058",
            "phone": "(507) 665-4800",
            "website": "https://mnved.org/",
            "students": 500
        }
    ],
    "Montevideo Public School District": [
        {
            "school_name": "Montevideo Elementary School",
            "address": "1025 William Ave, Montevideo, MN 56265",
            "phone": "(320) 269-6584",
            "website": "https://www.montevideoschools.org/",
            "students": 500
        },
        {
            "school_name": "Montevideo Secondary School",
            "address": "1501 William Ave, Montevideo, MN 56265",
            "phone": "(320) 269-6446",
            "website": "https://www.montevideoschools.org/",
            "students": 600
        }
    ],
    "Monticello Public School District": [
        {
            "school_name": "Monticello Elementary Schools",
            "address": "Various locations, Monticello, MN 55362",
            "phone": "(763) 272-2000",
            "website": "https://monticello.k12.mn.us/",
            "students": 1800
        },
        {
            "school_name": "Monticello Middle School",
            "address": "5789 Pinewood Dr, Monticello, MN 55362",
            "phone": "(763) 272-2300",
            "website": "https://monticello.k12.mn.us/",
            "students": 900
        },
        {
            "school_name": "Monticello High School",
            "address": "5225 School Blvd, Monticello, MN 55362",
            "phone": "(763) 272-3000",
            "website": "https://monticello.k12.mn.us/",
            "students": 1400
        }
    ],
    "Moorhead Public School District": [
        {
            "school_name": "Moorhead Elementary Schools",
            "address": "Various locations, Moorhead, MN 56560",
            "phone": "(218) 284-3300",
            "website": "https://www.moorheadschools.org/",
            "students": 2500
        },
        {
            "school_name": "Moorhead Middle Schools",
            "address": "Various locations, Moorhead, MN 56560",
            "phone": "(218) 284-3300",
            "website": "https://www.moorheadschools.org/",
            "students": 1500
        },
        {
            "school_name": "Moorhead High School",
            "address": "2300 28th St S, Moorhead, MN 56560",
            "phone": "(218) 284-2300",
            "website": "https://www.moorheadschools.org/",
            "students": 1800
        }
    ],
    "Moose Lake Public School District": [
        {
            "school_name": "Moose Lake Elementary School",
            "address": "4594 County Rd 10, Moose Lake, MN 55767",
            "phone": "(218) 485-4184",
            "website": "https://www.ml115.org/",
            "students": 300
        },
        {
            "school_name": "Moose Lake Secondary School",
            "address": "4594 County Rd 10, Moose Lake, MN 55767",
            "phone": "(218) 485-4435",
            "website": "https://www.ml115.org/",
            "students": 350
        }
    ],
    "Mora Public School District": [
        {
            "school_name": "Mora Elementary School",
            "address": "200 9th St N, Mora, MN 55051",
            "phone": "(320) 679-6200",
            "website": "https://www.moraschools.org/",
            "students": 600
        },
        {
            "school_name": "Mora Secondary School",
            "address": "400 Burg St E, Mora, MN 55051",
            "phone": "(320) 679-6200",
            "website": "https://www.moraschools.org/",
            "students": 700
        }
    ],
    "Morris Area Public Schools": [
        {
            "school_name": "Morris Area Elementary School",
            "address": "151 S Columbia Ave, Morris, MN 56267",
            "phone": "(320) 589-1250",
            "website": "https://www.morris.k12.mn.us/",
            "students": 400
        },
        {
            "school_name": "Morris Area Secondary School",
            "address": "201 S Columbia Ave, Morris, MN 56267",
            "phone": "(320) 589-4400",
            "website": "https://www.morris.k12.mn.us/",
            "students": 500
        }
    ],
    "Mounds View Public School District": [
        {
            "school_name": "Mounds View Elementary Schools",
            "address": "Various locations, Mounds View, MN 55112",
            "phone": "(651) 621-6000",
            "website": "https://www.moundsviewschools.org/",
            "students": 3000
        },
        {
            "school_name": "Mounds View Middle Schools",
            "address": "Various locations, Mounds View, MN 55112",
            "phone": "(651) 621-6000",
            "website": "https://www.moundsviewschools.org/",
            "students": 2000
        },
        {
            "school_name": "Mounds View High School",
            "address": "1900 Lake Valentine Rd, Arden Hills, MN 55112",
            "phone": "(651) 621-7000",
            "website": "https://www.moundsviewschools.org/",
            "students": 2100
        }
    ],
    "Mountain Iron-Buhl School District": [
        {
            "school_name": "Mountain Iron-Buhl Elementary School",
            "address": "8285 Rock Ridge Rd, Mt Iron, MN 55768",
            "phone": "(218) 735-1762",
            "website": "https://www.mib.k12.mn.us/",
            "students": 318
        },
        {
            "school_name": "Mountain Iron-Buhl Secondary School",
            "address": "8285 Rock Ridge Rd, Mt Iron, MN 55768",
            "phone": "(218) 735-1762",
            "website": "https://www.mib.k12.mn.us/",
            "students": 300
        }
    ],
    "Mountain Lake Public Schools": [
        {
            "school_name": "Mountain Lake Elementary School",
            "address": "700 11th St N, Mountain Lake, MN 56159",
            "phone": "(507) 427-2325",
            "website": "https://www.mountainlake.k12.mn.us/",
            "students": 250
        },
        {
            "school_name": "Mountain Lake Secondary School",
            "address": "700 11th St N, Mountain Lake, MN 56159",
            "phone": "(507) 427-2325",
            "website": "https://www.mountainlake.k12.mn.us/",
            "students": 200
        }
    ],
    "Murray County Central School Dist.": [
        {
            "school_name": "Murray County Central Elementary School",
            "address": "723 E College Dr, Slayton, MN 56172",
            "phone": "(507) 836-6181",
            "website": "https://www.mcc764.org/",
            "students": 300
        },
        {
            "school_name": "Murray County Central Secondary School",
            "address": "3305 N Redwood Ave, Slayton, MN 56172",
            "phone": "(507) 836-6181",
            "website": "https://www.mcc764.org/",
            "students": 350
        }
    ],
    "Nasha Shkola Charter School": [
        {
            "school_name": "Nasha Shkola Charter School",
            "address": "5701 83rd St W, Brooklyn Park, MN 55429",
            "phone": "(763) 496-7000",
            "website": "https://nashashkola.org/",
            "students": 200
        }
    ],
    "Nashwauk-Keewatin School District": [
        {
            "school_name": "Nashwauk-Keewatin Elementary School",
            "address": "305 Central Ave, Nashwauk, MN 55769",
            "phone": "(218) 885-1280",
            "website": "https://www.isd319.org/",
            "students": 150
        },
        {
            "school_name": "Nashwauk-Keewatin Secondary School",
            "address": "305 Central Ave, Nashwauk, MN 55769",
            "phone": "(218) 885-1280",
            "website": "https://www.isd319.org/",
            "students": 200
        }
    ],
    "Natural Science Academy": [
        {
            "school_name": "Natural Science Academy",
            "address": "1668 Montreal Ave, St Paul, MN 55116",
            "phone": "(651) 925-5277",
            "website": "https://naturalscienceacademy.org/",
            "students": 300
        }
    ],
    "Nay-Ah-Shing School": [
        {
            "school_name": "Nay-Ah-Shing School",
            "address": "33924 Nay-Ah-Shing Blvd, Onamia, MN 56359",
            "phone": "(320) 532-3249",
            "website": "https://nayahshing.org/",
            "students": 150
        }
    ],
    "Naytahwaush Community School": [
        {
            "school_name": "Naytahwaush Community School",
            "address": "9238 School Ave, Naytahwaush, MN 56566",
            "phone": "(218) 935-5854",
            "website": "https://www.naytahwaush.org/",
            "students": 100
        }
    ],
    "Nerstrand Charter School": [
        {
            "school_name": "Nerstrand Elementary School",
            "address": "205 S 2nd St, Nerstrand, MN 55053",
            "phone": "(507) 333-6850",
            "website": "https://nerstrandcharterschool.org/",
            "students": 200
        }
    ],
    "Nett Lake Public School District": [
        {
            "school_name": "Nett Lake Elementary School",
            "address": "13090 Westley Dr, Nett Lake, MN 55772",
            "phone": "(218) 757-3733",
            "website": "https://nettlake.mn.idc.k12.mn.us/",
            "students": 100
        }
    ],
    "Nevis Public School District": [
        {
            "school_name": "Nevis Elementary School",
            "address": "21197 Tulaby Rd NE, Nevis, MN 56467",
            "phone": "(218) 652-3500",
            "website": "https://www.nevis.k12.mn.us/",
            "students": 250
        },
        {
            "school_name": "Nevis Secondary School",
            "address": "21197 Tulaby Rd NE, Nevis, MN 56467",
            "phone": "(218) 652-3500",
            "website": "https://www.nevis.k12.mn.us/",
            "students": 200
        }
    ],
    "New Century Charter School": [
        {
            "school_name": "New Century Charter School",
            "address": "1380 Energy Ln, St Paul, MN 55108",
            "phone": "(651) 209-8912",
            "website": "https://newcenturyschool.org/",
            "students": 150
        }
    ],
    "New Century School": [
        {
            "school_name": "New Century School",
            "address": "1380 Energy Ln, St Paul, MN 55108",
            "phone": "(651) 209-8912",
            "website": "https://newcenturyschool.org/",
            "students": 150
        }
    ],
    "New City School": [
        {
            "school_name": "New City School",
            "address": "1789 Woodlane Dr, Woodbury, MN 55125",
            "phone": "(651) 209-8800",
            "website": "https://newcitycharterschool.org/",
            "students": 300
        }
    ],
    "New Discoveries Montessori Academy": [
        {
            "school_name": "New Discoveries Montessori Academy",
            "address": "616 Girard Ter N, Minneapolis, MN 55411",
            "phone": "(612) 285-7184",
            "website": "https://newdiscoveries.org/",
            "students": 200
        }
    ],
    "New Heights School Inc.": [
        {
            "school_name": "New Heights School",
            "address": "614 W 49th St, Minneapolis, MN 55419",
            "phone": "(612) 355-4672",
            "website": "https://www.newheightsschool.org/",
            "students": 150
        }
    ],
    "New London-Spicer School District": [
        {
            "school_name": "New London-Spicer Elementary School",
            "address": "101 4th Ave SW, New London, MN 56273",
            "phone": "(320) 354-2252",
            "website": "https://www.nls.k12.mn.us/",
            "students": 500
        },
        {
            "school_name": "New London-Spicer Secondary School",
            "address": "101 4th Ave SW, New London, MN 56273",
            "phone": "(320) 354-2252",
            "website": "https://www.nls.k12.mn.us/",
            "students": 600
        }
    ],
    "New Millennium Academy Charter School": [
        {
            "school_name": "New Millennium Academy Charter School",
            "address": "3300 Century Ave N, White Bear Lake, MN 55110",
            "phone": "(651) 407-7559",
            "website": "https://newmillenniumacademy.org/",
            "students": 300
        }
    ],
    "New Prague Area Schools": [
        {
            "school_name": "New Prague Elementary Schools",
            "address": "Various locations, New Prague, MN 56071",
            "phone": "(952) 758-1700",
            "website": "https://www.npaschools.org/",
            "students": 1500
        },
        {
            "school_name": "New Prague Middle School",
            "address": "721 Central Ave N, New Prague, MN 56071",
            "phone": "(952) 758-1600",
            "website": "https://www.npaschools.org/",
            "students": 800
        },
        {
            "school_name": "New Prague High School",
            "address": "221 12th St NE, New Prague, MN 56071",
            "phone": "(952) 758-1500",
            "website": "https://www.npaschools.org/",
            "students": 1100
        }
    ],
    "New Ulm Public School District": [
        {
            "school_name": "New Ulm Elementary Schools",
            "address": "Various locations, New Ulm, MN 56073",
            "phone": "(507) 233-1703",
            "website": "https://www.newulm.k12.mn.us/",
            "students": 1200
        },
        {
            "school_name": "New Ulm Middle School",
            "address": "900 N Garden St, New Ulm, MN 56073",
            "phone": "(507) 233-1700",
            "website": "https://www.newulm.k12.mn.us/",
            "students": 600
        },
        {
            "school_name": "New Ulm High School",
            "address": "1 Lincoln St, New Ulm, MN 56073",
            "phone": "(507) 233-1700",
            "website": "https://www.newulm.k12.mn.us/",
            "students": 900
        }
    ],
    "New York Mills Public School Dist.": [
        {
            "school_name": "New York Mills Elementary School",
            "address": "209 Hayes St, New York Mills, MN 56567",
            "phone": "(218) 385-4201",
            "website": "https://www.ny-mills.k12.mn.us/",
            "students": 300
        },
        {
            "school_name": "New York Mills Secondary School",
            "address": "209 Hayes St, New York Mills, MN 56567",
            "phone": "(218) 385-4201",
            "website": "https://www.ny-mills.k12.mn.us/",
            "students": 250
        }
    ],
    "Nicollet Public School District": [
        {
            "school_name": "Nicollet Elementary School",
            "address": "501 Pine St, Nicollet, MN 56074",
            "phone": "(507) 232-3411",
            "website": "https://www.nicollet.k12.mn.us/",
            "students": 200
        },
        {
            "school_name": "Nicollet Secondary School",
            "address": "501 Pine St, Nicollet, MN 56074",
            "phone": "(507) 232-3411",
            "website": "https://www.nicollet.k12.mn.us/",
            "students": 150
        }
    ],
    "Noble Academy": [
        {
            "school_name": "Noble Academy",
            "address": "9477 Karen Ln N, Osseo, MN 55369",
            "phone": "(763) 315-7600",
            "website": "https://nobleacademymn.com/",
            "students": 200
        }
    ],
    "Norman County East School District": [
        {
            "school_name": "Norman County East Elementary School",
            "address": "301 Elk St, Twin Valley, MN 56584",
            "phone": "(218) 584-5151",
            "website": "https://www.norman.k12.mn.us/",
            "students": 150
        },
        {
            "school_name": "Norman County East Secondary School",
            "address": "301 Elk St, Twin Valley, MN 56584",
            "phone": "(218) 584-5151",
            "website": "https://www.norman.k12.mn.us/",
            "students": 200
        }
    ],
    "Norman County West School District": [
        {
            "school_name": "Norman County West Elementary School",
            "address": "411 Elk St, Hendrum, MN 56550",
            "phone": "(218) 861-6670",
            "website": "https://www.ncwest.k12.mn.us/",
            "students": 100
        },
        {
            "school_name": "Norman County West Secondary School",
            "address": "411 Elk St, Hendrum, MN 56550",
            "phone": "(218) 861-6670",
            "website": "https://www.ncwest.k12.mn.us/",
            "students": 150
        }
    ],
    "North Branch Public Schools": [
        {
            "school_name": "North Branch Elementary Schools",
            "address": "Various locations, North Branch, MN 55056",
            "phone": "(651) 674-1000",
            "website": "https://www.nbranch.k12.mn.us/",
            "students": 1500
        },
        {
            "school_name": "North Branch Middle School",
            "address": "38432 Lincoln Trl, North Branch, MN 55056",
            "phone": "(651) 674-1050",
            "website": "https://www.nbranch.k12.mn.us/",
            "students": 800
        },
        {
            "school_name": "North Branch High School",
            "address": "38175 Grand Ave, North Branch, MN 55056",
            "phone": "(651) 674-1100",
            "website": "https://www.nbranch.k12.mn.us/",
            "students": 1200
        }
    ],
    "North Country Voc. Cooperative Center": [
        {
            "school_name": "North Country Vocational Cooperative Center",
            "address": "1850 White Pine Dr, Chisholm, MN 55719",
            "phone": "(218) 254-5181",
            "website": "https://www.ncvcc.com/",
            "students": 500
        }
    ],
    "North Lakes Academy": [
        {
            "school_name": "North Lakes Academy",
            "address": "7230 Boone Ave N, Brooklyn Park, MN 55428",
            "phone": "(763) 971-8991",
            "website": "https://northlakesacademy.org/",
            "students": 300
        }
    ],
    "North Metro Flex Academy": [
        {
            "school_name": "North Metro Flex Academy",
            "address": "1818 Riverwood Dr, Burnsville, MN 55337",
            "phone": "(952) 707-4800",
            "website": "https://northmetroflex.org/",
            "students": 200
        }
    ],
    "North Shore Community School": [
        {
            "school_name": "North Shore Community School",
            "address": "5926 Ryan Rd, Duluth, MN 55804",
            "phone": "(218) 525-0663",
            "website": "https://northshorecommunityschool.org/",
            "students": 150
        }
    ],
    "North St Paul-Maplewood School Dist": [
        {
            "school_name": "North St. Paul Elementary Schools",
            "address": "Various locations, North St. Paul, MN 55109",
            "phone": "(651) 748-7100",
            "website": "https://www.isd622.org/",
            "students": 2500
        },
        {
            "school_name": "North St. Paul Middle Schools",
            "address": "Various locations, North St. Paul, MN 55109",
            "phone": "(651) 748-7100",
            "website": "https://www.isd622.org/",
            "students": 1800
        },
        {
            "school_name": "North St. Paul High Schools",
            "address": "Various locations, North St. Paul, MN 55109",
            "phone": "(651) 748-7100",
            "website": "https://www.isd622.org/",
            "students": 2000
        }
    ],
    "Northeast Art And Science Polytechn": [
        {
            "school_name": "Northeast Art and Science Polytechnic",
            "address": "1305 5th St NE, Minneapolis, MN 55413",
            "phone": "(612) 728-5728",
            "website": "https://www.neasp.org/",
            "students": 200
        }
    ],
    "Northeast College Prep": [
        {
            "school_name": "Northeast College Prep",
            "address": "300 Industrial Blvd NE, Minneapolis, MN 55413",
            "phone": "(612) 248-8470",
            "website": "https://northeastcollegeprep.org/",
            "students": 150
        }
    ],
    "Northeast Metro 916 School District": [
        {
            "school_name": "Northeast Metro 916 Intermediate District",
            "address": "2670 Shady View Ln, Hugo, MN 55038",
            "phone": "(651) 415-5600",
            "website": "https://nemetro.k12.mn.us/",
            "students": 1000
        }
    ],
    "Northern Lights Academy Cooperative": [
        {
            "school_name": "Northern Lights Academy Cooperative",
            "address": "1915 Cty Rd 24, Shevlin, MN 56676",
            "phone": "(218) 785-4037",
            "website": "https://www.nlacoop.org/",
            "students": 100
        }
    ],
    "Northern Lights Community School": [
        {
            "school_name": "Northern Lights Community School",
            "address": "1909 Wayzata Blvd, Long Lake, MN 55356",
            "phone": "(952) 491-4499",
            "website": "https://northernlightscommunityschool.org/",
            "students": 150
        }
    ],
    "Northfield Public School District": [
        {
            "school_name": "Northfield Elementary Schools",
            "address": "Various locations, Northfield, MN 55057",
            "phone": "(507) 663-0600",
            "website": "https://northfieldschools.org/",
            "students": 1800
        },
        {
            "school_name": "Northfield Middle School",
            "address": "2200 Division St S, Northfield, MN 55057",
            "phone": "(507) 663-0668",
            "website": "https://northfieldschools.org/",
            "students": 1000
        },
        {
            "school_name": "Northfield High School",
            "address": "1400 Division St S, Northfield, MN 55057",
            "phone": "(507) 663-0630",
            "website": "https://northfieldschools.org/",
            "students": 1200
        }
    ],
    "Northland Community Schools": [
        {
            "school_name": "Northland Community Schools",
            "address": "1348 Kyllo Rd NW, Cass Lake, MN 56633",
            "phone": "(218) 335-8400",
            "website": "https://www.northlandcommunityschools.org/",
            "students": 300
        }
    ],
    "Northland Learning Center": [
        {
            "school_name": "Northland Learning Center",
            "address": "1667 Snelling Ave N, St Paul, MN 55108",
            "phone": "(651) 209-8384",
            "website": "https://northlandlc.org/",
            "students": 100
        }
    ],
    "Northwest Passage High School": [
        {
            "school_name": "Northwest Passage High School",
            "address": "200 Bloomington Ave S, Minneapolis, MN 55425",
            "phone": "(612) 843-5050",
            "website": "https://www.nwphs.org/",
            "students": 200
        }
    ],
    "Nova Classical Academy": [
        {
            "school_name": "Nova Classical Academy",
            "address": "1455 Victoria Park Dr, St Paul, MN 55117",
            "phone": "(651) 209-6320",
            "website": "https://www.novaclassical.org/",
            "students": 600
        }
    ],
    "Nrheg School District": [
        {
            "school_name": "NRHEG Elementary School",
            "address": "600 School St, New Richland, MN 56072",
            "phone": "(507) 465-3206",
            "website": "https://www.nrheg.k12.mn.us/",
            "students": 300
        },
        {
            "school_name": "NRHEG Secondary School",
            "address": "600 School St, New Richland, MN 56072",
            "phone": "(507) 465-3206",
            "website": "https://www.nrheg.k12.mn.us/",
            "students": 350
        }
    ],
    "Nw Region Interdistrict Council": [
        {
            "school_name": "Northwest Regional Interdistrict Council",
            "address": "114 W 1st St, Thief River Falls, MN 56701",
            "phone": "(218) 681-0900",
            "website": "https://www.nw-service.k12.mn.us/",
            "students": 500
        }
    ],
    "Odaa Academy of Science and Technol": [
        {
            "school_name": "Odaa Academy of Science and Technology",
            "address": "1025 Morgan Ave N, Minneapolis, MN 55411",
            "phone": "(612) 396-8885",
            "website": "https://odaacademy.org/",
            "students": 150
        }
    ],
    "Odyssey Academy": [
        {
            "school_name": "Odyssey Academy",
            "address": "1350 Englewood Ave, St Paul, MN 55104",
            "phone": "(651) 209-8384",
            "website": "https://odysseyacademy.org/",
            "students": 200
        }
    ],
    "Ogilvie Public School District": [
        {
            "school_name": "Ogilvie Elementary School",
            "address": "333 School Dr, Ogilvie, MN 56358",
            "phone": "(320) 272-5200",
            "website": "https://www.ogilvie.k12.mn.us/",
            "students": 250
        },
        {
            "school_name": "Ogilvie Secondary School",
            "address": "333 School Dr, Ogilvie, MN 56358",
            "phone": "(320) 272-5200",
            "website": "https://www.ogilvie.k12.mn.us/",
            "students": 200
        }
    ],
    "Onamia Public School District": [
        {
            "school_name": "Onamia Elementary School",
            "address": "35963 City St, Onamia, MN 56359",
            "phone": "(320) 532-3133",
            "website": "https://www.onamia.k12.mn.us/",
            "students": 200
        },
        {
            "school_name": "Onamia Secondary School",
            "address": "35963 City St, Onamia, MN 56359",
            "phone": "(320) 532-3133",
            "website": "https://www.onamia.k12.mn.us/",
            "students": 150
        }
    ],
    "Orono Public School District": [
        {
            "school_name": "Orono Elementary Schools",
            "address": "Various locations, Orono, MN 55356",
            "phone": "(952) 476-1000",
            "website": "https://www.orono.k12.mn.us/",
            "students": 1500
        },
        {
            "school_name": "Orono Middle School",
            "address": "1285 Duluth St, Long Lake, MN 55356",
            "phone": "(952) 476-2003",
            "website": "https://www.orono.k12.mn.us/",
            "students": 800
        },
        {
            "school_name": "Orono High School",
            "address": "795 Old Crystal Bay Rd N, Long Lake, MN 55356",
            "phone": "(952) 476-2003",
            "website": "https://www.orono.k12.mn.us/",
            "students": 1300
        }
    ],
    "Ortonville Public Schools": [
        {
            "school_name": "Ortonville Elementary School",
            "address": "200 3rd St NW, Ortonville, MN 56278",
            "phone": "(320) 839-6181",
            "website": "https://www.ortonville.k12.mn.us/",
            "students": 250
        },
        {
            "school_name": "Ortonville Secondary School",
            "address": "200 3rd St NW, Ortonville, MN 56278",
            "phone": "(320) 839-6181",
            "website": "https://www.ortonville.k12.mn.us/",
            "students": 200
        }
    ],
    "Osakis Public School District": [
        {
            "school_name": "Osakis Elementary School",
            "address": "500 17th Ave W, Osakis, MN 56360",
            "phone": "(320) 859-2192",
            "website": "https://www.osakis.k12.mn.us/",
            "students": 300
        },
        {
            "school_name": "Osakis Secondary School",
            "address": "500 17th Ave W, Osakis, MN 56360",
            "phone": "(320) 859-2192",
            "website": "https://www.osakis.k12.mn.us/",
            "students": 250
        }
    ],
    "Oshki Ogimaag Charter School": [
        {
            "school_name": "Oshki Ogimaag Charter School",
            "address": "1401 Fairview Ave N, Grand Rapids, MN 55744",
            "phone": "(218) 999-9030",
            "website": "https://oshkiogimaag.org/",
            "students": 100
        }
    ],
    "Osseo Public School District": [
        {
            "school_name": "Osseo Elementary Schools",
            "address": "Various locations, Osseo, MN 55369",
            "phone": "(763) 391-7000",
            "website": "https://www.district279.org/",
            "students": 10000
        },
        {
            "school_name": "Osseo Middle Schools",
            "address": "Various locations, Osseo, MN 55369",
            "phone": "(763) 391-7000",
            "website": "https://www.district279.org/",
            "students": 6000
        },
        {
            "school_name": "Osseo High Schools",
            "address": "Various locations, Osseo, MN 55369",
            "phone": "(763) 391-7000",
            "website": "https://www.district279.org/",
            "students": 7000
        }
    ],
    "Owatonna Public School District": [
        {
            "school_name": "Owatonna Elementary Schools",
            "address": "Various locations, Owatonna, MN 55060",
            "phone": "(507) 444-8600",
            "website": "https://www.owatonna.k12.mn.us/",
            "students": 2000
        },
        {
            "school_name": "Owatonna Middle School",
            "address": "333 E School St, Owatonna, MN 55060",
            "phone": "(507) 444-8600",
            "website": "https://www.owatonna.k12.mn.us/",
            "students": 1000
        },
        {
            "school_name": "Owatonna High School",
            "address": "333 E School St, Owatonna, MN 55060",
            "phone": "(507) 444-8900",
            "website": "https://www.owatonna.k12.mn.us/",
            "students": 1800
        }
    ],
    "Pact Charter School": [
        {
            "school_name": "PACT Charter School",
            "address": "7250 E Ramsey Parkway, Ramsey, MN 55303",
            "phone": "(763) 712-4200",
            "website": "https://pact.charter.k12.mn.us/",
            "students": 686
        }
    ],
    "Paladin Career & Technical High School": [
        {
            "school_name": "Paladin Career & Technical High School",
            "address": "7076 Stillwater Blvd N, Oakdale, MN 55128",
            "phone": "(651) 379-4200",
            "website": "https://paladincareertech.com/",
            "students": 300
        }
    ],
    "Park Rapids Public School District": [
        {
            "school_name": "Park Rapids Elementary School",
            "address": "800 Park Ave, Park Rapids, MN 56470",
            "phone": "(218) 237-6300",
            "website": "https://www.parkrapids.k12.mn.us/",
            "students": 600
        },
        {
            "school_name": "Park Rapids Secondary School",
            "address": "801 Henrietta Ave N, Park Rapids, MN 56470",
            "phone": "(218) 237-6400",
            "website": "https://www.parkrapids.k12.mn.us/",
            "students": 700
        }
    ],
    "Parkers Prairie Public School Dist.": [
        {
            "school_name": "Parkers Prairie Elementary School",
            "address": "305 W Main St, Parkers Prairie, MN 56361",
            "phone": "(218) 338-6541",
            "website": "https://www.parkersprairie.k12.mn.us/",
            "students": 200
        },
        {
            "school_name": "Parkers Prairie Secondary School",
            "address": "305 W Main St, Parkers Prairie, MN 56361",
            "phone": "(218) 338-6541",
            "website": "https://www.parkersprairie.k12.mn.us/",
            "students": 150
        }
    ],
    "Parnassus Preparatory Charter School": [
        {
            "school_name": "Parnassus Preparatory Charter School",
            "address": "11201 96th St N, Maple Grove, MN 55369",
            "phone": "(763) 496-1416",
            "website": "https://www.parnassus.info/",
            "students": 1200
        }
    ],
    "Partnership Academy Inc.": [
        {
            "school_name": "Partnership Academy",
            "address": "6500 Pillsbury Ave S, Richfield, MN 55423",
            "phone": "(612) 866-0816",
            "website": "https://www.partnershipacademy.com/",
            "students": 150
        }
    ],
    "Paynesville Public School District": [
        {
            "school_name": "Paynesville Elementary School",
            "address": "24936 Peregrine St, Paynesville, MN 56362",
            "phone": "(320) 243-3734",
            "website": "https://www.paynesvilleschools.com/",
            "students": 400
        },
        {
            "school_name": "Paynesville Secondary School",
            "address": "24936 Peregrine St, Paynesville, MN 56362",
            "phone": "(320) 243-3734",
            "website": "https://www.paynesvilleschools.com/",
            "students": 350
        }
    ],
    "Pelican Rapids Public School Dist.": [
        {
            "school_name": "Pelican Rapids Elementary School",
            "address": "310 S Broadway, Pelican Rapids, MN 56572",
            "phone": "(218) 863-5910",
            "website": "https://www.pelicandistrictschools.org/",
            "students": 300
        },
        {
            "school_name": "Pelican Rapids Secondary School",
            "address": "310 S Broadway, Pelican Rapids, MN 56572",
            "phone": "(218) 863-5910",
            "website": "https://www.pelicandistrictschools.org/",
            "students": 250
        }
    ],
    "Pequot Lakes Public Schools": [
        {
            "school_name": "Pequot Lakes Elementary School",
            "address": "30525 Patriot Ave, Pequot Lakes, MN 56472",
            "phone": "(218) 568-9500",
            "website": "https://www.pequotlakes.k12.mn.us/",
            "students": 600
        },
        {
            "school_name": "Pequot Lakes Middle School",
            "address": "30525 Patriot Ave, Pequot Lakes, MN 56472",
            "phone": "(218) 568-9500",
            "website": "https://www.pequotlakes.k12.mn.us/",
            "students": 400
        },
        {
            "school_name": "Pequot Lakes High School",
            "address": "30525 Patriot Ave, Pequot Lakes, MN 56472",
            "phone": "(218) 568-9500",
            "website": "https://www.pequotlakes.k12.mn.us/",
            "students": 500
        }
    ],
    "Perham-Dent Public School District": [
        {
            "school_name": "Perham-Dent Elementary Schools",
            "address": "Various locations, Perham, MN 56573",
            "phone": "(218) 346-6500",
            "website": "https://www.perham.k12.mn.us/",
            "students": 700
        },
        {
            "school_name": "Perham-Dent Secondary School",
            "address": "800 Coney St W, Perham, MN 56573",
            "phone": "(218) 346-1780",
            "website": "https://www.perham.k12.mn.us/",
            "students": 600
        }
    ],
    "Perpich Center For Arts Education": [
        {
            "school_name": "Perpich Arts High School",
            "address": "6125 Olson Memorial Hwy, Golden Valley, MN 55422",
            "phone": "(763) 591-4700",
            "website": "https://perpich.mn.gov/",
            "students": 200
        }
    ],
    "Pete Seeger Renaissance Charter Sch": [
        {
            "school_name": "Pete Seeger Renaissance Charter School",
            "address": "1600 Hampden Ave, St Paul, MN 55116",
            "phone": "(651) 639-9700",
            "website": "https://www.peteseegeracademy.org/",
            "students": 150
        }
    ],
    "Phoenix Academy Charter School": [
        {
            "school_name": "Phoenix Academy Charter School",
            "address": "1305 E 35th St, Minneapolis, MN 55407",
            "phone": "(612) 259-6732",
            "website": "https://phoenixacademymn.org/",
            "students": 100
        }
    ],
    "Pierz Public School District": [
        {
            "school_name": "Pierz Elementary School",
            "address": "412 Kamenic St, Pierz, MN 56364",
            "phone": "(320) 468-6458",
            "website": "https://www.pierz.k12.mn.us/",
            "students": 400
        },
        {
            "school_name": "Pierz Secondary School",
            "address": "412 Kamenic St, Pierz, MN 56364",
            "phone": "(320) 468-6458",
            "website": "https://www.pierz.k12.mn.us/",
            "students": 350
        }
    ],
    "Pillager Area Charter School": [
        {
            "school_name": "Pillager Area Charter School",
            "address": "8459 Brockett Rd, Pillager, MN 56473",
            "phone": "(218) 746-2300",
            "website": "https://www.pillagerschools.com/",
            "students": 200
        }
    ],
    "Pillager Public School District": [
        {
            "school_name": "Pillager Elementary School",
            "address": "115 2nd St W, Pillager, MN 56473",
            "phone": "(218) 746-2001",
            "website": "https://www.pillagerschools.com/",
            "students": 400
        },
        {
            "school_name": "Pillager Secondary School",
            "address": "115 2nd St W, Pillager, MN 56473",
            "phone": "(218) 746-2001",
            "website": "https://www.pillagerschools.com/",
            "students": 300
        }
    ],
    "PIM Arts High School": [
        {
            "school_name": "PIM Arts High School",
            "address": "1667 Snelling Ave N, St Paul, MN 55108",
            "phone": "(651) 209-8384",
            "website": "https://pimartshs.org/",
            "students": 150
        }
    ],
    "Pine City Public School District": [
        {
            "school_name": "Pine City Elementary School",
            "address": "700 6th St SW, Pine City, MN 55063",
            "phone": "(320) 629-4200",
            "website": "https://www.pinecity.k12.mn.us/",
            "students": 600
        },
        {
            "school_name": "Pine City Secondary School",
            "address": "700 6th St SW, Pine City, MN 55063",
            "phone": "(320) 629-4200",
            "website": "https://www.pinecity.k12.mn.us/",
            "students": 500
        }
    ],
    "Pine Island Public School Dist.": [
        {
            "school_name": "Pine Island Elementary School",
            "address": "223 1st Ave SE, Pine Island, MN 55963",
            "phone": "(507) 356-8581",
            "website": "https://www.pineisland.k12.mn.us/",
            "students": 500
        },
        {
            "school_name": "Pine Island Secondary School",
            "address": "223 1st Ave SE, Pine Island, MN 55963",
            "phone": "(507) 356-8581",
            "website": "https://www.pineisland.k12.mn.us/",
            "students": 400
        }
    ],
    "Pine Point Public School District": [
        {
            "school_name": "Pine Point Elementary School",
            "address": "1400 81st Ave NE, Blaine, MN 55434",
            "phone": "(763) 600-5920",
            "website": "https://www.pinepointschool.org/",
            "students": 300
        }
    ],
    "Pine River-Backus School District": [
        {
            "school_name": "Pine River-Backus Elementary School",
            "address": "24888 Govnr Rd, Pine River, MN 56474",
            "phone": "(218) 587-4427",
            "website": "https://www.prbschools.org/",
            "students": 400
        },
        {
            "school_name": "Pine River-Backus Secondary School",
            "address": "24888 Govnr Rd, Pine River, MN 56474",
            "phone": "(218) 587-4427",
            "website": "https://www.prbschools.org/",
            "students": 350
        }
    ],
    "Pine To Prairie Cooperative Center": [
        {
            "school_name": "Pine to Prairie Cooperative Center",
            "address": "1405 3rd Ave NE, Crookston, MN 56716",
            "phone": "(218) 281-3720",
            "website": "https://www.pinetoprairie.com/",
            "students": 200
        }
    ],
    "Pipestone Area School District": [
        {
            "school_name": "Pipestone Area Elementary School",
            "address": "1501 7th St SW, Pipestone, MN 56164",
            "phone": "(507) 825-5858",
            "website": "https://www.pas.k12.mn.us/",
            "students": 500
        },
        {
            "school_name": "Pipestone Area Secondary School",
            "address": "1401 7th St SW, Pipestone, MN 56164",
            "phone": "(507) 825-5858",
            "website": "https://www.pas.k12.mn.us/",
            "students": 400
        }
    ],
    "Plainview-Elgin-Millville School District": [
        {
            "school_name": "Plainview-Elgin-Millville Elementary School",
            "address": "500 W Broadway St, Plainview, MN 55964",
            "phone": "(507) 534-3281",
            "website": "https://www.pem.k12.mn.us/",
            "students": 600
        },
        {
            "school_name": "Plainview-Elgin-Millville Secondary School",
            "address": "500 W Broadway St, Plainview, MN 55964",
            "phone": "(507) 534-3281",
            "website": "https://www.pem.k12.mn.us/",
            "students": 500
        }
    ],
    "Prairie Creek Community School": [
        {
            "school_name": "Prairie Creek Community School",
            "address": "7180 Winnetka Ave N, Brooklyn Park, MN 55428",
            "phone": "(763) 600-5415",
            "website": "https://www.prairiecreek.org/",
            "students": 200
        }
    ],
    "Prairie Seeds Academy": [
        {
            "school_name": "Prairie Seeds Academy",
            "address": "6200 W Arrowhead Rd, Brooklyn Center, MN 55429",
            "phone": "(763) 391-9800",
            "website": "https://prairieseedsmn.org/",
            "students": 300
        }
    ],
    "Princeton Public School District": [
        {
            "school_name": "Princeton Elementary Schools",
            "address": "Various locations, Princeton, MN 55371",
            "phone": "(763) 389-6721",
            "website": "https://www.isd477.org/",
            "students": 1000
        },
        {
            "school_name": "Princeton Middle School",
            "address": "800 7th Ave N, Princeton, MN 55371",
            "phone": "(763) 389-6721",
            "website": "https://www.isd477.org/",
            "students": 600
        },
        {
            "school_name": "Princeton High School",
            "address": "807 Eighth Ave N, Princeton, MN 55371",
            "phone": "(763) 389-6721",
            "website": "https://www.isd477.org/",
            "students": 800
        }
    ],
    "Prior Lake-Savage Area Schools": [
        {
            "school_name": "Prior Lake-Savage Elementary Schools",
            "address": "Various locations, Prior Lake, MN 55372",
            "phone": "(952) 226-0000",
            "website": "https://www.priorlake-savage.k12.mn.us/",
            "students": 4000
        },
        {
            "school_name": "Prior Lake-Savage Middle Schools",
            "address": "Various locations, Prior Lake, MN 55372",
            "phone": "(952) 226-0000",
            "website": "https://www.priorlake-savage.k12.mn.us/",
            "students": 2500
        },
        {
            "school_name": "Prior Lake High School",
            "address": "7575 150th St W, Savage, MN 55378",
            "phone": "(952) 226-8600",
            "website": "https://www.priorlake-savage.k12.mn.us/",
            "students": 2200
        }
    ],
    "Proctor Public School District": [
        {
            "school_name": "Proctor Elementary Schools",
            "address": "Various locations, Proctor, MN 55810",
            "phone": "(218) 628-4926",
            "website": "https://www.proctor.k12.mn.us/",
            "students": 800
        },
        {
            "school_name": "Proctor Middle School",
            "address": "301 Fairview Ave, Proctor, MN 55810",
            "phone": "(218) 628-4926",
            "website": "https://www.proctor.k12.mn.us/",
            "students": 400
        },
        {
            "school_name": "Proctor High School",
            "address": "131 Burton St, Proctor, MN 55810",
            "phone": "(218) 628-4926",
            "website": "https://www.proctor.k12.mn.us/",
            "students": 600
        }
    ],
    "Prodeo Academy": [
        {
            "school_name": "Prodeo Academy",
            "address": "5201 33rd Ave S, Minneapolis, MN 55417",
            "phone": "(612) 293-4008",
            "website": "https://prodeoacademy.org/",
            "students": 200
        }
    ],
    "Progeny Academy Charter School": [
        {
            "school_name": "Progeny Academy Charter School",
            "address": "4857 Bloomington Ave, Minneapolis, MN 55419",
            "phone": "(612) 722-9013",
            "website": "https://www.progenyacademy.org/",
            "students": 100
        }
    ],
    "Quantum STEAM Academy Charter School": [
        {
            "school_name": "Quantum STEAM Academy Charter School",
            "address": "1515 Brewster St, St Paul, MN 55108",
            "phone": "(651) 379-9900",
            "website": "https://quantumsteamacademy.org/",
            "students": 150
        }
    ],
    "Randolph Public School District": [
        {
            "school_name": "Randolph Elementary School",
            "address": "25853 Elm St, Randolph, MN 55065",
            "phone": "(507) 263-2171",
            "website": "https://www.randolph.k12.mn.us/",
            "students": 300
        },
        {
            "school_name": "Randolph Secondary School",
            "address": "25853 Elm St, Randolph, MN 55065",
            "phone": "(507) 263-2171",
            "website": "https://www.randolph.k12.mn.us/",
            "students": 200
        }
    ],
    "Red Lake County Central Public Sch": [
        {
            "school_name": "Red Lake County Central Elementary School",
            "address": "610 7th St NW, Red Lake Falls, MN 56750",
            "phone": "(218) 253-2163",
            "website": "https://www.redlakecentralschools.org/",
            "students": 300
        },
        {
            "school_name": "Red Lake County Central Secondary School",
            "address": "610 7th St NW, Red Lake Falls, MN 56750",
            "phone": "(218) 253-2163",
            "website": "https://www.redlakecentralschools.org/",
            "students": 350
        }
    ],
    "Red Lake Falls Public School Dist.": [
        {
            "school_name": "Red Lake Falls Elementary School",
            "address": "505 Parke Ave SW, Red Lake Falls, MN 56750",
            "phone": "(218) 253-2959",
            "website": "https://www.redlakefalls.k12.mn.us/",
            "students": 200
        },
        {
            "school_name": "Red Lake Falls Secondary School",
            "address": "505 Parke Ave SW, Red Lake Falls, MN 56750",
            "phone": "(218) 253-2959",
            "website": "https://www.redlakefalls.k12.mn.us/",
            "students": 150
        }
    ],
    "Red Lake Public School District": [
        {
            "school_name": "Red Lake Elementary Schools",
            "address": "Various locations, Red Lake, MN 56671",
            "phone": "(218) 679-3353",
            "website": "https://www.redlakeschools.org/",
            "students": 800
        },
        {
            "school_name": "Red Lake Secondary Schools",
            "address": "Various locations, Red Lake, MN 56671",
            "phone": "(218) 679-3353",
            "website": "https://www.redlakeschools.org/",
            "students": 600
        }
    ],
    "Red Rock Central School District": [
        {
            "school_name": "Red Rock Central Elementary School",
            "address": "501 E Badger St, Jeffers, MN 56145",
            "phone": "(507) 628-5483",
            "website": "https://www.redrockcentral.org/",
            "students": 200
        },
        {
            "school_name": "Red Rock Central Secondary School",
            "address": "501 E Badger St, Jeffers, MN 56145",
            "phone": "(507) 628-5483",
            "website": "https://www.redrockcentral.org/",
            "students": 250
        }
    ],
    "Red Wing Public School District": [
        {
            "school_name": "Red Wing Elementary Schools",
            "address": "Various locations, Red Wing, MN 55066",
            "phone": "(651) 385-4500",
            "website": "https://www.redwing.k12.mn.us/",
            "students": 1200
        },
        {
            "school_name": "Red Wing Middle School",
            "address": "1851 Old Tyler Rd, Red Wing, MN 55066",
            "phone": "(651) 385-4600",
            "website": "https://www.redwing.k12.mn.us/",
            "students": 600
        },
        {
            "school_name": "Red Wing High School",
            "address": "2451 Eagle Ridge Dr, Red Wing, MN 55066",
            "phone": "(651) 385-4700",
            "website": "https://www.redwing.k12.mn.us/",
            "students": 900
        }
    ],
    "Redwood Area School District": [
        {
            "school_name": "Redwood Area Elementary School",
            "address": "901 E Bridge St, Redwood Falls, MN 56283",
            "phone": "(507) 644-8636",
            "website": "https://www.redwoodareaschools.com/",
            "students": 600
        },
        {
            "school_name": "Redwood Area Secondary School",
            "address": "901 E Bridge St, Redwood Falls, MN 56283",
            "phone": "(507) 644-8636",
            "website": "https://www.redwoodareaschools.com/",
            "students": 500
        }
    ],
    "Region 3 - Northeast Service Cooperative": [
        {
            "school_name": "Northeast Service Cooperative",
            "address": "5701 Grand Ave, Duluth, MN 55807",
            "phone": "(218) 624-1083",
            "website": "https://www.nescoinc.org/",
            "students": 500
        }
    ],
    "Region 4-Lakes Country Service Cooperative": [
        {
            "school_name": "Lakes Country Service Cooperative",
            "address": "1001 E Mount Faith, Fergus Falls, MN 56537",
            "phone": "(218) 739-3273",
            "website": "https://www.lcsc.org/",
            "students": 500
        }
    ],
    "Region 6 and 8-Southwest West Central Service Cooperative": [
        {
            "school_name": "Southwest West Central Service Cooperative",
            "address": "1420 E College Dr, Marshall, MN 56258",
            "phone": "(507) 537-2240",
            "website": "https://swwc.org/",
            "students": 1000
        }
    ],
    "Renville County West School Dist.": [
        {
            "school_name": "Renville County West Elementary School",
            "address": "100 Wolverine Dr, Renville, MN 56284",
            "phone": "(320) 329-8368",
            "website": "https://www.renville.k12.mn.us/",
            "students": 300
        },
        {
            "school_name": "Renville County West Secondary School",
            "address": "100 Wolverine Dr, Renville, MN 56284",
            "phone": "(320) 329-8368",
            "website": "https://www.renville.k12.mn.us/",
            "students": 250
        }
    ],
    "Richfield Public School District": [
        {
            "school_name": "Richfield Elementary Schools",
            "address": "Various locations, Richfield, MN 55423",
            "phone": "(612) 798-6000",
            "website": "https://www.richfieldschools.org/",
            "students": 2000
        },
        {
            "school_name": "Richfield Middle School",
            "address": "7461 Oliver Ave S, Richfield, MN 55423",
            "phone": "(612) 798-6500",
            "website": "https://www.richfieldschools.org/",
            "students": 1000
        },
        {
            "school_name": "Richfield High School",
            "address": "7001 Harriet Ave S, Richfield, MN 55423",
            "phone": "(612) 798-6500",
            "website": "https://www.richfieldschools.org/",
            "students": 1500
        }
    ],
    "Ridgeway Community School": [
        {
            "school_name": "Ridgeway Community School",
            "address": "35564 County Rd 12, Winona, MN 55987",
            "phone": "(507) 454-9566",
            "website": "https://www.ridgewayschool.org/",
            "students": 100
        }
    ],
    "River Bend Education District": [
        {
            "school_name": "River Bend Education District",
            "address": "1315 S Broadway, New Ulm, MN 56073",
            "phone": "(507) 359-8700",
            "website": "https://www.rbecservice.com/",
            "students": 500
        }
    ],
    "River's Edge Academy": [
        {
            "school_name": "River's Edge Academy",
            "address": "188 Buchanan St N, Hutchinson, MN 55350",
            "phone": "(320) 234-3660",
            "website": "https://www.rea.k12.mn.us/",
            "students": 150
        }
    ],
    "Riverway Learning Community Chtr": [
        {
            "school_name": "Riverway Learning Community Charter School",
            "address": "426 County Rd 40 NW, Oronoco, MN 55960",
            "phone": "(507) 367-7502",
            "website": "https://www.riverwaylearningcommunity.org/",
            "students": 100
        }
    ],
    "Robbinsdale Public School District": [
        {
            "school_name": "Robbinsdale Elementary Schools",
            "address": "Various locations, Robbinsdale, MN 55422",
            "phone": "(763) 504-4000",
            "website": "https://www.rdale.org/",
            "students": 5000
        },
        {
            "school_name": "Robbinsdale Middle Schools",
            "address": "Various locations, Robbinsdale, MN 55422",
            "phone": "(763) 504-4000",
            "website": "https://www.rdale.org/",
            "students": 3000
        },
        {
            "school_name": "Robbinsdale High Schools",
            "address": "Various locations, Robbinsdale, MN 55422",
            "phone": "(763) 504-4000",
            "website": "https://www.rdale.org/",
            "students": 4000
        }
    ],
    "Rochester Beacon Academy": [
        {
            "school_name": "Rochester Beacon Academy",
            "address": "7067 E Fish Lake Rd, Maple Grove, MN 55311",
            "phone": "(763) 898-8600",
            "website": "https://www.rochesterbeacon.org/",
            "students": 200
        }
    ],
    "Rochester Math And Science Academy": [
        {
            "school_name": "Rochester Math and Science Academy",
            "address": "5265 Chateau Rd NW, Rochester, MN 55901",
            "phone": "(507) 252-8940",
            "website": "https://rochestermathscience.org/",
            "students": 414
        }
    ],
    "Rochester Off-Campus Charter High": [
        {
            "school_name": "Rochester Off-Campus Charter High School",
            "address": "92 Woodlake Dr SE, Rochester, MN 55904",
            "phone": "(507) 535-3358",
            "website": "https://www.rochesteroffcampus.org/",
            "students": 150
        }
    ],
    "Rochester Public School District": [
        {
            "school_name": "Rochester Elementary Schools",
            "address": "Various locations, Rochester, MN 55901",
            "phone": "(507) 328-4000",
            "website": "https://www.rochesterschools.org/",
            "students": 8000
        },
        {
            "school_name": "Rochester Middle Schools",
            "address": "Various locations, Rochester, MN 55901",
            "phone": "(507) 328-4000",
            "website": "https://www.rochesterschools.org/",
            "students": 4500
        },
        {
            "school_name": "Rochester High Schools",
            "address": "Various locations, Rochester, MN 55901",
            "phone": "(507) 328-4000",
            "website": "https://www.rochesterschools.org/",
            "students": 5000
        }
    ],
    "Rochester Stem Academy": [
        {
            "school_name": "Rochester STEM Academy",
            "address": "5875 Chateau Rd NW, Rochester, MN 55901",
            "phone": "(507) 535-4800",
            "website": "https://rochesterstem.org/",
            "students": 500
        }
    ],
    "Rockford Public School District": [
        {
            "school_name": "Rockford Elementary Schools",
            "address": "Various locations, Rockford, MN 55373",
            "phone": "(763) 477-9165",
            "website": "https://www.rockford.k12.mn.us/",
            "students": 1200
        },
        {
            "school_name": "Rockford Middle School",
            "address": "6051 Ash St, Rockford, MN 55373",
            "phone": "(763) 477-5831",
            "website": "https://www.rockford.k12.mn.us/",
            "students": 600
        },
        {
            "school_name": "Rockford High School",
            "address": "7600 County Rd 50, Rockford, MN 55373",
            "phone": "(763) 477-5846",
            "website": "https://www.rockford.k12.mn.us/",
            "students": 900
        }
    ],
    "Rocori Public School District": [
        {
            "school_name": "Rocori Elementary Schools",
            "address": "Various locations, Cold Spring, MN 56320",
            "phone": "(320) 685-4900",
            "website": "https://www.rocori.k12.mn.us/",
            "students": 1500
        },
        {
            "school_name": "Rocori Middle School",
            "address": "19 Cty Rd 138, Cold Spring, MN 56320",
            "phone": "(320) 685-4900",
            "website": "https://www.rocori.k12.mn.us/",
            "students": 800
        },
        {
            "school_name": "Rocori High School",
            "address": "534 5th Ave N, Cold Spring, MN 56320",
            "phone": "(320) 685-4923",
            "website": "https://www.rocori.k12.mn.us/",
            "students": 1200
        }
    ],
    "Roseau Public School District": [
        {
            "school_name": "Roseau Elementary School",
            "address": "700 Summit Ave, Roseau, MN 56751",
            "phone": "(218) 463-1598",
            "website": "https://www.roseau.k12.mn.us/",
            "students": 500
        },
        {
            "school_name": "Roseau Secondary School",
            "address": "700 Summit Ave, Roseau, MN 56751",
            "phone": "(218) 463-2750",
            "website": "https://www.roseau.k12.mn.us/",
            "students": 450
        }
    ],
    "Rosemount-Apple Valley-Eagan School District": [
        {
            "school_name": "Rosemount-Apple Valley-Eagan Elementary Schools",
            "address": "Various locations, Apple Valley/Eagan/Rosemount, MN",
            "phone": "(651) 423-7700",
            "website": "https://www.district196.org/",
            "students": 10000
        },
        {
            "school_name": "Rosemount-Apple Valley-Eagan Middle Schools",
            "address": "Various locations, Apple Valley/Eagan/Rosemount, MN",
            "phone": "(651) 423-7700",
            "website": "https://www.district196.org/",
            "students": 6000
        },
        {
            "school_name": "Rosemount High School",
            "address": "3335 142nd St W, Rosemount, MN 55068",
            "phone": "(651) 423-7501",
            "website": "https://www.district196.org/",
            "students": 2100
        },
        {
            "school_name": "Apple Valley High School",
            "address": "14450 Hayes Rd, Apple Valley, MN 55124",
            "phone": "(952) 431-8200",
            "website": "https://www.district196.org/",
            "students": 1800
        },
        {
            "school_name": "Eagan High School",
            "address": "4185 Braddock Trl, Eagan, MN 55123",
            "phone": "(651) 683-6900",
            "website": "https://www.district196.org/",
            "students": 2200
        }
    ],
    "Roseville Public School District": [
        {
            "school_name": "Roseville Elementary Schools",
            "address": "Various locations, Roseville, MN 55113",
            "phone": "(651) 628-6451",
            "website": "https://www.isd623.org/",
            "students": 2500
        },
        {
            "school_name": "Roseville Middle Schools",
            "address": "Various locations, Roseville, MN 55113",
            "phone": "(651) 628-6451",
            "website": "https://www.isd623.org/",
            "students": 1800
        },
        {
            "school_name": "Roseville Area High School",
            "address": "1240 County Rd B2 W, Roseville, MN 55113",
            "phone": "(651) 635-1660",
            "website": "https://www.isd623.org/",
            "students": 2100
        }
    ],
    "Rothsay Public School District": [
        {
            "school_name": "Rothsay Elementary School",
            "address": "2040 Co Rd 52, Rothsay, MN 56579",
            "phone": "(218) 867-2116",
            "website": "https://www.rothsay.k12.mn.us/",
            "students": 150
        },
        {
            "school_name": "Rothsay Secondary School",
            "address": "2040 Co Rd 52, Rothsay, MN 56579",
            "phone": "(218) 867-2116",
            "website": "https://www.rothsay.k12.mn.us/",
            "students": 100
        }
    ],
    "Round Lake-Brewster Public Schools": [
        {
            "school_name": "Round Lake-Brewster Elementary School",
            "address": "901 5th Ave, Brewster, MN 56119",
            "phone": "(507) 842-5951",
            "website": "https://www.rlbschools.com/",
            "students": 150
        },
        {
            "school_name": "Round Lake-Brewster Secondary School",
            "address": "901 5th Ave, Brewster, MN 56119",
            "phone": "(507) 842-5951",
            "website": "https://www.rlbschools.com/",
            "students": 100
        }
    ],
    "Royalton Public School District": [
        {
            "school_name": "Royalton Elementary School",
            "address": "619 N Prairie Ave, Royalton, MN 56373",
            "phone": "(320) 584-4200",
            "website": "https://www.royalton.k12.mn.us/",
            "students": 300
        },
        {
            "school_name": "Royalton Secondary School",
            "address": "619 N Prairie Ave, Royalton, MN 56373",
            "phone": "(320) 584-4200",
            "website": "https://www.royalton.k12.mn.us/",
            "students": 250
        }
    ],
    "Rtr Public Schools": [
        {
            "school_name": "RTR Elementary School",
            "address": "107 2nd St NW, Russell, MN 56169",
            "phone": "(507) 697-6321",
            "website": "https://www.rtr.k12.mn.us/",
            "students": 200
        },
        {
            "school_name": "RTR Secondary School",
            "address": "107 2nd St NW, Russell, MN 56169",
            "phone": "(507) 697-6321",
            "website": "https://www.rtr.k12.mn.us/",
            "students": 150
        }
    ],
    "Rum River Special Education Cooperative": [
        {
            "school_name": "Rum River Special Education Cooperative",
            "address": "16955 Banks Rd, Elk River, MN 55330",
            "phone": "(763) 506-1000",
            "website": "https://www.rrsec.org/",
            "students": 500
        }
    ],
    "Runestone Area Ed. District": [
        {
            "school_name": "Runestone Area Education District",
            "address": "416 Summit Ave, Alexandria, MN 56308",
            "phone": "(320) 762-3300",
            "website": "https://www.runestone.net/",
            "students": 500
        }
    ],
    "Rush City Public School District": [
        {
            "school_name": "Rush City Elementary School",
            "address": "51001 Fair Ridge Rd, Rush City, MN 55069",
            "phone": "(320) 358-4724",
            "website": "https://www.rushcity.k12.mn.us/",
            "students": 400
        },
        {
            "school_name": "Rush City Secondary School",
            "address": "51001 Fair Ridge Rd, Rush City, MN 55069",
            "phone": "(320) 358-4724",
            "website": "https://www.rushcity.k12.mn.us/",
            "students": 350
        }
    ],
    "Rushford-Peterson Public Schools": [
        {
            "school_name": "Rushford-Peterson Elementary School",
            "address": "201 Mill St, Rushford Village, MN 55971",
            "phone": "(507) 864-7785",
            "website": "https://www.rushford.k12.mn.us/",
            "students": 300
        },
        {
            "school_name": "Rushford-Peterson Secondary School",
            "address": "201 Mill St, Rushford Village, MN 55971",
            "phone": "(507) 864-7785",
            "website": "https://www.rushford.k12.mn.us/",
            "students": 250
        }
    ],
    "Sage Academy Charter School": [
        {
            "school_name": "Sage Academy Charter School",
            "address": "6510 Singletree Ln, Brooklyn Park, MN 55369",
            "phone": "(763) 315-4461",
            "website": "https://www.sageacademymn.org/",
            "students": 200
        }
    ],
    "Saint Cloud Math And Science Academ": [
        {
            "school_name": "St. Cloud Math and Science Academy",
            "address": "1030 6th Ave S, St Cloud, MN 56301",
            "phone": "(320) 654-9073",
            "website": "https://stcmsa.org/",
            "students": 300
        }
    ],
    "Sankofa Underground North Academy": [
        {
            "school_name": "Sankofa Underground North Academy",
            "address": "3611 N 34th Ave, Minneapolis, MN 55412",
            "phone": "(612) 521-5450",
            "website": "https://www.sankofa-underground.org/",
            "students": 100
        }
    ],
    "Sartell-St. Stephen School District": [
        {
            "school_name": "Sartell-St. Stephen Elementary Schools",
            "address": "Various locations, Sartell/St. Stephen, MN 56379",
            "phone": "(320) 656-3701",
            "website": "https://www.sartell.k12.mn.us/",
            "students": 1800
        },
        {
            "school_name": "Sartell Middle School",
            "address": "627 3rd Ave N, Sartell, MN 56377",
            "phone": "(320) 656-3705",
            "website": "https://www.sartell.k12.mn.us/",
            "students": 900
        },
        {
            "school_name": "Sartell High School",
            "address": "3101 Pinecone Rd N, Sartell, MN 56377",
            "phone": "(320) 656-3701",
            "website": "https://www.sartell.k12.mn.us/",
            "students": 1200
        }
    ],
    "Sauk Centre Public School District": [
        {
            "school_name": "Sauk Centre Elementary School",
            "address": "900 9th St N, Sauk Centre, MN 56378",
            "phone": "(320) 352-2258",
            "website": "https://www.saukcentre.k12.mn.us/",
            "students": 400
        },
        {
            "school_name": "Sauk Centre Secondary School",
            "address": "900 9th St N, Sauk Centre, MN 56378",
            "phone": "(320) 352-2258",
            "website": "https://www.saukcentre.k12.mn.us/",
            "students": 450
        }
    ],
    "Sauk Rapids-Rice Public Schools": [
        {
            "school_name": "Sauk Rapids-Rice Elementary Schools",
            "address": "Various locations, Sauk Rapids, MN 56379",
            "phone": "(320) 653-2737",
            "website": "https://www.isd47.org/",
            "students": 2000
        },
        {
            "school_name": "Sauk Rapids-Rice Middle School",
            "address": "1835 Osauka Rd NE, Sauk Rapids, MN 56379",
            "phone": "(320) 653-2746",
            "website": "https://www.isd47.org/",
            "students": 1100
        },
        {
            "school_name": "Sauk Rapids-Rice High School",
            "address": "1835 Osauka Rd NE, Sauk Rapids, MN 56379",
            "phone": "(320) 653-2832",
            "website": "https://www.isd47.org/",
            "students": 1500
        }
    ],
    "Schoolcraft Learning Community Chtr": [
        {
            "school_name": "Schoolcraft Learning Community Charter School",
            "address": "426 County Rd 40 NW, Oronoco, MN 55960",
            "phone": "(507) 367-7502",
            "website": "https://www.riverwaylearningcommunity.org/",
            "students": 100
        }
    ],
    "Scitech Academy Charter School": [
        {
            "school_name": "SciTech Academy Charter School",
            "address": "5776 Old Shakopee Rd, Bloomington, MN 55437",
            "phone": "(952) 746-7670",
            "website": "https://scitechacademymn.org/",
            "students": 200
        }
    ],
    "Sebeka Public School District": [
        {
            "school_name": "Sebeka Elementary School",
            "address": "804 Pleasant Ave, Sebeka, MN 56477",
            "phone": "(218) 837-5101",
            "website": "https://www.sebeka.k12.mn.us/",
            "students": 200
        },
        {
            "school_name": "Sebeka Secondary School",
            "address": "804 Pleasant Ave, Sebeka, MN 56477",
            "phone": "(218) 837-5101",
            "website": "https://www.sebeka.k12.mn.us/",
            "students": 150
        }
    ],
    "Sejong Academy Of Minnesota": [
        {
            "school_name": "Sejong Academy of Minnesota",
            "address": "9711 Girard Ave N, Brooklyn Park, MN 55443",
            "phone": "(763) 548-8700",
            "website": "https://sejongacademy.org/",
            "students": 300
        }
    ],
    "Seven Hills Preparatory Academy": [
        {
            "school_name": "Seven Hills Preparatory Academy",
            "address": "1610 Marice Dr, Bloomington, MN 55431",
            "phone": "(952) 426-6000",
            "website": "https://www.sevenhillspreparatoryacademy.org/",
            "students": 1000
        }
    ],
    "Shakopee Public School District": [
        {
            "school_name": "Shakopee Elementary Schools",
            "address": "Various locations, Shakopee, MN 55379",
            "phone": "(952) 496-5000",
            "website": "https://shakopee.k12.mn.us/",
            "students": 4000
        },
        {
            "school_name": "Shakopee Middle Schools",
            "address": "Various locations, Shakopee, MN 55379",
            "phone": "(952) 496-5000",
            "website": "https://shakopee.k12.mn.us/",
            "students": 2000
        },
        {
            "school_name": "Shakopee High School",
            "address": "7379 Bridle Pass, Shakopee, MN 55379",
            "phone": "(952) 496-5152",
            "website": "https://shakopee.k12.mn.us/",
            "students": 2500
        }
    ],
    "Sherburne And Northern Wright Speci": [
        {
            "school_name": "Sherburne and Northern Wright Special Education Cooperative",
            "address": "13963 Hantho Ave, Elk River, MN 55330",
            "phone": "(763) 241-8703",
            "website": "https://www.snwsec.org/",
            "students": 500
        }
    ],
    "Sibley East School District": [
        {
            "school_name": "Sibley East Elementary School",
            "address": "600 3rd St, Gaylord, MN 55334",
            "phone": "(507) 237-3306",
            "website": "https://www.sibleyeast.k12.mn.us/",
            "students": 400
        },
        {
            "school_name": "Sibley East Secondary School",
            "address": "600 3rd St, Gaylord, MN 55334",
            "phone": "(507) 237-3306",
            "website": "https://www.sibleyeast.k12.mn.us/",
            "students": 350
        }
    ],
    "Skyline Math And Science Academy": [
        {
            "school_name": "Skyline Math and Science Academy",
            "address": "237 Missouri Ave N, Oakdale, MN 55128",
            "phone": "(651) 644-1023",
            "website": "https://skylinemathacademy.org/",
            "students": 200
        }
    ],
    "Sleepy Eye Public School District": [
        {
            "school_name": "Sleepy Eye Elementary School",
            "address": "115 E Dupree St, Sleepy Eye, MN 56085",
            "phone": "(507) 794-7904",
            "website": "https://www.sleepyeye.mntm.org/",
            "students": 300
        },
        {
            "school_name": "Sleepy Eye Secondary School",
            "address": "115 E Dupree St, Sleepy Eye, MN 56085",
            "phone": "(507) 794-7904",
            "website": "https://www.sleepyeye.mntm.org/",
            "students": 250
        }
    ],
    "Socrates School District": [
        {
            "school_name": "Socrates Program",
            "address": "1667 Snelling Ave N, St Paul, MN 55108",
            "phone": "(651) 209-8384",
            "website": "https://socratesprogram.org/",
            "students": 100
        }
    ],
    "Sojourner Truth Academy": [
        {
            "school_name": "Sojourner Truth Academy",
            "address": "3419 Bloomington Ave, Minneapolis, MN 55407",
            "phone": "(612) 721-4800",
            "website": "https://www.sojournertruthacademy.org/",
            "students": 200
        }
    ],
    "South Koochiching School District": [
        {
            "school_name": "South Koochiching Elementary School",
            "address": "1000 5th St, Northome, MN 56661",
            "phone": "(218) 897-5271",
            "website": "https://www.sk.k12.mn.us/",
            "students": 100
        },
        {
            "school_name": "South Koochiching Secondary School",
            "address": "1000 5th St, Northome, MN 56661",
            "phone": "(218) 897-5271",
            "website": "https://www.sk.k12.mn.us/",
            "students": 75
        }
    ],
    "South St. Paul Public School Dist.": [
        {
            "school_name": "South St. Paul Elementary Schools",
            "address": "Various locations, South St. Paul, MN 55075",
            "phone": "(651) 457-9400",
            "website": "https://www.southstpaul.k12.mn.us/",
            "students": 1800
        },
        {
            "school_name": "South St. Paul Secondary Schools",
            "address": "Various locations, South St. Paul, MN 55075",
            "phone": "(651) 457-9400",
            "website": "https://www.southstpaul.k12.mn.us/",
            "students": 1500
        }
    ],
    "South Washington County School Dist": [
        {
            "school_name": "South Washington County Elementary Schools",
            "address": "Various locations, Cottage Grove/Newport, MN",
            "phone": "(651) 425-6300",
            "website": "https://www.sowashco.org/",
            "students": 6000
        },
        {
            "school_name": "South Washington County Middle Schools",
            "address": "Various locations, Cottage Grove/Newport, MN",
            "phone": "(651) 425-6300",
            "website": "https://www.sowashco.org/",
            "students": 3500
        },
        {
            "school_name": "Park High School",
            "address": "8040 80th St S, Cottage Grove, MN 55016",
            "phone": "(651) 425-3702",
            "website": "https://www.sowashco.org/",
            "students": 1800
        },
        {
            "school_name": "East Ridge High School",
            "address": "4200 Woodbury Dr, Woodbury, MN 55129",
            "phone": "(651) 425-2300",
            "website": "https://www.sowashco.org/",
            "students": 1900
        }
    ],
    "Southern Mn Education Consortium": [
        {
            "school_name": "Southern Minnesota Education Consortium",
            "address": "1420 E College Dr, Marshall, MN 56258",
            "phone": "(507) 537-2240",
            "website": "https://www.smec.k12.mn.us/",
            "students": 500
        }
    ],
    "Southern Plains Education Cooperative": [
        {
            "school_name": "Southern Plains Education Cooperative",
            "address": "1200 N Hiawatha Ave, Pipestone, MN 56164",
            "phone": "(507) 825-5858",
            "website": "https://www.southernplainsedcoop.org/",
            "students": 500
        }
    ],
    "Southland Public School District": [
        {
            "school_name": "Southland Elementary School",
            "address": "203 9th St NW, Adams, MN 55909",
            "phone": "(507) 582-3568",
            "website": "https://www.southlandschools.org/",
            "students": 300
        },
        {
            "school_name": "Southland Secondary School",
            "address": "203 9th St NW, Adams, MN 55909",
            "phone": "(507) 582-3568",
            "website": "https://www.southlandschools.org/",
            "students": 250
        }
    ],
    "Southside Family Charter School": [
        {
            "school_name": "Southside Family Charter School",
            "address": "2749 35th St S, Minneapolis, MN 55406",
            "phone": "(612) 729-9140",
            "website": "https://www.southsidefamily.org/",
            "students": 100
        }
    ],
    "Southwest Metro Intermediate 288": [
        {
            "school_name": "Southwest Metro Intermediate District 288",
            "address": "790 Diffley Rd, Eagan, MN 55123",
            "phone": "(952) 388-1911",
            "website": "https://www.sw288.org/",
            "students": 500
        }
    ],
    "Spectrum High School": [
        {
            "school_name": "Spectrum High School",
            "address": "17796 Industrial Cir NW, Elk River, MN 55330",
            "phone": "(763) 241-8703",
            "website": "https://www.spectrumhighschool.org/",
            "students": 200
        }
    ],
    "Spring Grove School District": [
        {
            "school_name": "Spring Grove Elementary School",
            "address": "113 2nd Ave NW, Spring Grove, MN 55974",
            "phone": "(507) 498-3223",
            "website": "https://www.springgrove.k12.mn.us/",
            "students": 200
        },
        {
            "school_name": "Spring Grove Secondary School",
            "address": "113 2nd Ave NW, Spring Grove, MN 55974",
            "phone": "(507) 498-3223",
            "website": "https://www.springgrove.k12.mn.us/",
            "students": 150
        }
    ],
    "Spring Lake Park Public Schools": [
        {
            "school_name": "Spring Lake Park Elementary Schools",
            "address": "Various locations, Spring Lake Park, MN 55432",
            "phone": "(763) 600-5000",
            "website": "https://www.springlakeparkschools.org/",
            "students": 2000
        },
        {
            "school_name": "Spring Lake Park Middle Schools",
            "address": "Various locations, Spring Lake Park, MN 55432",
            "phone": "(763) 600-5000",
            "website": "https://www.springlakeparkschools.org/",
            "students": 1200
        },
        {
            "school_name": "Spring Lake Park High School",
            "address": "1345 81st Ave NE, Spring Lake Park, MN 55432",
            "phone": "(763) 600-5100",
            "website": "https://www.springlakeparkschools.org/",
            "students": 1800
        }
    ],
    "Springfield Public School District": [
        {
            "school_name": "Springfield Elementary School",
            "address": "39 Cass Ave N, Springfield, MN 56087",
            "phone": "(507) 723-4286",
            "website": "https://www.springfield.mntm.org/",
            "students": 350
        },
        {
            "school_name": "Springfield Secondary School",
            "address": "39 Cass Ave N, Springfield, MN 56087",
            "phone": "(507) 723-4286",
            "website": "https://www.springfield.mntm.org/",
            "students": 300
        }
    ],
    "St Paul Conservatory Performing Art": [
        {
            "school_name": "St. Paul Conservatory for Performing Artists",
            "address": "1667 Snelling Ave N, St Paul, MN 55108",
            "phone": "(651) 209-8384",
            "website": "https://spcpa.org/",
            "students": 500
        }
    ],
    "St. Anthony-New Brighton Schools": [
        {
            "school_name": "St. Anthony-New Brighton Elementary Schools",
            "address": "Various locations, St. Anthony/New Brighton, MN 55112",
            "phone": "(612) 706-1000",
            "website": "https://www.isd282.org/",
            "students": 1200
        },
        {
            "school_name": "St. Anthony Middle School",
            "address": "3301 33rd Ave NE, St Anthony, MN 55418",
            "phone": "(612) 706-1030",
            "website": "https://www.isd282.org/",
            "students": 600
        },
        {
            "school_name": "St. Anthony Village High School",
            "address": "3303 33rd Ave NE, St Anthony, MN 55418",
            "phone": "(612) 706-1100",
            "website": "https://www.isd282.org/",
            "students": 800
        }
    ],
    "St. Charles Public School District": [
        {
            "school_name": "St. Charles Elementary School",
            "address": "940 Whitewater Ave, St Charles, MN 55972",
            "phone": "(507) 932-3420",
            "website": "https://www.stcharlesmn.org/",
            "students": 500
        },
        {
            "school_name": "St. Charles Secondary School",
            "address": "940 Whitewater Ave, St Charles, MN 55972",
            "phone": "(507) 932-3420",
            "website": "https://www.stcharlesmn.org/",
            "students": 400
        }
    ],
    "St. Clair Public School District": [
        {
            "school_name": "St. Clair Elementary School",
            "address": "28909 Heron Lake Rd, St Clair, MN 56080",
            "phone": "(507) 245-3501",
            "website": "https://www.stclair.k12.mn.us/",
            "students": 200
        },
        {
            "school_name": "St. Clair Secondary School",
            "address": "28909 Heron Lake Rd, St Clair, MN 56080",
            "phone": "(507) 245-3501",
            "website": "https://www.stclair.k12.mn.us/",
            "students": 150
        }
    ],
    "St. Cloud Public School District": [
        {
            "school_name": "St. Cloud Elementary Schools",
            "address": "Various locations, St. Cloud, MN 56301",
            "phone": "(320) 370-8000",
            "website": "https://www.isd742.org/",
            "students": 5000
        },
        {
            "school_name": "St. Cloud Middle Schools",
            "address": "Various locations, St. Cloud, MN 56301",
            "phone": "(320) 370-8000",
            "website": "https://www.isd742.org/",
            "students": 2500
        },
        {
            "school_name": "St. Cloud High Schools",
            "address": "Various locations, St. Cloud, MN 56301",
            "phone": "(320) 370-8000",
            "website": "https://www.isd742.org/",
            "students": 3000
        }
    ],
    "St. Croix Preparatory Academy": [
        {
            "school_name": "St. Croix Preparatory Academy",
            "address": "4785 Prairie Dr, Woodbury, MN 55129",
            "phone": "(651) 888-2500",
            "website": "https://www.stcroixprep.org/",
            "students": 1200
        }
    ],
    "St. Croix River Education District": [
        {
            "school_name": "St. Croix River Education District",
            "address": "11 Peavey Rd, Stillwater, MN 55082",
            "phone": "(651) 439-5802",
            "website": "https://www.scred.k12.mn.us/",
            "students": 500
        }
    ],
    "St. Francis Public School District": [
        {
            "school_name": "St. Francis Elementary Schools",
            "address": "Various locations, St. Francis, MN 55070",
            "phone": "(763) 753-7040",
            "website": "https://www.stfrancis.k12.mn.us/",
            "students": 1800
        },
        {
            "school_name": "St. Francis Middle School",
            "address": "22919 St. Francis Blvd NW, St Francis, MN 55070",
            "phone": "(763) 213-8670",
            "website": "https://www.stfrancis.k12.mn.us/",
            "students": 900
        },
        {
            "school_name": "St. Francis High School",
            "address": "3325 Bridge St NW, St Francis, MN 55070",
            "phone": "(763) 213-1500",
            "website": "https://www.stfrancis.k12.mn.us/",
            "students": 1200
        }
    ],
    "St. James Public School District": [
        {
            "school_name": "St. James Elementary School",
            "address": "115 Armstrong Blvd S, St James, MN 56081",
            "phone": "(507) 375-1201",
            "website": "https://www.stjames.k12.mn.us/",
            "students": 400
        },
        {
            "school_name": "St. James Secondary School",
            "address": "115 Armstrong Blvd S, St James, MN 56081",
            "phone": "(507) 375-1201",
            "website": "https://www.stjames.k12.mn.us/",
            "students": 350
        }
    ],
    "St. Louis County School District": [
        {
            "school_name": "St. Louis County Schools",
            "address": "Various locations, Northern Minnesota",
            "phone": "(218) 726-2304",
            "website": "https://www.stlouiscountymn.gov/departments-a-z/schools",
            "students": 1000
        }
    ],
    "St. Louis Park Public School Dist.": [
        {
            "school_name": "St. Louis Park Elementary Schools",
            "address": "Various locations, St. Louis Park, MN 55426",
            "phone": "(952) 928-6000",
            "website": "https://www.slpschools.org/",
            "students": 2500
        },
        {
            "school_name": "St. Louis Park Middle School",
            "address": "3025 Minnesota Dr, St Louis Park, MN 55426",
            "phone": "(952) 928-6300",
            "website": "https://www.slpschools.org/",
            "students": 1200
        },
        {
            "school_name": "St. Louis Park High School",
            "address": "6425 W 33rd St, St Louis Park, MN 55426",
            "phone": "(952) 928-6100",
            "website": "https://www.slpschools.org/",
            "students": 1800
        }
    ],
    "St. Michael-Albertville School Dist": [
        {
            "school_name": "St. Michael-Albertville Elementary Schools",
            "address": "Various locations, St. Michael/Albertville, MN 55376",
            "phone": "(763) 497-6500",
            "website": "https://www.stma.k12.mn.us/",
            "students": 3000
        },
        {
            "school_name": "St. Michael-Albertville Middle School East",
            "address": "11343 50th St NE, Albertville, MN 55301",
            "phone": "(763) 497-2192",
            "website": "https://www.stma.k12.mn.us/",
            "students": 1200
        },
        {
            "school_name": "St. Michael-Albertville Middle School West",
            "address": "5800 Kernel Dr, St Michael, MN 55376",
            "phone": "(763) 497-6500",
            "website": "https://www.stma.k12.mn.us/",
            "students": 1200
        },
        {
            "school_name": "St. Michael-Albertville High School",
            "address": "5800 Kernel Dr, St Michael, MN 55376",
            "phone": "(763) 497-6500",
            "website": "https://www.stma.k12.mn.us/",
            "students": 2400
        }
    ],
    "St. Paul City School": [
        {
            "school_name": "St. Paul City School",
            "address": "1667 Snelling Ave N, St Paul, MN 55108",
            "phone": "(651) 209-8384",
            "website": "https://www.stpaulcityschool.org/",
            "students": 100
        }
    ],
    "St. Paul Public School District": [
        {
            "school_name": "St. Paul Elementary Schools",
            "address": "Various locations, St. Paul, MN 55101",
            "phone": "(651) 767-8100",
            "website": "https://www.spps.org/",
            "students": 15000
        },
        {
            "school_name": "St. Paul Middle Schools",
            "address": "Various locations, St. Paul, MN 55101",
            "phone": "(651) 767-8100",
            "website": "https://www.spps.org/",
            "students": 8000
        },
        {
            "school_name": "St. Paul High Schools",
            "address": "Various locations, St. Paul, MN 55101",
            "phone": "(651) 767-8100",
            "website": "https://www.spps.org/",
            "students": 10000
        }
    ],
    "St. Peter Public School District": [
        {
            "school_name": "St. Peter Elementary Schools",
            "address": "Various locations, St. Peter, MN 56082",
            "phone": "(507) 934-4210",
            "website": "https://www.stpeterschools.org/",
            "students": 800
        },
        {
            "school_name": "St. Peter Middle School",
            "address": "1005 S 5th St, St Peter, MN 56082",
            "phone": "(507) 934-4210",
            "website": "https://www.stpeterschools.org/",
            "students": 400
        },
        {
            "school_name": "St. Peter High School",
            "address": "100 Lincoln Dr, St Peter, MN 56082",
            "phone": "(507) 934-4210",
            "website": "https://www.stpeterschools.org/",
            "students": 600
        }
    ],
    "Staples-Motley School District": [
        {
            "school_name": "Staples-Motley Elementary School",
            "address": "805 3rd St NE, Staples, MN 56479",
            "phone": "(218) 894-5400",
            "website": "https://www.isd2170.k12.mn.us/",
            "students": 500
        },
        {
            "school_name": "Staples-Motley Secondary School",
            "address": "805 3rd St NE, Staples, MN 56479",
            "phone": "(218) 894-5400",
            "website": "https://www.isd2170.k12.mn.us/",
            "students": 450
        }
    ],
    "Star Of The North Academy Charter S": [
        {
            "school_name": "Star of the North Academy Charter School",
            "address": "1701 Charlton St, West St Paul, MN 55118",
            "phone": "(651) 234-0719",
            "website": "https://www.starofthenorthacademy.org/",
            "students": 150
        }
    ],
    "Step Academy Charter School": [
        {
            "school_name": "STEP Academy Charter School",
            "address": "835 5th St E, St Paul, MN 55106",
            "phone": "(651) 289-3991",
            "website": "https://www.stepacademymn.org/",
            "students": 200
        }
    ],
    "Stephen-Argyle Central Schools": [
        {
            "school_name": "Stephen-Argyle Elementary School",
            "address": "401 Heather Ln, Stephen, MN 56757",
            "phone": "(218) 478-3314",
            "website": "https://www.sac.k12.mn.us/",
            "students": 200
        },
        {
            "school_name": "Stephen-Argyle Secondary School",
            "address": "401 Heather Ln, Stephen, MN 56757",
            "phone": "(218) 478-3314",
            "website": "https://www.sac.k12.mn.us/",
            "students": 150
        }
    ],
    "Stewartville Public School District": [
        {
            "school_name": "Stewartville Elementary School",
            "address": "501 Cty Rd 28, Stewartville, MN 55976",
            "phone": "(507) 533-1300",
            "website": "https://www.stewartville.k12.mn.us/",
            "students": 800
        },
        {
            "school_name": "Stewartville Secondary School",
            "address": "501 Cty Rd 28, Stewartville, MN 55976",
            "phone": "(507) 533-1300",
            "website": "https://www.stewartville.k12.mn.us/",
            "students": 700
        }
    ],
    "Stillwater Area Public School Dist.": [
        {
            "school_name": "Stillwater Area Elementary Schools",
            "address": "Various locations, Stillwater, MN 55082",
            "phone": "(651) 351-8340",
            "website": "https://www.stillwaterschools.org/",
            "students": 3800
        },
        {
            "school_name": "Stillwater Junior High School",
            "address": "523 W Marsh St, Stillwater, MN 55082",
            "phone": "(651) 351-8800",
            "website": "https://www.stillwaterschools.org/",
            "students": 1100
        },
        {
            "school_name": "Oak-Land Junior High School",
            "address": "820 Manning Ave N, Lake Elmo, MN 55042",
            "phone": "(651) 351-7600",
            "website": "https://www.stillwaterschools.org/",
            "students": 1000
        },
        {
            "school_name": "Stillwater Area High School",
            "address": "5701 Stillwater Blvd N, Oak Park Heights, MN 55082",
            "phone": "(651) 351-8100",
            "website": "https://www.stillwaterschools.org/",
            "students": 2400
        }
    ],
    "Stonebridge Community School": [
        {
            "school_name": "Stonebridge Community School",
            "address": "7145 Steepleview Rd, Woodbury, MN 55125",
            "phone": "(651) 439-7982",
            "website": "https://stonebridgewoodbury.org/",
            "students": 200
        }
    ],
    "Stride Academy Charter School": [
        {
            "school_name": "Stride Academy Charter School",
            "address": "3051 Penn Ave N, Minneapolis, MN 55411",
            "phone": "(612) 355-0950",
            "website": "https://strideacademy.org/",
            "students": 300
        }
    ],
    "Success Academy": [
        {
            "school_name": "Success Academy",
            "address": "6700 Bixby Ave N, Brooklyn Park, MN 55369",
            "phone": "(763) 971-7417",
            "website": "https://www.successacademymn.org/",
            "students": 150
        }
    ],
    "Swan River Montessori Charter School": [
        {
            "school_name": "Swan River Montessori Charter School",
            "address": "1107 3rd St NW, Monticello, MN 55362",
            "phone": "(763) 271-7926",
            "website": "https://swanrivermontessori.org/",
            "students": 200
        }
    ],
    "Swanville Public School District": [
        {
            "school_name": "Swanville Elementary School",
            "address": "701 South St, Swanville, MN 56382",
            "phone": "(320) 568-2293",
            "website": "https://www.swanville.k12.mn.us/",
            "students": 150
        },
        {
            "school_name": "Swanville Secondary School",
            "address": "701 South St, Swanville, MN 56382",
            "phone": "(320) 568-2293",
            "website": "https://www.swanville.k12.mn.us/",
            "students": 100
        }
    ],
    "T.R.U.T.H. Preparatory Academy Char": [
        {
            "school_name": "T.R.U.T.H. Preparatory Academy Charter School",
            "address": "1857 5th St NE, Minneapolis, MN 55418",
            "phone": "(612) 379-7824",
            "website": "https://truthprepacademy.org/",
            "students": 100
        }
    ],
    "Team Academy": [
        {
            "school_name": "TEAM Academy Charter School",
            "address": "1855 E Lake St, Minneapolis, MN 55407",
            "phone": "(612) 722-4726",
            "website": "https://teamacademycharter.com/",
            "students": 100
        }
    ],
    "Technical Academies Of Minnesota": [
        {
            "school_name": "Technical Academies of Minnesota",
            "address": "7051 Brooklyn Blvd, Brooklyn Center, MN 55429",
            "phone": "(763) 549-5663",
            "website": "https://technicalacademiesofminnesota.org/",
            "students": 200
        }
    ],
    "Tesfa International School": [
        {
            "school_name": "Tesfa International School",
            "address": "1760 Larpenteur Ave W, Falcon Heights, MN 55113",
            "phone": "(651) 639-1700",
            "website": "https://www.tesfascholars.org/",
            "students": 150
        }
    ],
    "The Journey School": [
        {
            "school_name": "The Journey School",
            "address": "3671 Columbus Ave S, Minneapolis, MN 55407",
            "phone": "(612) 823-7827",
            "website": "https://www.journeyschool.org/",
            "students": 100
        }
    ],
    "Thief River Falls School District": [
        {
            "school_name": "Thief River Falls Elementary Schools",
            "address": "Various locations, Thief River Falls, MN 56701",
            "phone": "(218) 681-8711",
            "website": "https://www.trf.k12.mn.us/",
            "students": 800
        },
        {
            "school_name": "Franklin Middle School",
            "address": "513 Greenwood St E, Thief River Falls, MN 56701",
            "phone": "(218) 681-8673",
            "website": "https://www.trf.k12.mn.us/",
            "students": 400
        },
        {
            "school_name": "Lincoln High School",
            "address": "1501 Greenwood St E, Thief River Falls, MN 56701",
            "phone": "(218) 681-7668",
            "website": "https://www.trf.k12.mn.us/",
            "students": 600
        }
    ],
    "Three Rivers Montessori School": [
        {
            "school_name": "Three Rivers Montessori School",
            "address": "1611 Ames Ave, Elk River, MN 55330",
            "phone": "(763) 441-9950",
            "website": "https://threeriversmontessori.org/",
            "students": 150
        }
    ],
    "Tracy Area Public School District": [
        {
            "school_name": "Tracy Area Elementary School",
            "address": "934 Pine St, Tracy, MN 56175",
            "phone": "(507) 629-5518",
            "website": "https://www.tracy.k12.mn.us/",
            "students": 300
        },
        {
            "school_name": "Tracy Area Secondary School",
            "address": "934 Pine St, Tracy, MN 56175",
            "phone": "(507) 629-5518",
            "website": "https://www.tracy.k12.mn.us/",
            "students": 250
        }
    ],
    "Treknorth High School": [
        {
            "school_name": "TrekNorth High School",
            "address": "2400 Pine Ridge Ave NW, Bemidji, MN 56601",
            "phone": "(218) 444-1888",
            "website": "https://www.treknorth.org/",
            "students": 200
        }
    ],
    "Tri-City United School District": [
        {
            "school_name": "Tri-City United Elementary School",
            "address": "33 Southeast St, Lonsdale, MN 55046",
            "phone": "(507) 744-3900",
            "website": "https://www.tristatedatacorp.com/tcu/",
            "students": 600
        },
        {
            "school_name": "Tri-City United Secondary School",
            "address": "33 Southeast St, Lonsdale, MN 55046",
            "phone": "(507) 744-3900",
            "website": "https://www.tristatedatacorp.com/tcu/",
            "students": 500
        }
    ],
    "Tri-County School District": [
        {
            "school_name": "Tri-County Elementary School",
            "address": "27 Cty Rd 33, Karlstad, MN 56732",
            "phone": "(218) 436-2376",
            "website": "https://www.tri-county.k12.mn.us/",
            "students": 100
        },
        {
            "school_name": "Tri-County Secondary School",
            "address": "27 Cty Rd 33, Karlstad, MN 56732",
            "phone": "(218) 436-2376",
            "website": "https://www.tri-county.k12.mn.us/",
            "students": 75
        }
    ],
    "Trio Wolf Creek Distance Learning": [
        {
            "school_name": "Trio Wolf Creek Distance Learning Charter School",
            "address": "Online school",
            "phone": "(218) 586-0500",
            "website": "https://www.triowolfcreek.com/",
            "students": 300
        }
    ],
    "Triton School District": [
        {
            "school_name": "Triton Elementary School",
            "address": "5930 Broadway St, Longville, MN 56655",
            "phone": "(218) 363-3299",
            "website": "https://www.triton.k12.mn.us/",
            "students": 200
        },
        {
            "school_name": "Triton Secondary School",
            "address": "5930 Broadway St, Longville, MN 56655",
            "phone": "(218) 363-3299",
            "website": "https://www.triton.k12.mn.us/",
            "students": 150
        }
    ],
    "Truman Public School District": [
        {
            "school_name": "Truman Elementary School",
            "address": "401 E 6th St S, Truman, MN 56088",
            "phone": "(507) 776-2111",
            "website": "https://www.truman.k12.mn.us/",
            "students": 150
        },
        {
            "school_name": "Truman Secondary School",
            "address": "401 E 6th St S, Truman, MN 56088",
            "phone": "(507) 776-2111",
            "website": "https://www.truman.k12.mn.us/",
            "students": 100
        }
    ],
    "Twin Cities Academy High School": [
        {
            "school_name": "Twin Cities Academy High School",
            "address": "688 Hamline Ave N, St Paul, MN 55104",
            "phone": "(651) 285-9177",
            "website": "https://www.tcahs.org/",
            "students": 200
        }
    ],
    "Twin Cities German Immersion Chrtr": [
        {
            "school_name": "Twin Cities German Immersion Charter School",
            "address": "1031 Como Ave, St Paul, MN 55103",
            "phone": "(651) 492-7106",
            "website": "https://www.tcgis.org/",
            "students": 500
        }
    ],
    "Twin Cities International Elementary School": [
        {
            "school_name": "Twin Cities International Elementary School",
            "address": "92 St Joseph St, St Paul, MN 55107",
            "phone": "(651) 778-2900",
            "website": "https://www.tcics.org/",
            "students": 300
        }
    ],
    "Ubah Medical Academy Charter School": [
        {
            "school_name": "Ubah Medical Academy Charter School",
            "address": "3011 27th Ave S, Minneapolis, MN 55406",
            "phone": "(612) 722-4529",
            "website": "https://ubahmedicalacademy.org/",
            "students": 150
        }
    ],
    "Ulen-Hitterdal Public School Dist": [
        {
            "school_name": "Ulen-Hitterdal Elementary School",
            "address": "180 Cty Rd 10, Ulen, MN 56585",
            "phone": "(218) 596-8853",
            "website": "https://www.ulenhitterdal.k12.mn.us/",
            "students": 100
        },
        {
            "school_name": "Ulen-Hitterdal Secondary School",
            "address": "180 Cty Rd 10, Ulen, MN 56585",
            "phone": "(218) 596-8853",
            "website": "https://www.ulenhitterdal.k12.mn.us/",
            "students": 75
        }
    ],
    "Underwood Public School District": [
        {
            "school_name": "Underwood Elementary School",
            "address": "201 Church Ave, Underwood, MN 56586",
            "phone": "(218) 826-6101",
            "website": "https://www.underwood.k12.mn.us/",
            "students": 200
        },
        {
            "school_name": "Underwood Secondary School",
            "address": "201 Church Ave, Underwood, MN 56586",
            "phone": "(218) 826-6101",
            "website": "https://www.underwood.k12.mn.us/",
            "students": 150
        }
    ],
    "United South Central School Dist.": [
        {
            "school_name": "United South Central Elementary School",
            "address": "104 Ash St W, Wells, MN 56097",
            "phone": "(507) 553-5810",
            "website": "https://www.unitedsouthcentral.org/",
            "students": 300
        },
        {
            "school_name": "United South Central Secondary School",
            "address": "104 Ash St W, Wells, MN 56097",
            "phone": "(507) 553-5810",
            "website": "https://www.unitedsouthcentral.org/",
            "students": 250
        }
    ],
    "Universal Academy Charter School": [
        {
            "school_name": "Universal Academy Charter School",
            "address": "7451 York Ave S, Brooklyn Park, MN 55429",
            "phone": "(763) 600-7787",
            "website": "https://www.uamn.org/",
            "students": 200
        }
    ],
    "Upper Mississippi Academy": [
        {
            "school_name": "Upper Mississippi Academy",
            "address": "19 E Exchange St, St Paul, MN 55101",
            "phone": "(651) 528-8091",
            "website": "https://umissacademy.org",
            "students": 206
        }
    ],
    "Upsala Public School District": [
        {
            "school_name": "Upsala Elementary School",
            "address": "415 S Front St, Upsala, MN 56384",
            "phone": "(320) 573-2174",
            "website": "https://www.upsala.k12.mn.us/",
            "students": 200
        },
        {
            "school_name": "Upsala Secondary School",
            "address": "415 S Front St, Upsala, MN 56384",
            "phone": "(320) 573-2174",
            "website": "https://www.upsala.k12.mn.us/",
            "students": 150
        }
    ],
    "Urban Academy Charter School": [
        {
            "school_name": "Urban Academy Charter School",
            "address": "3400 N 40th St, Minneapolis, MN 55412",
            "phone": "(612) 722-4472",
            "website": "https://urbanacademymn.org/",
            "students": 150
        }
    ],
    "Venture Academy": [
        {
            "school_name": "Venture Academy",
            "address": "9600 Aldrich Ave S, Bloomington, MN 55420",
            "phone": "(952) 681-6678",
            "website": "https://www.ventureacademymn.org/",
            "students": 200
        }
    ],
    "Vermilion Country School": [
        {
            "school_name": "Vermilion Country School",
            "address": "1 Enterprise Dr, Tower, MN 55790",
            "phone": "(218) 753-1246",
            "website": "https://www.vermilioncountry.org/",
            "students": 150
        }
    ],
    "Verndale Public School District": [
        {
            "school_name": "Verndale Elementary School",
            "address": "411 SW Brown St, Verndale, MN 56481",
            "phone": "(218) 445-5184",
            "website": "https://www.verndale.k12.mn.us/",
            "students": 150
        },
        {
            "school_name": "Verndale Secondary School",
            "address": "411 SW Brown St, Verndale, MN 56481",
            "phone": "(218) 445-5184",
            "website": "https://www.verndale.k12.mn.us/",
            "students": 100
        }
    ],
    "Virginia Public School District": [
        {
            "school_name": "Virginia Elementary Schools",
            "address": "Various locations, Virginia, MN 55792",
            "phone": "(218) 742-3901",
            "website": "https://www.vmps.org/",
            "students": 800
        },
        {
            "school_name": "Virginia Secondary Schools",
            "address": "Various locations, Virginia, MN 55792",
            "phone": "(218) 742-3901",
            "website": "https://www.vmps.org/",
            "students": 700
        }
    ],
    "Voyageurs Expeditionary": [
        {
            "school_name": "Voyageurs Expeditionary School",
            "address": "3724 Bemidji Ave N, Bemidji, MN 56601",
            "phone": "(218) 444-3130",
            "website": "https://www.vexs.org/",
            "students": 200
        }
    ],
    "Wabasha-Kellogg Public School Dist.": [
        {
            "school_name": "Wabasha-Kellogg Elementary School",
            "address": "2113 Hiawatha Dr E, Wabasha, MN 55981",
            "phone": "(651) 565-3559",
            "website": "https://www.wabasha-kellogg.k12.mn.us/",
            "students": 400
        },
        {
            "school_name": "Wabasha-Kellogg Secondary School",
            "address": "2113 Hiawatha Dr E, Wabasha, MN 55981",
            "phone": "(651) 565-3559",
            "website": "https://www.wabasha-kellogg.k12.mn.us/",
            "students": 350
        }
    ],
    "Wabasso Public School District": [
        {
            "school_name": "Wabasso Elementary School",
            "address": "633 Maple St, Wabasso, MN 56293",
            "phone": "(507) 342-5100",
            "website": "https://www.wabasso.k12.mn.us/",
            "students": 150
        },
        {
            "school_name": "Wabasso Secondary School",
            "address": "633 Maple St, Wabasso, MN 56293",
            "phone": "(507) 342-5100",
            "website": "https://www.wabasso.k12.mn.us/",
            "students": 100
        }
    ],
    "Waconia Public School District": [
        {
            "school_name": "Waconia Elementary Schools",
            "address": "Various locations, Waconia, MN 55387",
            "phone": "(952) 442-0600",
            "website": "https://www.waconia.k12.mn.us/",
            "students": 1800
        },
        {
            "school_name": "Waconia Middle School",
            "address": "1400 Community Dr, Waconia, MN 55387",
            "phone": "(952) 442-0670",
            "website": "https://www.waconia.k12.mn.us/",
            "students": 900
        },
        {
            "school_name": "Waconia High School",
            "address": "1400 Community Dr, Waconia, MN 55387",
            "phone": "(952) 442-0670",
            "website": "https://www.waconia.k12.mn.us/",
            "students": 1300
        }
    ],
    "Wadena-Deer Creek School District": [
        {
            "school_name": "Wadena-Deer Creek Elementary School",
            "address": "600 Colfax Ave SW, Wadena, MN 56482",
            "phone": "(218) 631-3510",
            "website": "https://www.wdc2155.k12.mn.us/",
            "students": 500
        },
        {
            "school_name": "Wadena-Deer Creek Secondary School",
            "address": "600 Colfax Ave SW, Wadena, MN 56482",
            "phone": "(218) 631-3510",
            "website": "https://www.wdc2155.k12.mn.us/",
            "students": 400
        }
    ],
    "Walker-Hackensack-Akeley School Dist": [
        {
            "school_name": "Walker-Hackensack-Akeley Elementary School",
            "address": "201 S Akeley Ave, Walker, MN 56484",
            "phone": "(218) 547-1900",
            "website": "https://www.walker.k12.mn.us/",
            "students": 300
        },
        {
            "school_name": "Walker-Hackensack-Akeley Secondary School",
            "address": "201 S Akeley Ave, Walker, MN 56484",
            "phone": "(218) 547-1900",
            "website": "https://www.walker.k12.mn.us/",
            "students": 250
        }
    ],
    "Warren-Alvarado-Oslo School Dist.": [
        {
            "school_name": "Warren-Alvarado-Oslo Elementary School",
            "address": "617 Pumpkin Ridge Rd, Warren, MN 56762",
            "phone": "(218) 745-5343",
            "website": "https://www.wao.k12.mn.us/",
            "students": 200
        },
        {
            "school_name": "Warren-Alvarado-Oslo Secondary School",
            "address": "617 Pumpkin Ridge Rd, Warren, MN 56762",
            "phone": "(218) 745-5343",
            "website": "https://www.wao.k12.mn.us/",
            "students": 150
        }
    ],
    "Warroad Public School District": [
        {
            "school_name": "Warroad Elementary School",
            "address": "510 Cedar Ave, Warroad, MN 56763",
            "phone": "(218) 386-6699",
            "website": "https://www.warroad.k12.mn.us/",
            "students": 300
        },
        {
            "school_name": "Warroad Secondary School",
            "address": "510 Cedar Ave, Warroad, MN 56763",
            "phone": "(218) 386-6699",
            "website": "https://www.warroad.k12.mn.us/",
            "students": 250
        }
    ],
    "Waseca Public School District": [
        {
            "school_name": "Waseca Elementary Schools",
            "address": "Various locations, Waseca, MN 56093",
            "phone": "(507) 835-5020",
            "website": "https://www.waseca.k12.mn.us/",
            "students": 800
        },
        {
            "school_name": "Waseca Intermediate School",
            "address": "900 5th St NW, Waseca, MN 56093",
            "phone": "(507) 835-5020",
            "website": "https://www.waseca.k12.mn.us/",
            "students": 400
        },
        {
            "school_name": "Waseca Junior/Senior High School",
            "address": "1717 2nd St NW, Waseca, MN 56093",
            "phone": "(507) 835-5020",
            "website": "https://www.waseca.k12.mn.us/",
            "students": 800
        }
    ],
    "Watershed High School": [
        {
            "school_name": "Watershed High School",
            "address": "3825 Edgewood Ave S, St Louis Park, MN 55426",
            "phone": "(952) 928-6000",
            "website": "https://watershedhs.org/",
            "students": 100
        }
    ],
    "Watertown-Mayer Public School Dist.": [
        {
            "school_name": "Watertown-Mayer Elementary School",
            "address": "1001 Hwy 25 NW, Watertown, MN 55388",
            "phone": "(952) 955-0480",
            "website": "https://www.wm.k12.mn.us/",
            "students": 800
        },
        {
            "school_name": "Watertown-Mayer Secondary School",
            "address": "1001 Hwy 25 NW, Watertown, MN 55388",
            "phone": "(952) 955-0480",
            "website": "https://www.wm.k12.mn.us/",
            "students": 700
        }
    ],
    "Waterville-Elysian-Morristown School District": [
        {
            "school_name": "Waterville-Elysian-Morristown Elementary School",
            "address": "500 3rd St S, Waterville, MN 56096",
            "phone": "(507) 362-4432",
            "website": "https://www.wem.k12.mn.us/",
            "students": 400
        },
        {
            "school_name": "Waterville-Elysian-Morristown Secondary School",
            "address": "500 3rd St S, Waterville, MN 56096",
            "phone": "(507) 362-4432",
            "website": "https://www.wem.k12.mn.us/",
            "students": 350
        }
    ],
    "Waubun-Ogema-White Earth Public School": [
        {
            "school_name": "Waubun-Ogema-White Earth Elementary School",
            "address": "1013 Park Ave, Waubun, MN 56589",
            "phone": "(218) 473-6172",
            "website": "https://www.waubun.k12.mn.us/",
            "students": 200
        },
        {
            "school_name": "Waubun-Ogema-White Earth Secondary School",
            "address": "1013 Park Ave, Waubun, MN 56589",
            "phone": "(218) 473-6172",
            "website": "https://www.waubun.k12.mn.us/",
            "students": 150
        }
    ],
    "Wayzata Public School District": [
        {
            "school_name": "Wayzata Elementary Schools",
            "address": "Various locations, Wayzata, MN 55391",
            "phone": "(763) 745-5635",
            "website": "https://www.wayzataschools.org/",
            "students": 4000
        },
        {
            "school_name": "Wayzata Middle Schools",
            "address": "Various locations, Wayzata, MN 55391",
            "phone": "(763) 745-5635",
            "website": "https://www.wayzataschools.org/",
            "students": 2500
        },
        {
            "school_name": "Wayzata High School",
            "address": "4955 Peony Ln N, Plymouth, MN 55446",
            "phone": "(763) 745-6610",
            "website": "https://www.wayzataschools.org/",
            "students": 3500
        }
    ],
    "West Central Area School District": [
        {
            "school_name": "West Central Area Elementary School",
            "address": "409 S Board St, Barrett, MN 56311",
            "phone": "(320) 528-3201",
            "website": "https://www.westwcamn.org/",
            "students": 200
        },
        {
            "school_name": "West Central Area Secondary School",
            "address": "409 S Board St, Barrett, MN 56311",
            "phone": "(320) 528-3201",
            "website": "https://www.westwcamn.org/",
            "students": 150
        }
    ]

# Yet to do:
# West Central Education District	,
    # West Side Summit Charter School	,
    # West St. Paul-Mendota Hts.-Eagan School District	,
    # Westbrook-Walnut Grove Schools	,
    # Westonka Public School District	,
    # Wheaton Area Public School District	,
    # White Bear Lake School District	,
    # Willmar Public School District	,
    # Willow River Public School District	,
    # Win-E-Mac School District	,
    # Windom Public School District	,
    # Winona Area Public School District	,
    # Woodbury Leadership Academy	,
    # World Learner Charter School	,
    # Worthington Public School District	,
    # Wrenshall Public School District	,
    # Wright Technical Center	,
    # Yellow Medicine East School District	,
    # Yinghua Academy	,
    # Zumbro Education District	,
    # Zumbrota-Mazeppa School District	,


}

# Combine all school lists into one DataFrame
schools_data = pd.DataFrame([school for district in schools.values() for school in district])

# Define the output directory for the markdown files
output_dir = '.'
os.makedirs(output_dir, exist_ok=True)

# Assign district names to each row in the DataFrame
for district_name, schools_list in schools.items():
    district_name = district_name.replace(" Dist.", "").replace(" District", "").replace(" Public School District", "").replace(" School District", "").replace(" School Dist", "").replace(" Public School", "").rstrip('.')

    for school in schools_list:
        school['address'] = school['address'].replace('+', ', ')
        schools_data.loc[schools_data['school_name'] == school['school_name'], 'district_name'] = district_name

# Function to generate markdown files
def generate_markdown_by_index(row):
    # Simplify the school name for the directory and file
    district_name_simple = row['district_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")
    school_name_simple = row['school_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")
    path = os.path.join(output_dir, district_name_simple)
    os.makedirs(path, exist_ok=True)

    # Filename for the markdown
    file_path = os.path.join(path, f"{school_name_simple}.md")

    # Markdown content with front-matter and details
    with open(file_path, 'w') as file:
        file.write(f"---\nlayout: page\ntitle: {row['school_name']}\n---\n")  # School Name
        file.write(
            f"# Navigation\n\n[[All countries/states/provinces]](../../..) > [[All Minnesota Districts]](../..) > [[All In {row['district_name']}]](..)\n\n")

        file.write(f"# {row['school_name']} ({row['district_name']})\n\n")  # School Name and area as header

        # Loop through keys per school
        for key, value in row.items():
            if key not in ['district_name', 'school_name']:
                if str(value).startswith("http"):
                    value = "<" + value + ">"
                file.write(f"**{key.replace('_', ' ').title()}**: {value}\n\n")

        file.write(f"**School's overall airborne virus protection grade (0-5)**: 0\n\n")
        file.write(f"**Discord, Facebook, or WhatsApp group for discovery/advocacy for THIS school**: TODO\n\n")
        file.write(f"**School's policy on Ventilation**: TODO\n\n")
        file.write(f"**School's Ventilation Work Completion**: TODO\n\n")
        file.write(f"**School's Air-Purification**: TODO\n\n")
        file.write(f"**School's CO2 monitoring to actively drive ventilation and filtration**: TODO\n\n")
        file.write(f"**School's Wikidata URL**: TODO")
        file.write(f"\n\n\n[Edit this page](https://github.com/ventilate-schools/MN/edit/main/{file_path}).")
        file.write(f" See also [rules for contribution](../../../contribution-rules/)")

# Generate markdown files for each school
schools_data.apply(generate_markdown_by_index, axis=1)

def create_area_and_root_index():
    # Create a dictionary to keep track of schools in each district
    districts_dict = {}

    for index, row in schools_data.iterrows():
        district_name_simple = row['district_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")
        school_name_simple = row['school_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")

        # Check if the district already exists in the dictionary
        if district_name_simple not in districts_dict:
            districts_dict[district_name_simple] = []

        # Append the school name to the district's list
        districts_dict[district_name_simple].append(school_name_simple)

    # Write an index markdown file for each district and gather data for root index
    root_index_content = "---\ntitle: Schools in Minnesota and their ventilation status\n---\n"

    root_index_content += (
        "\n# Navigation\n\n[[All countries/states/provinces]](..)\n\n# Purpose of site\n\nGiven **COVID-19 is Airborne** and the world is pushing to better ventilate "
        "schools for long term student and teacher health, we're tracking the "
        "progress for that in Minnesota. This is ahead of government effort to do the same. If government starts to "
        "track this work, this effort will continue because that effort might be weak."
        "We're guided by 33 profs and PhDs who are pushing for a policy change in a "
        "March 2024 article on **Science.org**: [Mandating indoor air quality for public buildings](https://drive.google.com/file/d/16l_IH47cQtC7fFuafvHca7ORNVGITxx8/view). "
        "Not only active ventilation (which should "
        "be mechanical heat recovery type in this age), but air filtration/purification "
        "too and CO2 monitoring to drive ventilation levels, as CO2 inside is a proxy indicator "
        "for COVID risk. As it happens the WHO also have a [2023 airborne risk assessment guide](https://iris.who.int/handle/10665/376346)\n\n"
        "Know that other diseases are airborne too: Measles "
        "(studies [1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2810934/pdf/10982072.pdf) "
        "[2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3880795/pdf/nihms532643.pdf) "
        "[3](https://pubmed.ncbi.nlm.nih.gov/31257413/) "
        "[4](https://www.sciencedirect.com/science/article/pii/S0196655316305363)), "
        "Influenza, RSV and TB. The same "
        "ventilation and air filtration measures reduce transmission of those too.\n\n When we say "
        "student and teacher health, we're wanting absences to go down too. If we lower "
        "transmission in schools, we reduce multi-generation transmission too, as kids bring "
        "infections home to parents. With lowered transmission, we also reduce long COVID, "
        "where the worst sufferers have disappeared from education and the workplace.\n\n")

    root_index_content += (
        "\n## Leaderboard\n\n1. to be announced\n2. to be announced\n3. to be announced\n4. to be announced\n5. to be announced\n\n")

    root_index_content += ("{% include_relative grade.html %}\n\n")

    root_index_content += ("# Minnesota School Districts:\n\n")

    for district, schools in districts_dict.items():
        district_index_file_path = os.path.join(output_dir, district, "index.md")
        os.makedirs(os.path.join(output_dir, district), exist_ok=True)

        with open(district_index_file_path, 'w') as district_index_file:
            district_index_file.write(f"---\nlayout: page\ntitle: Schools in {district.replace('_', ' ')}\n---\n")
            district_index_file.write(
                f"# Navigation\n\n[[All countries/states/provinces]](../..) > [[All B.C. districts]](..)\n\n")
            district_index_file.write(f"# Schools in {district.replace('_', ' ')}\n\n")
            district_index_file.write("{% include_relative grade.html %}\n\n")
            district_index_file.write(f"**Schools:**\n\n")
            for school in schools:
                school_file_path = school
                district_index_file.write(f"- [{school.replace('_', ' ')}]({school_file_path}.md)\n")

        # Add to root index content with cleaner URLs
        root_index_content += f"- [{district.replace('_', ' ')}]({district}/): {len(schools)} schools\n"

    root_index_content += ("\n\n# Site ownership\n\nThis site is edited by volunteers who're "
                           "interested in accelerating the work to complete the adequate ventilation of Minnesota schools. "
                           "This effort was not commissioned by education authorities or government.\n\n"
                           "[Edit this page](https://github.com/ventilate-schools/MN/edit/main/index.md). See also [rules for contribution](./contribution_rules/)")

    # Write the root index file
    root_index_path = os.path.join(output_dir, "index.md")
    with open(root_index_path, 'w') as root_index_file:
        root_index_file.write(root_index_content)

# Call the function to create index markdown files and root index
create_area_and_root_index()

# Print confirmation
print("Index markdown files with front matter and links have been created in each area directory and root directory.")