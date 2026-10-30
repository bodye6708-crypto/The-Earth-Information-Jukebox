"""
Comprehensive Scientific Research & Observation Datasets
Authoritative Sources:
- NASA Goddard Institute for Space Studies (GISTEMP v4)
- NOAA Global Monitoring Laboratory (Mauna Loa Observatory)
- NASA Sea Level Change Team / CNES Satellite Altimetry
- NSIDC (National Snow and Ice Data Center)
- USGS Global Earthquake Hazards Program
- Smithsonian Global Volcanism Program
"""

CLIMATE_INDICATORS = [
    {
        "id": "global_temp",
        "titleEn": "Global Surface Temperature Anomaly",
        "titleAr": "شذوذ درجة حرارة سطح الأرض العالمية",
        "value": "+1.45 °C",
        "unit": "degrees Celsius relative to 1850-1900 baseline",
        "observationYear": 2024,
        "source": "NASA GISTEMP v4 / Copernicus ECMWF ERA5",
        "sourceUrl": "https://data.giss.nasa.gov/gistemp/",
        "descriptionEn": "Global mean surface temperature reached 1.45 ± 0.12 °C above the pre-industrial baseline (1850-1900), marking 2023-2024 as the hottest recorded period in observational history.",
        "descriptionAr": "بلغ متوسط شذوذ درجة حرارة السطح العالمية +1.45 درجة مئوية مقارنة بمعدلات ما قبل الثورة الصناعية، مسجلاً الفترة الأكثر حرارة في تاريخ الأرصاد العلمية الموثقة.",
        "category": "thermal"
    },
    {
        "id": "co2_concentration",
        "titleEn": "Atmospheric Carbon Dioxide (CO₂)",
        "titleAr": "تركيز ثاني أكسيد الكربون في الغلاف الجوي",
        "value": "422.80 ppm",
        "unit": "parts per million",
        "observationYear": 2024,
        "source": "NOAA Global Monitoring Laboratory (Mauna Loa, Hawaii)",
        "sourceUrl": "https://gml.noaa.gov/ccgg/trends/",
        "descriptionEn": "Direct in-situ air sampling at Mauna Loa Observatory recorded monthly mean CO₂ at ~422.8 ppm, compared to pre-industrial levels of ~280 ppm.",
        "descriptionAr": "سجلت عينات الهواء المباشرة في مرصد مونا لوا بهاواي تركيزاً شهرياً لغاز CO₂ بلغ 422.8 جزءاً في المليون، مقارنة بنحو 280 جزءاً في المليون قبل العصر الصناعي.",
        "category": "greenhouse_gas"
    },
    {
        "id": "sea_level_rise",
        "titleEn": "Global Mean Sea Level Trend",
        "titleAr": "معدل ارتفاع متوسط مستوى سطح البحر العالمي",
        "value": "+3.4 mm/year",
        "unit": "millimeters per year (+103 mm total since 1993)",
        "observationYear": 2024,
        "source": "NASA Sea Level Change / TOPEX & Jason Altimetry",
        "sourceUrl": "https://sealevel.nasa.gov/",
        "descriptionEn": "Continuous high-precision satellite altimetry records a steady sea level rise of 3.4 ± 0.4 mm/yr, accelerating compared to 20th-century tide gauge averages (~1.7 mm/yr).",
        "descriptionAr": "توثق مقاييس الارتفاع الرادارية بالأقمار الصناعية ارتفاعاً سنوياً مستمراً بمعدل 3.4 ملم/سنة، ناتجاً عن التمدد الحراري للمياه وذوبان الصفائح الجليدية.",
        "category": "ocean"
    },
    {
        "id": "antarctic_ice_mass",
        "titleEn": "Antarctic Continental Ice Sheet Mass Change",
        "titleAr": "تغير كتلة الصفيحة الجليدية لقارة أنتاركتيكا",
        "value": "-148 Gt/year",
        "unit": "Gigatons of ice lost per year",
        "observationYear": 2024,
        "source": "NASA GRACE and GRACE Follow-On Satellites",
        "sourceUrl": "https://climate.nasa.gov/vital-signs/ice-sheets/",
        "descriptionEn": "Satellite gravimetry measurements by GRACE show Antarctica has lost roughly ~150 gigatons of ice mass annually over the past two decades, predominantly in West Antarctica.",
        "descriptionAr": "تظهر قياسات الجاذبية الفضائية للقمرين التوأم جريس فقدان أنتاركتيكا لنحو 150 مليار طن من الجليد سنوياً، تتركز غالبيتها في غرب القارة القطبية.",
        "category": "cryosphere"
    },
    {
        "id": "arctic_sea_ice",
        "titleEn": "Arctic Summer Minimum Sea Ice Extent",
        "titleAr": "الحد الأدنى لمساحة الجليد البحري بالقطب الشمالي",
        "value": "4.28 million km²",
        "unit": "million square kilometers",
        "observationYear": 2024,
        "source": "NSIDC (National Snow and Ice Data Center)",
        "sourceUrl": "https://nsidc.org/arcticseaicenews/",
        "descriptionEn": "The September Arctic sea ice minimum extent has declined at an average decadal rate of ~12.2% relative to the 1981–2010 average.",
        "descriptionAr": "سجل الحد الأدنى الصيفي لمساحة الجليد في المحيط المتجمد الشمالي تراجعاً حاداً بمعدل 12.2% لكل عقد زمني مقارنة بمتوسطات الأعوام 1981-2010.",
        "category": "cryosphere"
    },
    {
        "id": "ocean_heat_content",
        "titleEn": "Ocean Heat Content (0–2000m depth)",
        "titleAr": "المحتوى الحراري للمحيطات (العمق من 0 إلى 2000 متر)",
        "value": "+384 ZJ",
        "unit": "Zettajoules (10²¹ Joules) above 1955-1960 baseline",
        "observationYear": 2024,
        "source": "NOAA NCEI Ocean Climate Laboratory / Argo Float Array",
        "sourceUrl": "https://www.ncei.noaa.gov/access/global-ocean-heat-content/",
        "descriptionEn": "The world's upper oceans absorbed over 90% of excess Earth system heating, reaching an unprecedented all-time high energy accumulation.",
        "descriptionAr": "امتصت محيطات العالم ما يزيد عن 90% من فائض الطاقة المحتبسة في مناخ الأرض، مسجلة أعلى سعة حرارية في تاريخ رصد مصفوفة مجسات أرغو.",
        "category": "ocean"
    }
]

HISTORICAL_CLIMATE_SERIES = [
    {"year": 1880, "anomaly": -0.16, "co2": 290.8, "seaLevel": -140.0, "note": "Beginning of reliable instrumental meteorological recording."},
    {"year": 1890, "anomaly": -0.36, "co2": 294.4, "seaLevel": -125.0, "note": "Late 19th-century volcanic cooling periods (Krakatoa aftermath)."},
    {"year": 1900, "anomaly": -0.08, "co2": 295.7, "seaLevel": -110.0, "note": "Turn of the 20th century baseline."},
    {"year": 1910, "anomaly": -0.42, "co2": 299.7, "seaLevel": -98.0, "note": "Katmai volcanic aerosols and solar minimum."},
    {"year": 1920, "anomaly": -0.27, "co2": 303.4, "seaLevel": -82.0, "note": "Early industrial expansion."},
    {"year": 1930, "anomaly": -0.14, "co2": 307.3, "seaLevel": -68.0, "note": "Pre-World War period expansion of weather stations."},
    {"year": 1940, "anomaly": 0.12, "co2": 311.3, "seaLevel": -52.0, "note": "Mid-century warming plateau."},
    {"year": 1950, "anomaly": -0.17, "co2": 311.0, "seaLevel": -40.0, "note": "Industrial aerosol emissions offsetting greenhouse forcing."},
    {"year": 1960, "anomaly": -0.03, "co2": 316.9, "seaLevel": -25.0, "note": "Beginning of high-precision Mauna Loa CO₂ monitoring."},
    {"year": 1970, "anomaly": 0.03, "co2": 325.7, "seaLevel": -15.0, "note": "Global meteorological satellite observation begins."},
    {"year": 1980, "anomaly": 0.26, "co2": 338.7, "seaLevel": 0.0, "note": "Onset of accelerated modern global warming trend."},
    {"year": 1990, "anomaly": 0.45, "co2": 354.4, "seaLevel": 16.0, "note": "First IPCC Assessment Report (FAR) published."},
    {"year": 2000, "anomaly": 0.40, "co2": 369.5, "seaLevel": 42.0, "note": "Satellite radar altimetry and Argo floats operational."},
    {"year": 2010, "anomaly": 0.72, "co2": 389.9, "seaLevel": 68.0, "note": "Marked acceleration of Arctic sea ice retreat."},
    {"year": 2015, "anomaly": 0.90, "co2": 400.8, "seaLevel": 82.0, "note": "Global CO₂ crosses 400 ppm milestone permanently."},
    {"year": 2020, "anomaly": 1.02, "co2": 414.2, "seaLevel": 94.0, "note": "Tied for warmest decade in human history."},
    {"year": 2023, "anomaly": 1.18, "co2": 421.1, "seaLevel": 100.0, "note": "Strong El Niño conditions amplify baseline warming."},
    {"year": 2024, "anomaly": 1.45, "co2": 422.8, "seaLevel": 103.4, "note": "Highest global average surface temperature on record (NASA/Copernicus)."}
]

GEOLOGICAL_CHAPTERS = [
    {
        "id": "formation",
        "titleEn": "1. Planetary Accretion & The Hadean Eon",
        "titleAr": "1. تشكل الكوكب والدهر الجهنمي (الجهنمي Hadean)",
        "timespan": "4.54 – 4.00 Billion Years Ago",
        "summaryEn": "Earth assembled through collisional gravitational accretion of planetesimals within the protoplanetary disk around the infant Sun.",
        "summaryAr": "تشكلت الأرض عبر التراكم الثقالي والاصطدامات العنيفة للكويكبات البدائية في القرص الكوكبي المحيط بالشمس الفتية.",
        "contentEn": "During the Hadean Eon (4.54 to 4.0 Ga), kinetic energy from continuous meteorite bombardment and radioactive decay kept Earth largely molten in a magma ocean. Core differentiation occurred rapidly as dense liquid iron-nickel sank to form the core, while lighter silicate melts formed the mantle. The Moon was born from the colossal impact with protoplanet Theia ~4.51 Ga. As the surface cooled, water vapor condensed from steam to form the first oceans ~4.4 Ga, evidenced by detrital zircon crystals from Jack Hills, Western Australia.",
        "contentAr": "خلال الدهر الجهنمي (قبل 4.54 إلى 4 مليارات عام)، أبقت الاصطدامات النيزكية المستمرة والحرارة الإشعاعية الأرض في حالة انصهار صهيري كامل. غاص الحديد والنيكل الكثيف لمركز الكوكب ليشكل اللب، بينما طفت السيليكات الخفيفة مكونة الوشاح. وُلد القمر إثر الاصطدام العملاق مع كويكب 'ثيا'. ومع انخفاض حرارة السطح، تكثف بخار الماء مكوّناً أول محيطات بدائية قبل 4.4 مليار سنة، وهو ما أثبتته بلورات الزركون العتيقة في تلال جاك هيلز بغرب أستراليا.",
        "sources": ["Valley et al., Nature Geoscience 2014 (Jack Hills zircons)", "NASA Astrobiology / Lunar and Planetary Institute"]
    },
    {
        "id": "archean",
        "titleEn": "2. Archean Eon & The Dawn of Life",
        "titleAr": "2. الدهر السحيق وبداية ظهور الحياة (Archean Eon)",
        "timespan": "4.00 – 2.50 Billion Years Ago",
        "summaryEn": "The emergence of the first anaerobic microbial life, primitive continents, and early biogenic stromatolites.",
        "summaryAr": "ظهور أول أشكال الحياة الميكروبية اللاهوائية وتكون الكراتونات القارية البدائية وبناء الستروماتوليت.",
        "contentEn": "In the anoxic Archean atmosphere dominated by N₂, CO₂, and CH₄, the earliest single-celled life arose in hydrothermal vents or shallow tidal pools (~3.8 to 3.5 Ga). Microbial mats created layered sedimentary structures called stromatolites. Towards the end of the Archean, ancestral cyanobacteria evolved oxygenic photosynthesis, using abundant water as an electron donor and releasing free molecular oxygen (O₂) as a byproduct, permanently setting the stage for Earth's atmospheric revolution.",
        "contentAr": "في ظل غلاف جوي خالٍ من الأكسجين تسوده غازات النيتروجين وثاني أكسيد الكربون والميثان، نشأت أول خلايا حية وحيدة الخلية قرب الفوهات البركانية المائية (قبل 3.8 إلى 3.5 مليار سنة). شكلت الكائنات الدقيقة مستعمرات كلسية طبقية تعرف بالستروماتوليت. وفي أواخر هذا الدهر، طورت البكتيريا الزرقاء قدرة البناء الضوئي المائي، مطلقة غاز الأكسجين (O₂) للمرة الأولى.",
        "sources": ["Schopf: Cradle of Life", "Geological Society of London Special Publications"]
    },
    {
        "id": "proterozoic",
        "titleEn": "3. Proterozoic Eon, GOE & Snowball Earth",
        "titleAr": "3. دهر الطلائع، حدث الأكسدة العظيم، والأرض كرة ثلجية",
        "timespan": "2.50 – 0.541 Billion Years Ago",
        "summaryEn": "Atmospheric oxygenation (GOE), eukaryotic cellular evolution, and extreme global cryogenian glaciations.",
        "summaryAr": "تأكسد الغلاف الجوي، وتطور الخلايا حقيقية النواة، والعصور الجليدية الشاملة (الأرض كرة ثلج).",
        "contentEn": "The Great Oxidation Event (~2.4–2.1 Ga) radically altered global geochemistry, oxidising oceanic dissolved iron into vast Banded Iron Formations (BIFs). The removal of atmospheric methane triggered the Huronian glaciation. Later in the Neoproterozoic Cryogenian Period (~720–635 Ma), runaway ice-albedo feedback encased almost the entire globe in ice ('Snowball Earth'). Intense volcanic CO₂ outgassing eventually broke the deep freeze, followed by the appearance of the enigmatic macroscopic Ediacaran biota.",
        "contentAr": "أدى حدث الأكسدة العظيم (قبل 2.4 - 2.1 مليار عام) إلى تحول جيوكيميائي جذري، حيث ترسب الحديد المحيطي في تشكيلات الحديد الشريطي (BIFs). وتسبب احتراق الميثان في عصر جليدي مبكر. وفي العصر الكريوجيني (قبل 720-635 مليون عام)، تجمد الكوكب بأكمله تقريباً في ظاهرة 'الأرض كرة ثلج'. وأنقذت انبعاثات البراكين لغاز CO₂ الكوكب من التجمد، ليعقب ذلك ظهور كائنات الإدياكارا المعقدة.",
        "sources": ["Hoffman et al., Science 1998", "Nature Geoscience / ICS International Chronostratigraphic Chart"]
    },
    {
        "id": "paleozoic",
        "titleEn": "4. Paleozoic Era & Colonization of Land",
        "titleAr": "4. حقبة الحياة القديمة (الباليوزوي) وغزو اليابسة",
        "timespan": "541 – 252 Million Years Ago",
        "summaryEn": "The Cambrian Explosion of animal phyla, land plant radiation, and the catastrophic Great Dying extinction.",
        "summaryAr": "الانفجار الكامبري للأصناف الحيوانية، انتشار الغابات البرية، وانقراض نهاية البرمي الأعظم.",
        "contentEn": "Beginning with the Cambrian explosion, all major animal body architectures (phyla) diversified rapidly in the oceans. During the Silurian and Devonian, vascular plants and arthropods colonized the continents, followed by tetrapods. Vast Carboniferous swamp forests laid down modern coal reserves while drawing down CO₂. The Paleozoic ended with the most devastating mass extinction in Earth history: the end-Permian extinction (~252 Ma), driven by massive Siberian Traps flood basalt volcanism that annihilated ~95% of marine species.",
        "contentAr": "بدأت الحقبة بالانفجار الكامبري الذي شهد ظهور كافة الشعب الحيوانية الرئيسية في البحار. وخلال العصرين السيلوري والديفوني، غزت النباتات الوعائية والبرمائيات الأولى اليابسة. وشكلت غابات العصر الكربوني الكثيفة مناجم الفحم الحجري الحالية. وانتهت الحقبة بأعنف انقراض جماعي في تاريخ الأرض (انقراض البرمي-الترياسي قبل 252 مليون سنة) حيث اندلعت براكين مصاطب سيبيريا وقضت على 95% من الكائنات البحرية.",
        "sources": ["Burgess et al., PNAS 2014 (Permian Extinction Timing)", "Smithsonian Paleobiology Database"]
    },
    {
        "id": "mesozoic",
        "titleEn": "5. Mesozoic Era: Age of Reptiles & Breakup of Pangaea",
        "titleAr": "5. حقبة الحياة الوسطى (الميزوزوي): عصر الديناصورات وتفكك بانجيا",
        "timespan": "252 – 66 Million Years Ago",
        "summaryEn": "The dominance of dinosaurs, flowering angiosperms, Pangaea rifting, and the Chicxulub asteroid impact.",
        "summaryAr": "سيادة الديناصورات، تفكك القارة العظمى بانجيا، وظهور الزهور، حتى اصطدام كويكب تشيكشولوب.",
        "contentEn": "Spanning the Triassic, Jurassic, and Cretaceous periods, the Mesozoic saw dinosaurs dominate terrestrial ecosystems while pterosaurs filled the skies and plesiosaurs ruled the warm shelf seas. Pangaea fragmented into Laurasia and Gondwana, opening the Atlantic Ocean. Angiosperms (flowering plants) transformed terrestrial floras in the Cretaceous. The era terminated abruptly 66.0 Ma when a ~10-km diameter asteroid impacted Chicxulub, Mexico, creating nuclear winter conditions that drove non-avian dinosaurs to extinction.",
        "contentAr": "شملت الحقبة العصور الترياسي والجوراسي والطباشيري (الكريتاسي)، وهيمن خلالها الديناصورات على اليابسة وتفككت قارة بانجيا إلى لوراسيا وغوندوانا لتولد المحيطات الحديثة. وفي العصر الطباشيري ظهرت النباتات الزهرية. وانتهت الحقبة فجأة قبل 66 مليون عام باصطدام كويكب تشيكشولوب العملاق (قطره 10 كم) في شبه جزيرة يوكاتان بالمكسيك، مسبباً شتاءً تصادمياً مظلماً أنهى عصر الديناصورات.",
        "sources": ["Alvarez et al., Science 1980", "Schulte et al., Science 2010 (Chicxulub Synthesis)"]
    },
    {
        "id": "cenozoic",
        "titleEn": "6. Cenozoic Era: Rise of Mammals & Quaternary Ice Ages",
        "titleAr": "6. حقبة الحياة الحديثة (السينوزوي): سيادة الثدييات والعصور الجليدية",
        "timespan": "66 Million Years Ago – Present Day",
        "summaryEn": "Mammalian radiation, Himalayan uplift, Antarctic glaciation, and hominin evolution.",
        "summaryAr": "ازدهار الثدييات، وتصادم الهند بآسيا وتكون الهيمالايا، ودورات الجليد الرباعية، وظهور الإنسان.",
        "contentEn": "Following the K-Pg extinction, surviving small mammals and birds radiated to fill ecological niches. The tectonic collision of the Indian subcontinent with Eurasia produced the Himalayas and Tibetan Plateau, initiating global cooling via silicate weathering. Antarctica developed its permanent ice cap ~34 Ma. The Quaternary period (past 2.6 Ma) has been defined by Milankovitch-paced orbital oscillations between glacial maxima and interglacials, during which genus Homo evolved and Homo sapiens emerged in Africa ~300,000 years ago.",
        "contentAr": "عقب انقراض K-Pg، تنوعت الثدييات الصغيرة والطيور لتملأ البيئات الشاغرة. وأدى اصطدام شبه القارة الهندية بآسيا لرفع جبال الهيمالايا وهضبة التبت، مما حفز تبريد الكوكب عبر تجوية السيليكات وتشكل غطاء أنتاركتيكا الجليدي قبل 34 مليون عام. واتسم العصر الرباعي (آخر 2.6 مليون سنة) بتعاقب العصور الجليدية والدافئة، وفيه تطور الجنس البشري وظهر الإنسان العاقل (Homo sapiens) في إفريقيا قبل نحو 300 ألف عام.",
        "sources": ["Zachos et al., Trends, Rhythms, and Aberrations in Global Climate 65 Ma to Present (Science)", "Hublin et al., Nature 2017 (Jebel Irhoud Homo sapiens)"]
    }
]

PEER_REVIEWED_PUBLICATIONS = [
    {
        "id": "pub_01",
        "title": "Global Surface Temperature Analysis (GISTEMP v4)",
        "authors": "Lenssen, N. J. L., G. A. Schmidt, J. E. Hansen, et al.",
        "journal": "Journal of Geophysical Research: Atmospheres",
        "year": 2019,
        "doi": "10.1029/2018JD029522",
        "url": "https://data.giss.nasa.gov/gistemp/references.html",
        "abstract": "Presents updated methodology for the NASA GISS Surface Temperature Analysis, incorporating NOAA GHCN v4 station records and ERSST v5 ocean observations with expanded uncertainty quantification.",
        "institution": "NASA Goddard Institute for Space Studies"
    },
    {
        "id": "pub_02",
        "title": "IPCC Sixth Assessment Report (AR6): The Physical Science Basis",
        "authors": "Intergovernmental Panel on Climate Change (IPCC)",
        "journal": "Cambridge University Press",
        "year": 2021,
        "doi": "10.1017/9781009157896",
        "url": "https://www.ipcc.ch/report/ar6/wg1/",
        "abstract": "Comprehensive scientific assessment of past, present, and future planetary climate changes, radiative forcing, ocean heating, and cryosphere dynamics compiled by hundreds of leading international researchers.",
        "institution": "WMO / UNEP"
    },
    {
        "id": "pub_03",
        "title": "Eight Glacial Cycles from an Antarctic Ice Core (EPICA Dome C)",
        "authors": "EPICA Community Members",
        "journal": "Nature",
        "year": 2004,
        "doi": "10.1038/nature02599",
        "url": "https://www.nature.com/articles/nature02599",
        "abstract": "Reports the continuous 3,190-meter ice core from Dome C in East Antarctica, extending direct records of atmospheric greenhouse gas concentrations and isotopic temperature proxies across 740,000 years.",
        "institution": "European Project for Ice Coring in Antarctica"
    },
    {
        "id": "pub_04",
        "title": "Mass balance of the Antarctic Ice Sheet from 1992 to 2017 (IMBIE)",
        "authors": "The IMBIE Team (Shepherd, A., et al.)",
        "journal": "Nature",
        "year": 2018,
        "doi": "10.1038/s41586-018-0179-y",
        "url": "https://www.nature.com/articles/s41586-018-0179-y",
        "abstract": "Reconciled estimate from 24 independent satellite survey estimates showing that Antarctica lost 2,720 ± 1,390 billion tonnes of ice between 1992 and 2017, corresponding to an increase in global mean sea level.",
        "institution": "ESA / NASA Ice Sheet Mass Balance Inter-comparison Exercise"
    },
    {
        "id": "pub_05",
        "title": "The Chicxulub Asteroid Impact and Mass Extinction at the Cretaceous-Paleogene Boundary",
        "authors": "Schulte, P., Alegret, L., Arenillas, I., et al.",
        "journal": "Science",
        "year": 2010,
        "doi": "10.1126/science.1177265",
        "url": "https://www.science.org/doi/10.1126/science.1177265",
        "abstract": "Synthesis of stratigraphical, micropaleontological, geochemical, and geodynamic evidence confirming the single, synchronous ~10-km asteroid impact at Chicxulub as the definitive cause of the K-Pg mass extinction.",
        "institution": "International Geological Research Consortium"
    }
]

COUNTRY_PROFILES = [
    {
        "code": "EGY",
        "nameEn": "Egypt",
        "nameAr": "مصر",
        "capital": "Cairo",
        "continent": "Africa / Asia (Sinai)",
        "coordinates": {"lat": 26.8206, "lng": 30.8025},
        "established": "c. 3100 BCE (First Dynasty Unification under Narmer); 1922 (Modern Independence)",
        "areaKm2": 1002450,
        "climateClass": "BWh (Hyper-arid Hot Desert) / Csa (Mediterranean Coast)",
        "meanAnnualTemp": "22.1 °C",
        "geographySummaryEn": "Home to the lower Nile River valley and delta, bordering the Mediterranean Sea and Red Sea, cradling one of the world's earliest riverine civilizations.",
        "geographySummaryAr": "موطن وادي ودلتا نهر النيل، تشرف على البحرين المتوسط والأحمر، وتعد مهداً لواحدة من أقدم الحضارات الإنسانية المستقرة في التاريخ.",
        "source": "FAO Aquastat / Egyptian Meteorological Authority / World Bank Climate Portal"
    },
    {
        "code": "SAU",
        "nameEn": "Saudi Arabia",
        "nameAr": "المملكة العربية السعودية",
        "capital": "Riyadh",
        "continent": "Asia",
        "coordinates": {"lat": 23.8859, "lng": 45.0792},
        "established": "1744 (First Saudi State); 1932 (Unification under King Abdulaziz)",
        "areaKm2": 2149690,
        "climateClass": "BWh (Arid Subtropical Desert) / As (Asir Montane)",
        "meanAnnualTemp": "25.3 °C",
        "geographySummaryEn": "Occupies roughly 80% of the Arabian Peninsula, containing the vast Rub' al Khali (Empty Quarter) desert and the Arabian Shield geological formation.",
        "geographySummaryAr": "تشغل نحو 80% من شبه الجزيرة العربية، وتضم صحراء الربع الخالي الشاسعة وتكوينات الدرع العربي الجيولوجي القديم الغني بالمعادن.",
        "source": "Saudi Geological Survey / National Center for Meteorology"
    },
    {
        "code": "USA",
        "nameEn": "United States",
        "nameAr": "الولايات المتحدة الأمريكية",
        "capital": "Washington, D.C.",
        "continent": "North America",
        "coordinates": {"lat": 37.0902, "lng": -95.7129},
        "established": "July 4, 1776 (Declaration of Independence)",
        "areaKm2": 9833517,
        "climateClass": "Diverse: Dfb/Cfa (East), BSk/BWh (West), Csb (Pacific Coast), ET (Alaska)",
        "meanAnnualTemp": "11.6 °C",
        "geographySummaryEn": "Stretches from the Atlantic to Pacific oceans, featuring the Rocky Mountains, Mississippi River Basin, Great Lakes, and arctic Alaska.",
        "geographySummaryAr": "تمتد بين المحيطين الأطلسي والهادئ، وتتميز بسلاسل جبال روكي وحوض المسيسيبي والبحيرات العظمى وبراري ألاسكا القطبية.",
        "source": "USGS / NOAA National Centers for Environmental Information"
    },
    {
        "code": "BRA",
        "nameEn": "Brazil",
        "nameAr": "البرازيل",
        "capital": "Brasília",
        "continent": "South America",
        "coordinates": {"lat": -14.2350, "lng": -51.9253},
        "established": "September 7, 1822 (Independence from Portugal)",
        "areaKm2": 8515767,
        "climateClass": "Af/Am (Equatorial Amazonian Rain Forest), Aw (Tropical Savanna/Cerrado)",
        "meanAnnualTemp": "25.0 °C",
        "geographySummaryEn": "Largest country in South America, containing the majority of the Amazon River basin and rainforest, holding unmatched global biodiversity.",
        "geographySummaryAr": "أكبر دول أمريكا الجنوبية، وتحتضن الجزء الأعظم من حوض وغابات الأمازون المطيرة وأغنى مستودع للتنوع البيولوجي على وجه الأرض.",
        "source": "INPE (National Institute for Space Research Brazil) / IBGE"
    },
    {
        "code": "NOR",
        "nameEn": "Norway",
        "nameAr": "النرويج",
        "capital": "Oslo",
        "continent": "Europe",
        "coordinates": {"lat": 60.4720, "lng": 8.4689},
        "established": "c. 872 CE (Unification under Harald Fairhair); 1905 (Dissolution of Union)",
        "areaKm2": 385207,
        "climateClass": "Cfb/Cfc (Marine West Coast moderated by Gulf Stream) / ET (Tundra/Svalbard)",
        "meanAnnualTemp": "4.2 °C",
        "geographySummaryEn": "Renowned for deeply incised glacial fjords, Scandinavian mountain chain, and extensive arctic archipelago of Svalbard.",
        "geographySummaryAr": "تشتهر بسواحل المضايق الجليدية العميقة (Fjords) وسلسلة الجبال الإسكندنافية وأرخبيل سفالبارد القطبي ومخزن البذور العالمي.",
        "source": "Norwegian Meteorological Institute / Geological Survey of Norway"
    }
]
