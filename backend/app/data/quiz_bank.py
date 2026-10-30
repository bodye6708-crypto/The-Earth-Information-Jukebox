"""
Comprehensive 100-Question Scientific Earth Science Question Bank
Strictly validated: 10 Levels x 10 Questions = 100 Questions total.
Progression:
Level 1: Basic knowledge about Earth
Level 2: Continents, oceans, geographical features
Level 3: Earth rotation, revolution, and seasons
Level 4: Solar System and basic astronomy
Level 5: Atmosphere, weather, and pressure
Level 6: Climate and geological processes
Level 7: Oceans, ecosystems, and environmental science
Level 8: Scientific charts and data interpretation
Level 9: Earth systems and biogeochemical cycles
Level 10: Expert Earth Science reasoning & geophysics
"""

QUIZ_LEVELS = [
    {
        "level": 1,
        "titleEn": "Level 1: Basic Knowledge About Earth",
        "titleAr": "المستوى 1: المعرفة الأساسية بكوكب الأرض",
        "difficulty": "very_easy",
        "questions": [
            {
                "id": 1,
                "qEn": "What is the approximate shape of the Earth?",
                "qAr": "ما هو الشكل الهندسي التقريبي الحقيقي لكوكب الأرض؟",
                "optionsEn": ["Perfect sphere", "Oblate spheroid", "Flat disc", "Cylinder"],
                "optionsAr": ["كرة مثالية تماماً", "شبه كروي مفلطح (بيضاوي)", "قرص مسطح", "أسطواني"],
                "correct": 1,
                "explanationEn": "Earth rotates on its axis, generating centrifugal force that causes it to bulge at the equator and flatten slightly at the poles (oblate spheroid).",
                "explanationAr": "تدور الأرض حول محورها، وتؤدي قوة الطرد المركزي إلى انتفاخها قليلاً عند خط الاستواء وتفلطحها عند القطبين (مجسم شبه كروي مفلطح).",
                "source": "NASA Earth Science / geodesy.noaa.gov"
            },
            {
                "id": 2,
                "qEn": "Approximately what percentage of the Earth's surface is covered by water?",
                "qAr": "ما هي النسبة المئوية التقريبية لمساحة سطح الأرض المغطاة بالمياه؟",
                "optionsEn": ["About 50%", "About 71%", "About 85%", "About 92%"],
                "optionsAr": ["حوالي 50%", "حوالي 71%", "حوالي 85%", "حوالي 92%"],
                "correct": 1,
                "explanationEn": "Water bodies (oceans, seas, lakes, rivers, and ice) cover roughly 70.8% of Earth's total surface area.",
                "explanationAr": "تغطي المسطحات المائية (المحيطات والبحار والبحيرات والأنهار والجليد) حوالي 70.8% من إجمالي مساحة سطح الأرض.",
                "source": "USGS Water Science School"
            },
            {
                "id": 3,
                "qEn": "What is the third planet from the Sun in our Solar System?",
                "qAr": "ما هو الكوكب الثالث بُعداً عن الشمس في مجموعتنا الشمسية؟",
                "optionsEn": ["Mars", "Venus", "Earth", "Mercury"],
                "optionsAr": ["المريخ", "الزهرة", "الأرض", "عطارد"],
                "correct": 2,
                "explanationEn": "Starting from the Sun, the planets are Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune.",
                "explanationAr": "بالترتيب ابتداءً من الشمس: عطارد، ثم الزهرة، ثم الأرض كالكوكب الثالث، ثم المريخ، المشتري، زحل، أورانوس، ونبتون.",
                "source": "NASA Planetary Fact Sheet"
            },
            {
                "id": 4,
                "qEn": "What is the outermost solid mechanical layer of Earth called?",
                "qAr": "ماذا يُطلق على الطبقة الخارجية الصلبة ميكانيكياً لكوكب الأرض؟",
                "optionsEn": ["Crust", "Outer Core", "Asthenosphere", "Inner Core"],
                "optionsAr": ["القشرة الأرضية (Crust)", "اللب الخارجي", "الغلاف الموري (Asthenosphere)", "اللب الداخلي"],
                "correct": 0,
                "explanationEn": "The crust is the thin, solid outermost layer of Earth, ranging from 5 km under oceans to 70 km beneath mountains.",
                "explanationAr": "القشرة هي الطبقة الخارجية الصلبة للأرض، ويتراوح سمكها من نحو 5 كم تحت قيعان المحيطات إلى 70 كم تحت سلاسل الجبال.",
                "source": "USGS Inside the Earth"
            },
            {
                "id": 5,
                "qEn": "What is the primary gas composing Earth's dry atmosphere by volume?",
                "qAr": "ما هو الغاز الرئيسي المكوّن للغلاف الجوي الجاف للأرض من حيث الحجم؟",
                "optionsEn": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Argon"],
                "optionsAr": ["الأكسجين", "النيتروجين", "ثاني أكسيد الكربون", "الأرجون"],
                "correct": 1,
                "explanationEn": "Nitrogen makes up approximately 78.08% of Earth's dry atmosphere by volume, while oxygen constitutes 20.95%.",
                "explanationAr": "يشكل النيتروجين نحو 78.08% من حجم الهواء الجاف، بينما يمثل الأكسجين حوالي 20.95%.",
                "source": "NOAA Earth System Research Laboratories"
            },
            {
                "id": 6,
                "qEn": "How many natural permanent moons orbit the planet Earth?",
                "qAr": "كم قمراً طبيعياً دائماً يدور حول كوكب الأرض؟",
                "optionsEn": ["Zero", "Exactly One", "Two", "Four"],
                "optionsAr": ["صفر", "قمر واحد فقط", "اثنان", "أربعة"],
                "correct": 1,
                "explanationEn": "Earth has exactly one natural permanent satellite, commonly known simply as the Moon (Luna).",
                "explanationAr": "تمتلك الأرض قمراً طبيعياً دائماً واحداً فقط، وهو القمر التابع (Luna).",
                "source": "NASA Lunar Science"
            },
            {
                "id": 7,
                "qEn": "What is the accepted approximate age of the Earth based on radiometric dating of meteorites?",
                "qAr": "ما هو العمر العلمي التقريبي المقبول لكوكب الأرض بناءً على التأريخ الإشعاعي للنيازك؟",
                "optionsEn": ["2.1 billion years", "4.54 billion years", "6.2 billion years", "10 billion years"],
                "optionsAr": ["2.1 مليار سنة", "4.54 مليار سنة", "6.2 مليار سنة", "10 مليارات سنة"],
                "correct": 1,
                "explanationEn": "Radiometric dating of the oldest known Earth minerals and Solar System meteorites confirms Earth formed ~4.54 ± 0.05 billion years ago.",
                "explanationAr": "أثبتت قياسات التأريخ الإشعاعي لأقدم صخور ومعادن النيازك في النظام الشمسي أن عمر الأرض يقدر بنحو 4.54 مليار سنة.",
                "source": "USGS Geologic Time / Nature Geoscience"
            },
            {
                "id": 8,
                "qEn": "What force holds Earth's atmosphere from escaping into space?",
                "qAr": "ما هي القوة الفيزيائية التي تمنع الغلاف الجوي للأرض من الهروب إلى الفضاء الخارجي؟",
                "optionsEn": ["Magnetic field", "Gravitational force", "Centrifugal force", "Solar wind"],
                "optionsAr": ["المجال المغناطيسي", "قوة الجاذبية الأرضية", "قوة الطرد المركزي", "الرياح الشمسية"],
                "correct": 1,
                "explanationEn": "Earth's mass creates a gravitational field strong enough to retain atmospheric gases whose thermal velocities remain below escape velocity.",
                "explanationAr": "تولد كتلة الأرض حقلاً تجاذبياً كافياً لاحتجاز جزيئات الغاز طالما كانت سرعتها الحرارية أقل من سرعة الإفلات.",
                "source": "NASA Glenn Research Center"
            },
            {
                "id": 9,
                "qEn": "What state of matter forms Earth's inner core?",
                "qAr": "ما هي الحالة الفيزيائية للمادة التي يتكون منها اللب الداخلي للأرض؟",
                "optionsEn": ["Liquid iron", "Solid crystalline iron-nickel", "Gaseous plasma", "Molten silicate magma"],
                "optionsAr": ["حديد سائل", "حديد ونيكل بلوري صلب", "بلازما غازية", "صهير سيليكاتي سائل"],
                "correct": 1,
                "explanationEn": "Despite extreme temperatures (~5,400°C), immense hydrostatic pressure (~330 to 360 GPa) forces the inner core into a solid crystalline state.",
                "explanationAr": "رغم الحرارة الهائلة (~5400 مئوية)، فإن الضغط الفائق (330-360 جيجا باسكال) يحافظ على اللب الداخلي في حالة صلبة متماسكة.",
                "source": "USGS Geophysics / Earth and Planetary Science Letters"
            },
            {
                "id": 10,
                "qEn": "Which imaginary line divides the Earth into the Northern and Southern Hemispheres?",
                "qAr": "ما هو الخط الوهمي الذي يقسم كوكب الأرض إلى نصف شمالي ونصف جنوبي؟",
                "optionsEn": ["Prime Meridian", "Equator", "Tropic of Cancer", "Arctic Circle"],
                "optionsAr": ["خط غرينتش", "خط الاستواء (Equator)", "مدار السرطان", "الدائرة القطبية الشمالية"],
                "correct": 1,
                "explanationEn": "The Equator is the line of 0 degrees latitude equidistant from both geographical poles, dividing Earth into Northern and Southern Hemispheres.",
                "explanationAr": "خط الاستواء هو دائرة العرض صفر التي تقع على مسافة متساوية من القطبين وتقسم الأرض لنصفين شمالي وجنوبي.",
                "source": "National Geographic Education"
            }
        ]
    },
    {
        "level": 2,
        "titleEn": "Level 2: Continents, Oceans & Geography",
        "titleAr": "المستوى 2: القارات والمحيطات وتضاريس الأرض",
        "difficulty": "easy",
        "questions": [
            {
                "id": 11,
                "qEn": "What is the largest ocean on Earth by surface area and volume?",
                "qAr": "ما هو أكبر محيطات كوكب الأرض من حيث المساحة والحجم المائي؟",
                "optionsEn": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"],
                "optionsAr": ["المحيط الأطلسي", "المحيط الهندي", "المحيط الهادئ (Pacific)", "المحيط المتجمد الشمالي"],
                "correct": 2,
                "explanationEn": "The Pacific Ocean covers over 165 million square kilometers, covering roughly one-third of the planet's surface.",
                "explanationAr": "يمتد المحيط الهادئ على مساحة تتجاوز 165 مليون كيلومتر مربع، ما يعادل ثلث إجمالي مساحة سطح كوكب الأرض بأكمله.",
                "source": "NOAA National Ocean Service"
            },
            {
                "id": 12,
                "qEn": "What is the highest mountain peak above sea level on Earth?",
                "qAr": "ما هي أعلى قمة جبلية فوق مستوى سطح البحر على كوكب الأرض؟",
                "optionsEn": ["K2", "Mount Kilimanjaro", "Mount Everest", "Denali"],
                "optionsAr": ["قمة K2", "جبل كليمنجارو", "جبل إفرست (Everest)", "قمة دينالي"],
                "correct": 2,
                "explanationEn": "Mount Everest in the Himalayas rises to an officially recognized elevation of 8,848.86 meters above sea level.",
                "explanationAr": "ترتفع قمة إفرست في سلسلة جبال الهيمالايا إلى 8848.86 متراً فوق مستوى سطح البحر المعتمد دولياً.",
                "source": "Survey Department of Nepal & National Bureau of Surveying and Mapping China"
            },
            {
                "id": 13,
                "qEn": "What is the deepest verified trench and point in the world's oceans?",
                "qAr": "ما هو أعمق خندق ونقطة مسجلة في محيطات العالم؟",
                "optionsEn": ["Java Trench", "Mariana Trench (Challenger Deep)", "Puerto Rico Trench", "Romanche Trench"],
                "optionsAr": ["خندق جاوة", "خندق ماريانا (نقطة تشالنجر)", "خندق بورتوريكو", "خندق رومانش"],
                "correct": 1,
                "explanationEn": "Challenger Deep in the Mariana Trench reaches an extreme oceanic depth of approximately 10,928 to 10,994 meters below sea level.",
                "explanationAr": "يصل عمق نقطة تشالنجر في خندق ماريانا إلى ما بين 10,928 و 10,994 متراً تحت مستوى سطح البحر.",
                "source": "NOAA Ocean Exploration / GEBCO Bathymetry"
            },
            {
                "id": 14,
                "qEn": "Which continent is completely surrounded by the Southern Ocean and covered by an ice sheet?",
                "qAr": "أي قارة محاطة بالكامل بالمحيط الجنوبي وتغطيها طبقة جليدية قارية عملاقة؟",
                "optionsEn": ["Greenland", "Antarctica", "Australia", "Eurasia"],
                "optionsAr": ["غرينلاند", "القارة القطبية الجنوبية (أنتاركتيكا)", "أستراليا", "أوراسيا"],
                "correct": 1,
                "explanationEn": "Antarctica is the fifth largest continent, covered by an ice sheet containing roughly 90% of the world's ice and 70% of Earth's fresh water.",
                "explanationAr": "أنتاركتيكا مغطاة بصفائح جليدية هائلة تضم قرابة 90% من جليد العالم و70% من إجمالي المياه العذبة على الأرض.",
                "source": "British Antarctic Survey / NASA Cryospheric Sciences"
            },
            {
                "id": 15,
                "qEn": "What is the longest river system on Earth by total channel length?",
                "qAr": "ما هو أطول نظام نهري على وجه الأرض من حيث طول المجرى الرئيسي؟",
                "optionsEn": ["Yangtze River", "Mississippi-Missouri River", "Nile River", "Danube River"],
                "optionsAr": ["نهر يانغتسي", "نهر المسيسيبي-ميسوري", "نهر النيل (Nile)", "نهر الدانوب"],
                "correct": 2,
                "explanationEn": "The Nile River in northeastern Africa extends roughly 6,650 km (4,132 miles), making it traditionally recognized as Earth's longest river.",
                "explanationAr": "يمتد نهر النيل في شمال شرق إفريقيا لنحو 6,650 كم، وهو المعترف به كأطول أنهار كوكب الأرض.",
                "source": "Encyclopaedia Britannica / USGS River Basins"
            },
            {
                "id": 16,
                "qEn": "What is the largest hot desert on Earth?",
                "qAr": "ما هي أكبر صحراء رملية حارة جافة في العالم؟",
                "optionsEn": ["Gobi Desert", "Kalahari Desert", "Sahara Desert", "Arabian Desert"],
                "optionsAr": ["صحراء غوبي", "صحراء كالاهاري", "الصحراء الكبرى (Sahara)", "صحراء الربع الخالي"],
                "correct": 2,
                "explanationEn": "The Sahara covers over 9.2 million square kilometers across North Africa, roughly the size of the entire United States or China.",
                "explanationAr": "تمتد الصحراء الكبرى على مساحة تفوق 9.2 مليون كيلومتر مربع عبر شمال إفريقيا.",
                "source": "USGS Land Cover Institute"
            },
            {
                "id": 17,
                "qEn": "Which continent consists of the fewest number of sovereign countries?",
                "qAr": "أي قارة تضم أقل عدد من الدول المستقلة ذات السيادة؟",
                "optionsEn": ["South America", "Australia / Oceania", "Antarctica (0 countries under Treaty)", "Europe"],
                "optionsAr": ["أمريكا الجنوبية", "أوقيانوسيا", "أنتاركتيكا (صفر دول طبقاً لمعاهدة القطب الجنوبي)", "أوروبا"],
                "correct": 2,
                "explanationEn": "Antarctica has no sovereign nations or permanent human population, governed strictly under the international Antarctic Treaty System of 1959.",
                "explanationAr": "أنتاركتيكا لا تضم أي دولة مستقلة ذات سيادة وتخضع للإدارة الدولية بموجب معاهدة القطب الجنوبي لعام 1959 للأغراض العلمية والسلام.",
                "source": "Secretariat of the Antarctic Treaty"
            },
            {
                "id": 18,
                "qEn": "The Caspian Sea is technically classified in geography and limnology as what?",
                "qAr": "ما هو التصنيف الجغرافي والليمونولوجي الدقيق لبحر قزوين؟",
                "optionsEn": ["An open arm of the Arctic Ocean", "The world's largest endorheic lake", "A freshwater tectonic fjord", "A submarine valley"],
                "optionsAr": ["ذراع مفتوح للمحيط المتجمد", "أكبر بحيرة مغلقة (حوض حبيس) في العالم", "مضيق مائي تكتوني عذب", "وادٍ محيطي غاطس"],
                "correct": 1,
                "explanationEn": "The Caspian Sea is completely landlocked without natural ocean outlets, making it the largest enclosed inland body of water (endorheic lake).",
                "explanationAr": "بحر قزوين حوض مغلق تماماً عن المحيطات المفتوحة، ولذلك يعد جغرافياً وعلمياً أكبر بحيرة مغلقة على وجه الأرض.",
                "source": "NASA Earth Observatory / UNEP"
            },
            {
                "id": 19,
                "qEn": "Which strait connects the Atlantic Ocean to the Mediterranean Sea?",
                "qAr": "ما هو المضيق المائي الاستراتيجي الذي يربط المحيط الأطلسي بالبحر الأبيض المتوسط؟",
                "optionsEn": ["Strait of Hormuz", "Strait of Malacca", "Strait of Gibraltar", "Bering Strait"],
                "optionsAr": ["مضيق هرمز", "مضيق ملقا", "مضيق جبل طارق (Gibraltar)", "مضيق بيرنغ"],
                "correct": 2,
                "explanationEn": "The Strait of Gibraltar connects the Atlantic Ocean to the Mediterranean Sea and separates the Iberian Peninsula from North Africa.",
                "explanationAr": "يربط مضيق جبل طارق بين المحيط الأطلسي والبحر الأبيض المتوسط، ويفصل بين شبه الجزيرة الأيبيرية وشمال إفريقيا.",
                "source": "International Hydrographic Organization"
            },
            {
                "id": 20,
                "qEn": "The Ring of Fire around the Pacific Ocean basin is famous for containing what proportion of Earth's volcanoes and earthquakes?",
                "qAr": "تشتهر منطقة 'حزام النار' حول المحيط الهادئ باحتوائها على أي نسبة من زلازل وبراكين الأرض؟",
                "optionsEn": ["About 25%", "About 50%", "Over 75% of active volcanoes and ~90% of earthquakes", "Exactly 100%"],
                "optionsAr": ["حوالي 25%", "حوالي 50%", "أكثر من 75% من البراكين النشطة وقرابة 90% من الزلازل", "100% تماماً"],
                "correct": 2,
                "explanationEn": "The Pacific Rim of Fire accounts for roughly 75% of all active subaerial volcanoes and ~90% of the world's recorded earthquakes due to subducting plates.",
                "explanationAr": "يضم حزام النار المحيطي نحو 75% من براكين العالم النشطة وحوالي 90% من زلازله نتيجة انغراز الصفائح التكتونية.",
                "source": "USGS Earthquake Hazards Program"
            }
        ]
    },
    {
        "level": 3,
        "titleEn": "Level 3: Rotation, Revolution & Seasons",
        "titleAr": "المستوى 3: دوران الأرض والمواسم وفصول السنة",
        "difficulty": "easy_intermediate",
        "questions": [
            {
                "id": 21,
                "qEn": "What is the primary cause of Earth's recurring seasons throughout the year?",
                "qAr": "ما هو السبب الفيزيائي الفلكي الرئيسي لحدوث الفصول الأربعة على كوكب الأرض؟",
                "optionsEn": ["Varying distance to the Sun", "Axial tilt of ~23.44 degrees relative to the orbital plane", "Changes in solar luminosity", "Precession of the equinoxes"],
                "optionsAr": ["تغير المسافة بين الأرض والشمس", "ميل محور دوران الأرض بنحو 23.44 درجة بالنسبة لمستوى المدار", "تغير الإشعاع الشمسي الصادر", "ترنح المحور في الفضاء"],
                "correct": 1,
                "explanationEn": "Seasons occur because Earth's rotational axis is tilted 23.44°, altering the angle of incidence and duration of sunlight as it orbits the Sun.",
                "explanationAr": "تنشأ الفصول بسبب ميل محور دوران الأرض بزاوية 23.44 درجة، مما يغير زاوية سقوط أشعة الشمس وطول النهار خلال دورانها السنوي.",
                "source": "NASA Space Place / NOAA Climate.gov"
            },
            {
                "id": 22,
                "qEn": "How long does it take for Earth to complete one full sidereal rotation relative to distant stars?",
                "qAr": "كم يستغرق دوران الأرض دورة كاملة بالنسبة للنجوم البعيدة (اليوم النجمي Sidereal Day)؟",
                "optionsEn": ["24 hours 00 minutes 00 seconds", "23 hours 56 minutes 4.1 seconds", "24 hours 56 minutes", "23 hours 12 minutes"],
                "optionsAr": ["24 ساعة تماماً", "23 ساعة و56 دقيقة و4.1 ثانية", "24 ساعة و56 دقيقة", "23 ساعة و12 دقيقة"],
                "correct": 1,
                "explanationEn": "A sidereal day is approximately 23 hours, 56 minutes, and 4.0905 seconds. The 24-hour solar day accounts for Earth's orbital advancement around the Sun.",
                "explanationAr": "اليوم النجمي للأرض يبلغ 23 ساعة و56 دقيقة و4.09 ثانية، بينما اليوم الشمسي 24 ساعة لتعويض تقدم الأرض في مدارها حول الشمس.",
                "source": "IERS (International Earth Rotation and Reference Systems Service)"
            },
            {
                "id": 23,
                "qEn": "What is the term for the point in Earth's elliptical orbit where it is closest to the Sun?",
                "qAr": "ما هو المصطلح الفلكي للنقطة التي تكون فيها الأرض في أقرب مسافة لها من الشمس في مدارها البيضاوي؟",
                "optionsEn": ["Aphelion", "Perihelion", "Perigee", "Apogee"],
                "optionsAr": ["الأوج (Aphelion)", "الحضيض الشمسي (Perihelion)", "حضيض القمر (Perigee)", "أوج القمر (Apogee)"],
                "correct": 1,
                "explanationEn": "Perihelion occurs around January 3–5 each year when Earth is about 147.1 million km from the Sun, compared to aphelion (152.1M km) in July.",
                "explanationAr": "الحضيض الشمسي يحدث في أوائل يناير حين تصبح الأرض على بعد 147.1 مليون كم من الشمس، بينما الأوج في أوائل يوليو على بعد 152.1 مليون كم.",
                "source": "US Naval Observatory Astronomical Applications"
            },
            {
                "id": 24,
                "qEn": "On which two days of the year do day and night have approximately equal duration globally?",
                "qAr": "في أي يومين من العام يتساوى طول الليل والنهار تقريباً في جميع أنحاء كوكب الأرض؟",
                "optionsEn": ["Summer and Winter Solstices", "Vernal and Autumnal Equinoxes", "Perihelion and Aphelion", "Lunar eclipse dates"],
                "optionsAr": ["الانقلاب الصيفي والانقلاب الشتوي", "الاعتدال الربيعي والاعتدال الخريفي (Equinoxes)", "الحضيض والأوج", "أيام خسوف القمر"],
                "correct": 1,
                "explanationEn": "During the equinoxes (~March 20 and ~September 22), the Sun crosses the celestial equator and shines directly over the equator, equalizing day and night.",
                "explanationAr": "أثناء الاعتدالين (حوالي 20 مارس و 22 سبتمبر) تتعامد الشمس على خط الاستواء مباشرة ليتساوى الليل والنهار في سائر الكوكب.",
                "source": "NASA Earth Observatory"
            },
            {
                "id": 25,
                "qEn": "Why is a leap year with 366 days added to the Gregorian calendar every four years (with century exceptions)?",
                "qAr": "لماذا تضاف سنة كبيسة تحتوي على 366 يوماً كل أربع سنوات في التقويم الشمسي؟",
                "optionsEn": ["Earth's rotation slows down by 1 hour", "Earth's tropical orbit takes ~365.2422 days", "The Moon's orbit creates a gap", "To match Mars year cycle"],
                "optionsAr": ["لأن دوران الأرض يبطؤ ساعة كل عام", "لأن السنة الشمسية المدارية الحقيقية تستغرق حوالي 365.2422 يوماً", "بسبب فارق مدار القمر", "لمزامنة التقويم مع كوكب المريخ"],
                "correct": 1,
                "explanationEn": "Earth takes ~365.2422 solar days to orbit the Sun. Adding one extra day every 4 years (minus century years not divisible by 400) keeps calendar seasons aligned.",
                "explanationAr": "تستغرق دورة الأرض حول الشمس حوالي 365.2422 يوماً. وإضافة يوم كل 4 سنوات يحفظ توافق التقويم المدني مع الفصول الطبيعية.",
                "source": "National Institute of Standards and Technology (NIST)"
            },
            {
                "id": 26,
                "qEn": "In which direction does the planet Earth rotate when viewed looking down from above the North Pole?",
                "qAr": "في أي اتجاه تدور الأرض حول محورها إذا نظرنا إليها من الفضاء فوق القطب الشمالي؟",
                "optionsEn": ["Clockwise", "Counter-clockwise (prograde)", "Alternating every 6 months", "North to South"],
                "optionsAr": ["في اتجاه عقارب الساعة", "عكس اتجاه عقارب الساعة (Prograde)", "تتبدل كل 6 أشهر", "من الشمال إلى الجنوب"],
                "correct": 1,
                "explanationEn": "Looking down from above the North Pole, Earth rotates counter-clockwise from west to east, causing the Sun and celestial bodies to appear to rise in the east.",
                "explanationAr": "عند النظر من فوق القطب الشمالي تدور الأرض من الغرب نحو الشرق (عكس عقارب الساعة)، ولذلك تبدو الشمس تشرق من الشرق.",
                "source": "NASA Jet Propulsion Laboratory"
            },
            {
                "id": 27,
                "qEn": "What is the approximate speed of Earth's rotational surface motion at the Equator?",
                "qAr": "ما هي السرعة الخطية التقريبية لحركة سطح الأرض الناتجة عن الدوران عند خط الاستواء؟",
                "optionsEn": ["100 km/h", "500 km/h", "1,670 km/h (~465 m/s)", "10,000 km/h"],
                "optionsAr": ["100 كم/ساعة", "500 كم/ساعة", "1,670 كم/ساعة (حوالي 465 م/ث)", "10,000 كم/ساعة"],
                "correct": 2,
                "explanationEn": "With Earth's equatorial circumference of ~40,075 km divided by ~24 hours, rotational linear speed at the equator reaches ~1,670 km/h (465 m/s).",
                "explanationAr": "محيط الأرض عند خط الاستواء نحو 40,075 كم مقسوماً على 24 ساعة يعطي سرعة خطية تصل إلى 1,670 كم/ساعة تقريباً.",
                "source": "NASA Goddard Space Flight Center"
            },
            {
                "id": 28,
                "qEn": "What is the phenomenon called where Earth's rotation axis traces out a slow conical wobble over a period of ~25,772 years?",
                "qAr": "ماذا يسمى الترنح المخروطي البطيء لمحور دوران الأرض في الفضاء والذي يكتمل كل 25,772 سنة؟",
                "optionsEn": ["Axial Precession", "Nutation", "Polar wandering", "Obliquity shift"],
                "optionsAr": ["بدارية المحور / ترنح الاعتدالين (Axial Precession)", "الترقيص (Nutation)", "الهجرة القطبية", "تغير الميل الزاوي"],
                "correct": 0,
                "explanationEn": "Axial precession, driven by gravitational tidal forces of the Sun and Moon on Earth's equatorial bulge, has a cycle of ~25,772 years.",
                "explanationAr": "البدارية المحورية هي حركة مخروطية لمحور الأرض ناتجة عن قوى الجذب التفاضلي للشمس والقمر على الانتفاخ الاستوائي وتكتمل كل 25,772 عاماً.",
                "source": "IERS Technical Notes / Celestial Mechanics"
            },
            {
                "id": 29,
                "qEn": "What is the latitude of the Tropic of Cancer in the Northern Hemisphere?",
                "qAr": "ما هي دائرة العرض الدقيقة لمدار السرطان في النصف الشمالي للكرة الأرضية؟",
                "optionsEn": ["Approximately 23.44° N", "Exactly 45.00° N", "Approximately 66.56° N", "Exactly 90.00° N"],
                "optionsAr": ["حوالي 23.44° شمالاً", "45.00° شمالاً تماماً", "حوالي 66.56° شمالاً", "90.00° شمالاً تماماً"],
                "correct": 0,
                "explanationEn": "The Tropic of Cancer is currently located at approximately 23°26′11″ (23.44°) North, marking the northernmost latitude where the Sun can appear directly overhead.",
                "explanationAr": "يقع مدار السرطان حالياً عند 23.44 درجة شمالاً، وهي أقصى نقطة شمالية يمكن أن تتعامد عليها أشعة الشمس عند الظهيرة في الانقلاب الصيفي.",
                "source": "NOAA Solar Calculation Service"
            },
            {
                "id": 30,
                "qEn": "At what point in the polar regions does the Sun remain above the horizon continuously for 24 hours (Midnight Sun)?",
                "qAr": "أين تحدث ظاهرة شمس منتصف الليل (بقاء الشمس فوق الأفق 24 ساعة متواصلة في الصيف)؟",
                "optionsEn": ["Within the Tropics", "Between the Equator and 45° latitude", "Poleward of the Arctic and Antarctic Circles (~66.5°)", "Only at the exact geographic poles"],
                "optionsAr": ["بين المدارين", "بين خط الاستواء ودائرة عرض 45°", "ما وراء الدائرتين القطبيتين الشمالية والجنوبية (~66.5°)", "عند نقطة القطب فقط"],
                "correct": 2,
                "explanationEn": "Locations north of the Arctic Circle (66.5° N) and south of the Antarctic Circle (66.5° S) experience continuous daylight during their respective summer solstices.",
                "explanationAr": "المناطق الواقعة وراء الدائرة القطبية (شمال 66.5° شمالاً وجنوب 66.5° جنوباً) تشهد بقاء الشمس فوق الأفق على مدار اليوم في فصل الصيف.",
                "source": "Royal Astronomical Society"
            }
        ]
    },
    {
        "level": 4,
        "titleEn": "Level 4: Solar System & Basic Astronomy",
        "titleAr": "المستوى 4: النظام الشمسي وعلم الفلك الأساسي",
        "difficulty": "intermediate",
        "questions": [
            {
                "id": 31,
                "qEn": "What type of planet is Earth classified as within the Solar System?",
                "qAr": "كيف يُصنف كوكب الأرض علمياً بين كواكب المجموعة الشمسية؟",
                "optionsEn": ["Gas giant", "Terrestrial / Rocky planet", "Ice giant", "Dwarf planet"],
                "optionsAr": ["عملاق غازي", "كوكب أرضي / صخري (Terrestrial Planet)", "عملاق جليدي", "كوكب قزم"],
                "correct": 1,
                "explanationEn": "Earth is one of the four inner terrestrial planets (Mercury, Venus, Earth, Mars) composed primarily of silicate rocks and metallic iron cores.",
                "explanationAr": "الأرض كوكب صخري ضمن الكواكب الصخرية الداخلية الأربعة التي تتكون أساساً من صخور السيليكات ونواة معدنية غنية بالحديد.",
                "source": "IAU (International Astronomical Union)"
            },
            {
                "id": 32,
                "qEn": "What is the average distance from the Earth to the Sun, defining one Astronomical Unit (1 AU)?",
                "qAr": "ما هي المسافة المتوسطة بين الأرض والشمس، والتي تعرّف الوحدة الفلكية (1 AU)؟",
                "optionsEn": ["Approximately 149,597,870 km", "Approximately 384,400 km", "Approximately 1,000,000 km", "Approximately 9.46 trillion km"],
                "optionsAr": ["حوالي 149,597,870 كم (150 مليون كم)", "حوالي 384,400 كم", "حوالي مليون كم", "حوالي 9.46 تريليون كم"],
                "correct": 0,
                "explanationEn": "By official IAU definition, 1 Astronomical Unit (AU) is exactly 149,597,870,700 meters (~149.6 million kilometers).",
                "explanationAr": "تعرف الوحدة الفلكية رسمياً من الاتحاد الفلكي الدولي بـ 149,597,870,700 متراً، أي قرابة 150 مليون كيلومتر.",
                "source": "International Astronomical Union Resolution B2"
            },
            {
                "id": 33,
                "qEn": "What is the dominant scientific hypothesis explaining the origin of Earth's Moon?",
                "qAr": "ما هي الفرضية العلمية السائدة لتفسير نشأة قمر الأرض؟",
                "optionsEn": ["Co-formation from the solar nebula", "Gravitational capture of a rogue dwarf planet", "Giant Impact Hypothesis (Theia collision)", "Fission from Earth's rapid rotation"],
                "optionsAr": ["التشكل المشترك من السديم الشمسي", "الأسر الجاذبي لكوكب قزم", "فرضية الاصطدام العملاق مع كوكب ثيا (Giant Impact)", "الانشطار السريع بسبب دوران الأرض"],
                "correct": 2,
                "explanationEn": "The Giant Impact Hypothesis posits a Mars-sized protoplanet named Theia collided with the early proto-Earth ~4.5 billion years ago, forming the Moon from ejected debris.",
                "explanationAr": "تنص فرضية الاصطدام العملاق على أن كويكباً بحجم المريخ يُدعى 'ثيا' اصطدم بالأرض المبكرة، وتكثف الحطام المتطاير ليشكل القمر.",
                "source": "NASA Lunar Science Institute / Science 2023"
            },
            {
                "id": 34,
                "qEn": "How long does it take for light emitted from the Sun's photosphere to reach Earth?",
                "qAr": "كم يستغرق الضوء المنبعث من الشمس للوصول إلى سطح كوكب الأرض؟",
                "optionsEn": ["Instantaneous (0 seconds)", "About 8 minutes and 20 seconds", "About 1 hour", "About 24 hours"],
                "optionsAr": ["لحظياً (صفر ثوانٍ)", "حوالي 8 دقائق و20 ثانية", "حوالي ساعة كاملة", "حوالي 24 ساعة"],
                "correct": 1,
                "explanationEn": "Dividing the 149.6 million km distance by the speed of light in vacuum (299,792 km/s) yields roughly 499 seconds, or ~8 minutes 19 seconds.",
                "explanationAr": "بقسمة مسافة 149.6 مليون كم على سرعة الضوء (299,792 كم/ث) ينتج حوالي 499 ثانية، أي قرابة 8 دقائق و20 ثانية.",
                "source": "NIST Physical Measurement Laboratory"
            },
            {
                "id": 35,
                "qEn": "What protects the Earth from harmful high-energy solar wind particles and cosmic radiation?",
                "qAr": "ما الذي يحمي الأرض من الجسيمات المشحونة عالية الطاقة للرياح الشمسية والإشعاع الكوني؟",
                "optionsEn": ["The Moon's shadow", "Earth's geomagnetic field (Magnetosphere)", "The ozone layer alone", "Cloud cover in the troposphere"],
                "optionsAr": ["ظل القمر", "المجال المغناطيسي للأرض (الغلاف المغناطيسي)", "طبقة الأوزون فقط", "الغيوم والغيوم الركامية"],
                "correct": 1,
                "explanationEn": "Earth's geodynamo in the liquid outer core generates a magnetic field forming the magnetosphere, deflecting the majority of the solar wind around Earth.",
                "explanationAr": "يولد دينامو الأرض في اللب الخارجي السائل درعاً مغناطيسياً يحرف الجسيمات المتأينة للرياح الشمسية بعيداً عن الغلاف الجوي.",
                "source": "NASA Heliophysics Division"
            },
            {
                "id": 36,
                "qEn": "What visible atmospheric light show occurs near the polar regions when solar wind particles interact with upper atmospheric gases?",
                "qAr": "ما هو العرض الضوئي البديع الذي يظهر في سماء القطبين عند تصادم الرياح الشمسية بذرات الغلاف الجوي؟",
                "optionsEn": ["Zodiacal light", "Aurora (Borealis and Australis)", "Noctilucent clouds", "Light pillars"],
                "optionsAr": ["ضوء البروج", "الشفق القطبي (الأورورا Aurora Borealis & Australis)", "الغيوم الليلية المضيئة", "الأعمدة الضوئية الجليدية"],
                "correct": 1,
                "explanationEn": "Auroras occur when solar wind particles accelerate along magnetic field lines and collide with oxygen and nitrogen atoms, exciting them to emit green and red light.",
                "explanationAr": "يحدث الشفق القطبي عند تسارع جسيمات الرياح الشمسية مع خطوط المجال المغناطيسي واصطدامها بذرات الأكسجين والنيتروجين مطلقة أضواء خضراء وحمراء.",
                "source": "NOAA Space Weather Prediction Center"
            },
            {
                "id": 37,
                "qEn": "Which planet is often referred to as Earth's 'sister planet' due to having similar diameter, mass, and bulk density?",
                "qAr": "أي كواكب المجموعة الشمسية يُطلق عليه لقب 'توأم الأرض' لتقارب قطره وكتلته وكثافته؟",
                "optionsEn": ["Mars", "Venus", "Mercury", "Neptune"],
                "optionsAr": ["المريخ", "الزهرة (Venus)", "عطارد", "نبتون"],
                "correct": 1,
                "explanationEn": "Venus has ~95% of Earth's diameter and ~81.5% of Earth's mass, though its runaway greenhouse atmosphere creates surface temperatures of ~465°C.",
                "explanationAr": "الزهرة يمتلك نحو 95% من قطر الأرض و81.5% من كتلتها، ورغم هذا التطابق الهندسي فإن غلافه الكثيف جعله جحيماً بـ 465 درجة مئوية.",
                "source": "NASA Planetary Exploration / Venus Express"
            },
            {
                "id": 38,
                "qEn": "What is the orbital eccentricity of Earth's orbit around the Sun?",
                "qAr": "ما هو مقدار اللامركزية المدارية (الانحراف المداري) لمدار الأرض حول الشمس؟",
                "optionsEn": ["0.000 (perfect circle)", "Approximately 0.0167 (nearly circular ellipse)", "0.205 (highly elliptical)", "0.999 (parabolic)"],
                "optionsAr": ["صفر تماماً (دائرة تامة)", "حوالي 0.0167 (قطع ناقص يقارب الدائرة)", "0.205 (شديد الاستطالة)", "0.999"],
                "correct": 1,
                "explanationEn": "Earth's orbit is a nearly circular ellipse with an eccentricity of ~0.0167, causing a modest ~3.4% difference in solar distance between perihelion and aphelion.",
                "explanationAr": "مدار الأرض إهليلجي شبه دائري بانحراف مداري طفيف يبلغ 0.0167 فقط، ما يجعل الفارق بين أقرب وأبعد نقطة لا يتجاوز 3.4%.",
                "source": "NASA JPL Solar System Dynamics"
            },
            {
                "id": 39,
                "qEn": "In astronomical terms, what is the 'Habitable Zone' (or Goldilocks Zone) around a star?",
                "qAr": "ما هو تعريف 'النطاق الصالح للحياة' (Goldilocks Zone) حول النجم في علم الفلك؟",
                "optionsEn": ["A region with zero radiation", "The orbital distance range where liquid water can stably exist on a planet's surface", "The boundary inside a black hole", "Where temperatures are exactly 0°C at all times"],
                "optionsAr": ["منطقة خالية من أي إشعاع", "المدى المداري الذي يمكن فيه للمياه السائلة الاستقرار على سطح الكوكب", "حدود أفق الحدث للثقب الأسود", "حيث الحرارة صفر مئوية دوماً"],
                "correct": 1,
                "explanationEn": "The circumstellar habitable zone is the distance range from a host star where atmospheric pressure allows liquid surface water, vital for terrestrial life.",
                "explanationAr": "هو المدى المداري حول النجم الذي يسمح فيه الإشعاع الشمسي والضغط الجوي بوجود الماء السائل المستقر على سطح الكوكب دون تجمد أو غليان.",
                "source": "NASA Exoplanet Exploration Program"
            },
            {
                "id": 40,
                "qEn": "Which star is currently the closest star to the Earth and Solar System?",
                "qAr": "ما هو أقرب نجم لكوكب الأرض والمجموعة الشمسية بعد الشمس؟",
                "optionsEn": ["Sirius", "Proxima Centauri", "Betelgeuse", "Polaris"],
                "optionsAr": ["الشعرى اليمانية", "بروكسيما سنتوري (قنطور الأقرب)", "منكب الجوزاء", "نجم القطب الشمالي"],
                "correct": 1,
                "explanationEn": "Proxima Centauri, a red dwarf in the Alpha Centauri system, is located approximately 4.2465 light-years (~40 trillion km) from Earth.",
                "explanationAr": "بروكسيما سنتوري هو قزم أحمر يقع على مسافة 4.2465 سنة ضوئية (حوالي 40 تريليون كم) من كوكبنا.",
                "source": "ESA Gaia Mission / Astronomy & Astrophysics"
            }
        ]
    },
    {
        "level": 5,
        "titleEn": "Level 5: Atmosphere, Weather & Pressure",
        "titleAr": "المستوى 5: الغلاف الجوي والطقس والضغط الجوي",
        "difficulty": "intermediate",
        "questions": [
            {
                "id": 41,
                "qEn": "In which atmospheric layer does virtually all of Earth's weather and cloud activity occur?",
                "qAr": "في أي طبقة من طبقات الغلاف الجوي تحدث كافة الظواهر الجوية والغيوم والأمطار؟",
                "optionsEn": ["Troposphere", "Stratosphere", "Mesosphere", "Thermosphere"],
                "optionsAr": ["التروبوسفير (Troposphere)", "الستراتوسفير", "الميزوسفير", "الثيرموسفير"],
                "correct": 0,
                "explanationEn": "The troposphere extends from the surface up to 7–20 km altitude and contains ~75% of atmospheric mass and 99% of its water vapor, hosting weather systems.",
                "explanationAr": "تمتد طبقة التروبوسفير من السطح حتى ارتفاع 7-20 كم وتضم 75% من كتلة الهواء و99% من بخار الماء وتحدث فيها كل تقلبات الطقس.",
                "source": "NOAA National Weather Service"
            },
            {
                "id": 42,
                "qEn": "What is standard atmospheric pressure at mean sea level under standard international conditions?",
                "qAr": "ما هو مقدار الضغط الجوي المعياري عند متوسط مستوى سطح البحر بالوحدات الدولية؟",
                "optionsEn": ["100 kPa exactly", "101.325 kPa (1,013.25 hPa / 1 atm)", "760 kPa", "14.7 kPa"],
                "optionsAr": ["100 كيلو باسكال تماماً", "101.325 كيلو باسكال (1,013.25 هكتوباسكال)", "760 كيلو باسكال", "14.7 كيلو باسكال"],
                "correct": 1,
                "explanationEn": "Standard atmospheric pressure is defined internationally as 101,325 Pa, equivalent to 1,013.25 millibars (hPa) or 760 mmHg.",
                "explanationAr": "الضغط الجوي القياسي المعترف به دولياً يساوي 101,325 باسكال (1,013.25 مليبار/هكتوباسكال) أو 760 ملم زئبق.",
                "source": "ISO 2533: Standard Atmosphere"
            },
            {
                "id": 43,
                "qEn": "In which atmospheric layer is the protective ozone layer (ozonosphere) primarily situated?",
                "qAr": "في أي طبقة من الغلاف الجوي تتركز طبقة الأوزون الحامية من الأشعة فوق البنفسجية؟",
                "optionsEn": ["Troposphere", "Stratosphere", "Thermosphere", "Exosphere"],
                "optionsAr": ["التروبوسفير", "الستراتوسفير (Stratosphere)", "الثيرموسفير", "الإكسوسفير"],
                "correct": 1,
                "explanationEn": "The ozone layer resides in the stratosphere between roughly 15 km and 35 km altitude, where ozone molecules absorb harmful solar UV-B and UV-C radiation.",
                "explanationAr": "تتركز طبقة الأوزون في الستراتوسفير بين ارتفاع 15 و 35 كم، لتمتص الأشعة فوق البنفسجية الشمسية الضارة بالحياة.",
                "source": "WMO / UNEP Scientific Assessment of Ozone Depletion"
            },
            {
                "id": 44,
                "qEn": "What apparent inertial force caused by Earth's rotation deflects moving winds to the right in the Northern Hemisphere and left in the Southern Hemisphere?",
                "qAr": "ما هي القوة الظاهرية الناتجة عن دوران الأرض والتي تحرف اتجاه الرياح يميناً في النصف الشمالي ويساراً في النصف الجنوبي؟",
                "optionsEn": ["Centripetal force", "Coriolis effect / force", "Gravitational tidal force", "Lorentz force"],
                "optionsAr": ["القوة الجاذبة المركزية", "تأثير كوريوليس (Coriolis Effect)", "قوة المد الجذبي", "قوة لورنتز"],
                "correct": 1,
                "explanationEn": "The Coriolis effect, a consequence of viewing moving air masses from Earth's rotating reference frame, deflects trajectories rightwards in the North and leftwards in the South.",
                "explanationAr": "تأثير كوريوليس ينشأ عن حركة الكتل الهوائية في إطار مرجعي دوار، مما يحرف مسار الرياح والعواصف الدوارة.",
                "source": "AMS Glossary of Meteorology / NOAA"
            },
            {
                "id": 45,
                "qEn": "What is the coldest atmospheric layer where meteors typically burn up upon entry?",
                "qAr": "ما هي أبرد طبقات الغلاف الجوي والتي تحترق فيها معظم النيازك والشهب عند دخولها؟",
                "optionsEn": ["Stratosphere", "Mesosphere", "Thermosphere", "Troposphere"],
                "optionsAr": ["الستراتوسفير", "الميزوسفير (Mesosphere)", "الثيرموسفير", "التروبوسفير"],
                "correct": 1,
                "explanationEn": "The mesosphere (50–85 km altitude) reaches minimum temperatures down to -90°C to -130°C at the mesopause and vaporizes incoming meteoric particles.",
                "explanationAr": "الميزوسفير (بين 50 و 85 كم) هي أبرد طبقة وتنخفض حرارتها إلى ما دون -90 درجة مئوية، وفيها تحترق الشهب بفعل الاحتكاك والضغط الصدمي.",
                "source": "NASA Earth Science / UCAR"
            },
            {
                "id": 46,
                "qEn": "What is the Karman Line, internationally recognized by the FAI as the boundary between Earth's atmosphere and outer space?",
                "qAr": "ما هو خط كارمان (Kármán line) المعترف به دولياً كحد فاصل بين الغلاف الجوي والفضاء الخارجي؟",
                "optionsEn": ["10 km above sea level", "50 km above sea level", "100 km (62 miles) above sea level", "500 km above sea level"],
                "optionsAr": ["10 كم فوق سطح البحر", "50 كم فوق سطح البحر", "100 كم (62 ميلاً) فوق سطح البحر", "500 كم فوق سطح البحر"],
                "correct": 2,
                "explanationEn": "The Fédération Aéronautique Internationale (FAI) defines the edge of space at the Kármán line at 100 km altitude, where orbital dynamics exceed aerodynamic lift.",
                "explanationAr": "يعرف الاتحاد الدولي للملاحة الجوية خط كارمان على ارتفاع 100 كم كحد يبدأ عنده الفضاء حيث تفقد الأجنحة الديناميكية قدرتها على الرفع.",
                "source": "Fédération Aéronautique Internationale (FAI)"
            },
            {
                "id": 47,
                "qEn": "What is the thermodynamic process where warm moist air cools as it rises due to decreasing ambient pressure without exchange of heat with surroundings?",
                "qAr": "ما هي العملية الثرموديناميكية التي يبرد فيها الهواء الصاعد بسبب انخفاض الضغط دون تبادل حراري مع المحيط؟",
                "optionsEn": ["Conduction", "Adiabatic cooling", "Latent vaporization", "Radiative equilibrium"],
                "optionsAr": ["التوصيل الحراري", "التبريد الأديباتي (Adiabatic Cooling)", "التبخير الكامن", "الاتزان الإشعاعي"],
                "correct": 1,
                "explanationEn": "Adiabatic expansion occurs as rising air expands under decreasing environmental pressure, performing work and lowering its temperature without heat exchange.",
                "explanationAr": "التبريد الأديباتي يحدث حين يتمدد الهواء الصاعد بسبب انخفاض الضغط الجوي ويبذل شغلاً يخفض حرارته، وهو المسؤول عن تكاثف الغيوم.",
                "source": "American Meteorological Society Glossary"
            },
            {
                "id": 48,
                "qEn": "What instrument is traditionally utilized to measure atmospheric air pressure?",
                "qAr": "ما هو الجهاز العلمي التقليدي المستخدم لقياس الضغط الجوي؟",
                "optionsEn": ["Anemometer", "Barometer", "Hygrometer", "Spectrometer"],
                "optionsAr": ["الأنيموميتر", "الباروميتر (Barometer)", "الهايجروميتر", "المطياف"],
                "correct": 1,
                "explanationEn": "A barometer (mercury or aneroid) measures ambient atmospheric pressure, essential for tracking frontal passages and anticipating weather systems.",
                "explanationAr": "الباروميتر (سواء الزئبقي أو المفرغ) هو الجهاز الأساسي لقياس ضغط الهواء لتتبع الكتل الهوائية والمنخفضات الجوية.",
                "source": "National Weather Service Instrument Manual"
            },
            {
                "id": 49,
                "qEn": "Which greenhouse gas is responsible for the largest portion of the natural terrestrial greenhouse effect on Earth?",
                "qAr": "أي الغازات هو المسؤول عن الجزء الأكبر من ظاهرة الاحتباس الحراري الطبيعية على كوكب الأرض؟",
                "optionsEn": ["Methane", "Water vapor (H₂O)", "Ozone", "Nitrous oxide"],
                "optionsAr": ["الميثان", "بخار الماء (Water Vapor)", "الأوزون", "أكسيد النيتروز"],
                "correct": 1,
                "explanationEn": "Water vapor is the most abundant natural greenhouse gas, contributing ~60% of the natural greenhouse warming, though its concentration is driven by temperature.",
                "explanationAr": "بخار الماء هو أكبر مسبب للاحتباس الحراري الطبيعي على الأرض ويساهم بنحو 60% من الدفء الطبيعي لكوكبنا قبل الأنشطة البشرية.",
                "source": "IPCC Assessment Reports / NASA GISS"
            },
            {
                "id": 50,
                "qEn": "What is the global wind belt that blows steadily from east to west across the tropics toward the Intertropical Convergence Zone (ITCZ)?",
                "qAr": "ما هي الرياح الدائمة التي تهب بثبات من الشرق إلى الغرب عبر المناطق المدارية نحو خط الاستواء؟",
                "optionsEn": ["Polar easterlies", "Mid-latitude westerlies", "Trade winds (Alizés)", "Roaring forties"],
                "optionsAr": ["الشرقيات القطبية", "الغربيات العكسية", "الرياح التجارية (Trade Winds)", "رياح الأربعينات الهوجاء"],
                "correct": 2,
                "explanationEn": "The trade winds blow reliably from subtropical high-pressure ridges toward the equatorial doldrums (northeast in Northern Hemisphere, southeast in Southern Hemisphere).",
                "explanationAr": "الرياح التجارية تهب باستمرار من المرتفعات شبه المدارية نحو المنخفض الاستوائي، واستخدمها البحارة عبر التاريخ للملاحة.",
                "source": "NOAA National Weather Service / Hadley Circulation"
            }
        ]
    },
    {
        "level": 6,
        "titleEn": "Level 6: Climate & Geological Processes",
        "titleAr": "المستوى 6: المناخ والعمليات الجيولوجية وحركة الصفائح",
        "difficulty": "intermediate_advanced",
        "questions": [
            {
                "id": 51,
                "qEn": "What unifying geological theory explains continental drift, earthquakes, and mountain building through moving lithospheric plates?",
                "qAr": "ما هي النظرية الجيولوجية الموحدة التي تفسر زحزحة القارات وتشكل الجبال والزلازل عبر حركة صفائح الغلاف الصخري؟",
                "optionsEn": ["Geosyncline theory", "Plate Tectonics", "Catastrophism", "Expanding Earth hypothesis"],
                "optionsAr": ["نظرية تقعر الأرض", "نظرية الصفائح التكتونية (Plate Tectonics)", "نظرية الكوارث الفجائية", "فرضية تمدد الأرض"],
                "correct": 1,
                "explanationEn": "Plate tectonics explains how Earth's rigid lithospheric plates glide atop the ductile asthenosphere, driving orogeny, volcanism, and seismic activity.",
                "explanationAr": "تفسر تكتونية الصفائح انزلاق صفائح الغلاف الصخري الصلبة فوق الغلاف الموري اللدن، مما يفسر تكون الجبال والبراكين والزلازل.",
                "source": "USGS Plate Tectonics in a Nutshell"
            },
            {
                "id": 52,
                "qEn": "What is the name of the ancient supercontinent that incorporated almost all of Earth's landmasses ~335 to ~175 million years ago?",
                "qAr": "ما هو اسم القارة العظمى القديمة التي جمعت كل كتل اليابسة قبل نحو 300 إلى 175 مليون سنة؟",
                "optionsEn": ["Rodinia", "Pangaea (Pangea)", "Columbia / Nuna", "Gondwana alone"],
                "optionsAr": ["رودينيا", "بانجيا (Pangea)", "كولومبيا / نونا", "غوندوانا وحدها"],
                "correct": 1,
                "explanationEn": "Pangaea was the supercontinent that assembled during the late Paleozoic and began rifting apart during the early Jurassic ~175 million years ago.",
                "explanationAr": "بانجيا هي القارة العملاقة التي تشكلت في أواخر حقبة الحياة القديمة وتفككت خلال العصر الجوراسي إلى لوراسيا وغوندوانا.",
                "source": "USGS Historical Geology"
            },
            {
                "id": 53,
                "qEn": "What geological boundary occurs where two tectonic plates move away from each other, such as at the Mid-Atlantic Ridge?",
                "qAr": "ما نوع الحدود التكتونية التي تتباعد عندها صفيحتان عن بعضهما كما في سلسلة أعراف منتصف الأطلسي؟",
                "optionsEn": ["Convergent boundary", "Divergent boundary (Constructive)", "Transform boundary", "Subduction zone"],
                "optionsAr": ["حدود متقاربة", "حدود متباعدة / بناءة (Divergent Boundary)", "حدود صدعية تحويلية", "نطاق انغراز"],
                "correct": 1,
                "explanationEn": "At divergent boundaries, tectonic plates pull apart and upwelling magma from the mantle cools to form new oceanic crust.",
                "explanationAr": "عند الحدود المتباعدة، تبتعد الصفائح الصخرية وتصعد الماجما من الوشاح لتتبرد وتكون قشرة محيطية جديدة في عملية اتساع قاع البحر.",
                "source": "USGS Understanding Plate Motions"
            },
            {
                "id": 54,
                "qEn": "What geological zone is formed where an oceanic plate slides beneath a continental or another oceanic plate into the mantle?",
                "qAr": "ماذا يسمى النطاق الذي تنزلق فيه صفيحة محيطية ثقيلة تحت صفيحة أخرى لتغوص في الوشاح؟",
                "optionsEn": ["Subduction zone", "Rift valley", "Mid-ocean ridge", "Transform fault"],
                "optionsAr": ["نطاق الانغراز (Subduction Zone)", "الوادي المتصدع", "حيد منتصف المحيط", "الصدع التحويلي"],
                "correct": 0,
                "explanationEn": "In subduction zones, denser oceanic lithosphere plunges beneath the less dense plate, generating deep oceanic trenches and volcanic arcs.",
                "explanationAr": "في نطاقات الانغراز تغطس القشرة المحيطية الأكثر كثافة تحت القشرة القارية، مولدة خنادق محيطية عميقة وسلاسل براكين نشطة.",
                "source": "Smithsonian Global Volcanism Program"
            },
            {
                "id": 55,
                "qEn": "What scale measures the seismic moment release (total mechanical energy) of an earthquake, replacing the Richter scale for large events?",
                "qAr": "ما هو المقياس العلمي الدقيق المستخدم حالياً لقياس الطاقة الميكانيكية الكلية للزلازل الكبيرة؟",
                "optionsEn": ["Modified Mercalli Intensity scale", "Moment Magnitude Scale (Mw)", "Fujita scale", "Mohs scale"],
                "optionsAr": ["مقياس ميركالي المعدل", "مقياس درجة العزم الزلزالي (Moment Magnitude Scale - Mw)", "مقياس فوجيتا", "مقياس موهس"],
                "correct": 1,
                "explanationEn": "The Moment Magnitude scale (Mw), introduced by Hanks and Kanamori (1979), measures physical seismic moment and avoids saturation in large earthquakes.",
                "explanationAr": "يقيس مقياس درجة العزم (Mw) عزم الزلزال الفيزيائي (مساحة الفالق ومقدار الإزاحة وقوة الصخور) دون تشبع عند الزلازل الكبرى.",
                "source": "USGS Earthquake Hazards / Seismological Research Letters"
            },
            {
                "id": 56,
                "qEn": "What type of rock is formed directly from the crystallization and solidification of molten magma or lava?",
                "qAr": "ما نوع الصخور التي تتشكل مباشرة من تبريد وتبلور الصهارة (الماجما) أو الحمم البركانية؟",
                "optionsEn": ["Sedimentary rock", "Igneous rock", "Metamorphic rock", "Evaporite"],
                "optionsAr": ["صخور رسوبية", "صخور نارية (Igneous Rock)", "صخور متحولة", "متبخرات ملحية"],
                "correct": 1,
                "explanationEn": "Igneous rocks (such as basalt, granite, and obsidian) form when molten rock cools and solidifies either underground (plutonic) or on the surface (volcanic).",
                "explanationAr": "تتشكل الصخور النارية (مثل البازلت والغرانيت) عندما تبرد الماجما وتتبلور في باطن الأرض أو على السطح بعد ثوران البركان.",
                "source": "British Geological Survey"
            },
            {
                "id": 57,
                "qEn": "What cyclical variations in Earth's eccentricity, axial tilt, and precession pace the Quaternary glacial and interglacial cycles?",
                "qAr": "ما هي الدورات الفلكية لتغير انحراف مدار الأرض وميل محورها وترنحه والتي تتحكم في العصور الجليدية؟",
                "optionsEn": ["Milankovitch cycles", "Wilson cycles", "Solar sunspot 11-year cycles", "Chandler wobble"],
                "optionsAr": ["دورات ميلانكوفيتش (Milankovitch Cycles)", "دورات ويلسون لتجمع القارات", "دورات البقع الشمسية", "تذبذب تشاندلر"],
                "correct": 0,
                "explanationEn": "Milankovitch cycles describe orbital eccentricity (~100kyr), obliquity (~41kyr), and precession (~23kyr) driving astronomical variations in seasonal insolation.",
                "explanationAr": "دورات ميلانكوفيتش تفسر التغيرات الفلكية في مدار الأرض وميلها وترنحها، مما يغير توزيع الإشعاع الشمسي ويقود العصور الجليدية.",
                "source": "NASA Earth Observatory / Science"
            },
            {
                "id": 58,
                "qEn": "What famous fault in California marks a major strike-slip transform boundary between the Pacific Plate and North American Plate?",
                "qAr": "ما هو الفالق الشهير في كاليفورنيا الذي يمثل صدعاً تحويلياً انزلاقياً بين صفيحة الهادئ وصفيحة أمريكا الشمالية؟",
                "optionsEn": ["New Madrid fault", "San Andreas Fault", "Anatolian fault", "Alpine fault"],
                "optionsAr": ["فالق نيو مدريد", "فالق سان أندرياس (San Andreas Fault)", "فالق شمال الأناضول", "فالق الألب"],
                "correct": 1,
                "explanationEn": "The San Andreas Fault is a right-lateral strike-slip transform fault extending roughly 1,200 km through California.",
                "explanationAr": "فالق سان أندرياس هو صدع تحويلي انزلاقي أفقي يمتد على مسافة 1200 كم ويفصل بين صفيحة المحيط الهادئ وصفيحة أمريكا الشمالية.",
                "source": "USGS California Fault Maps"
            },
            {
                "id": 59,
                "qEn": "What is the continuous global conveyor belt of ocean circulation driven by temperature and salinity gradients called?",
                "qAr": "ماذا يسمى الحزام الناقل العالمي لتيارات المحيط العميقة المدفوعة بفوارق الحرارة والملوحة؟",
                "optionsEn": ["Ekman transport", "Thermohaline Circulation (AMOC / Global Conveyor)", "Surface gyres", "Tidal resonance"],
                "optionsAr": ["انتقال إكمان", "الدورة الحرارية الملحية (Thermohaline Circulation / AMOC)", "الدوامات السطحية فقط", "الرنين المدّي"],
                "correct": 1,
                "explanationEn": "Thermohaline circulation is driven by dense, cold, saline water sinking in polar regions and slowly circulating through the deep global ocean basins.",
                "explanationAr": "الدورة الحرارية الملحية تعتمد على غوص المياه الباردة عالية الملوحة في القطبين وجريانها في أعماق المحيطات لتنظيم مناخ الكوكب.",
                "source": "NOAA Ocean Service Education"
            },
            {
                "id": 60,
                "qEn": "What geological era, beginning ~66 million years ago following the Cretaceous-Paleogene extinction, is known as the 'Age of Mammals'?",
                "qAr": "ما هي الحقبة الجيولوجية التي بدأت قبل 66 مليون سنة عقب انقراض الديناصورات وتعرف بعصر الثدييات؟",
                "optionsEn": ["Paleozoic Era", "Mesozoic Era", "Cenozoic Era", "Neoproterozoic Era"],
                "optionsAr": ["حقبة الحياة القديمة (Paleozoic)", "حقبة الحياة الوسطى (Mesozoic)", "حقبة الحياة الحديثة (Cenozoic Era)", "البروتيروزويك"],
                "correct": 2,
                "explanationEn": "The Cenozoic Era spans from the K-Pg extinction event 66 million years ago to the present day, characterized by the radiation of mammals, birds, and angiosperms.",
                "explanationAr": "حقبة الحياة الحديثة (السينوزوي) بدأت قبل 66 مليون سنة وشهدت ازدهار الثدييات والطيور والنباتات الزهرية وصولاً إلى ظهور الإنسان.",
                "source": "International Commission on Stratigraphy (ICS)"
            }
        ]
    },
    {
        "level": 7,
        "titleEn": "Level 7: Oceans, Ecosystems & Biosphere",
        "titleAr": "المستوى 7: المحيطات والأنظمة البيئية والغلاف الحيوي",
        "difficulty": "advanced",
        "questions": [
            {
                "id": 61,
                "qEn": "What microscopic marine photosynthetic organisms form the foundational base of oceanic food webs and produce ~50% of Earth's oxygen?",
                "qAr": "ما هي الكائنات المجهرية النباتية الدقيقة التي تشكل قاعدة السلسلة الغذائية البحرية وتنتج نصف أكسجين الأرض؟",
                "optionsEn": ["Zooplankton", "Phytoplankton", "Coral polyps", "Foraminifera"],
                "optionsAr": ["العوالق الحيوانية (الزوبلانكتون)", "العوالق النباتية البحرية (الفيتوبلانكتون - Phytoplankton)", "بوليبات المرجان", "الفورامينيفرا"],
                "correct": 1,
                "explanationEn": "Marine phytoplankton (such as diatoms and cyanobacteria like Prochlorococcus) perform massive photosynthesis, generating roughly 50% of global atmospheric oxygen.",
                "explanationAr": "تقوم العوالق النباتية (مثل الدياتومات والبكتيريا الزرقاء) بعمليات بناء ضوئي هائلة تنتج ما يقارب 50% من أكسجين كوكب الأرض.",
                "source": "NASA Ocean Biology / NOAA"
            },
            {
                "id": 62,
                "qEn": "What chemical consequence occurs when oceanic surface waters absorb excess anthropogenic carbon dioxide from the atmosphere?",
                "qAr": "ما هي الظاهرة الكيميائية البيئية التي تحدث عند امتصاص مياه المحيطات لثاني أكسيد الكربون الزائد من الجو؟",
                "optionsEn": ["Ocean desalination", "Ocean Acidification (drop in oceanic pH)", "Thermal super-saturation", "Eutrophication"],
                "optionsAr": ["تحلية المحيطات", "تحمض المحيطات (انخفاض الرقم الهيدروجيني pH)", "فرط التشبع الحراري", "الإثراء الغذائي السطحي"],
                "correct": 1,
                "explanationEn": "CO₂ dissolves in seawater to form carbonic acid (H₂CO₃), increasing hydrogen ion concentration and lowering oceanic pH while depleting carbonate ions needed for calcification.",
                "explanationAr": "يتفاعل ثاني أكسيد الكربون المذاب مع ماء البحر مكوناً حمض الكربونيك، مما يخفض الرقم الهيدروجيني للمحيطات ويهدد الكائنات ذات الأصداف المرجانية.",
                "source": "NOAA PMEL Ocean Acidification Program"
            },
            {
                "id": 63,
                "qEn": "What is the world's largest living biological structure and coral reef system on Earth?",
                "qAr": "ما هو أكبر بناء حيوي عضوي ونظام بيئي للشعاب المرجانية على سطح كوكب الأرض؟",
                "optionsEn": ["Mesoamerican Barrier Reef", "Great Barrier Reef (Australia)", "Red Sea Coral Reef", "Florida Reef Tract"],
                "optionsAr": ["الحاجز المرجاني لأمريكا الوسطى", "الحاجز المرجاني العظيم في أستراليا (Great Barrier Reef)", "شعاب البحر الأحمر", "شعاب فلوريدا"],
                "correct": 1,
                "explanationEn": "The Great Barrier Reef off north-eastern Australia extends over 2,300 km and covers ~344,400 sq km, visible even from Earth orbit.",
                "explanationAr": "يمتد الحاجز المرجاني العظيم قبالة شمال شرق أستراليا على طول 2300 كم ويضم آلاف الشعاب، ويمكن رؤيته حتى من الفضاء.",
                "source": "UNESCO World Heritage Centre / GBRMPA"
            },
            {
                "id": 64,
                "qEn": "In ecology and biogeography, what is an ecosystem or biome called where rivers meet the sea and fresh and saltwater mix?",
                "qAr": "ماذا يسمى النظام البيئي النهري البحري الذي تلتقي فيه مياه الأنهار العذبة بمياه البحر المالحة؟",
                "optionsEn": ["Abyssal plain", "Estuary", "Oasis", "Pelagic zone"],
                "optionsAr": ["السهل اللجي السحيق", "المصب الخليجي / الإستواري (Estuary)", "الواحة", "المنطقة المحيطية المفتوحة"],
                "correct": 1,
                "explanationEn": "Estuaries are semi-enclosed coastal bodies of water where freshwater runoff mixes with seawater, creating highly productive brackish nursery habitats.",
                "explanationAr": "المصبات (Estuaries) هي بيئات ساحلية فريدة تمتزج فيها المياه العذبة بالمالحة وتعد من أغنى الحواضن البيئية للكائنات البحرية.",
                "source": "US EPA National Estuary Program"
            },
            {
                "id": 65,
                "qEn": "What is the standard salinity measurement of the open global ocean on the Practical Salinity Scale (PSS-78)?",
                "qAr": "ما هو القياس المعياري لملوحة مياه المحيطات المفتوحة وفقاً لمقياس الملوحة العملي (PSS-78)؟",
                "optionsEn": ["Approximately 5 PSU (0.5% mass fraction)", "Approximately 35 PSU (~35 g of dissolved salts per kg of seawater / 3.5%)", "Approximately 70 PSU (7%)", "Approximately 120 PSU (12%)"],
                "optionsAr": ["حوالي 5 وحدات ملوحة (0.5%)", "حوالي 35 وحدة ملوحة عملية (~35 غراماً من الأملاح الذائبة لكل كغم ماء بحر أو 3.5%)", "حوالي 70 وحدة ملوحة (7%)", "حوالي 120 وحدة ملوحة"],
                "correct": 1,
                "explanationEn": "On the Practical Salinity Scale (PSS-78), salinity is a dimensionless conductivity ratio with 35 corresponding to approximately 35.165 g/kg on the modern TEOS-10 Absolute Salinity scale (g/kg).",
                "explanationAr": "وفقاً لمقياس الملوحة العملي (PSS-78) المعتمد في علم المحيطات الفيزيائي، تبلغ ملوحة مياه المحيط المفتوحة نحو 35 وحدة (ما يعادل قرابة 35.165 غرام ملح لكل كيلوغرام ماء وفق معيار TEOS-10 الدولي).",
                "source": "UNESCO/IOC PSS-78 & TEOS-10 International Thermodynamic Equation of Seawater"
            },
            {
                "id": 66,
                "qEn": "What is the name of the oceanic zone that receives no sunlight and extends from 1,000 meters to 4,000 meters below sea level?",
                "qAr": "ماذا تسمى الطبقة المحيطية التي لا يصلها ضوء الشمس نهائياً وتمتد بين عمق 1000 و 4000 متر؟",
                "optionsEn": ["Epipelagic (sunlight) zone", "Mesopelagic (twilight) zone", "Bathypelagic (midnight) zone", "Hadalpelagic (trench) zone"],
                "optionsAr": ["منطقة السطح المضاءة (Epipelagic)", "منطقة الشفق (Mesopelagic)", "منطقة منتصف الليل البحرية (Bathypelagic Zone)", "منطقة الخنادق الهدالية"],
                "correct": 2,
                "explanationEn": "The bathypelagic zone (1,000 m to 4,000 m) exists in complete darkness, with intense hydrostatic pressure and temperatures around 4°C.",
                "explanationAr": "منطقة منتصف الليل السحيقة (Bathypelagic) تعيش في ظلام دامس وضغط مائي مرتفع دون أي بناء ضوئي.",
                "source": "Woods Hole Oceanographic Institution"
            },
            {
                "id": 67,
                "qEn": "What unique terrestrial ecosystem stores more carbon per square meter than any other biome, formed by waterlogged, partially decomposed plant matter?",
                "qAr": "ما هو النظام البيئي الأرضي الذي يخزن كميات هائلة من الكربون لكل متر مربع عبر تراكم نباتي بطيء التحلل في الأراضي الرطبة؟",
                "optionsEn": ["Temperate grassland", "Peatland / Bogs", "Arid savannah", "Chaparral"],
                "optionsAr": ["المراعي المعتدلة", "أراضي الخث / المستنقعات الخثية (Peatlands)", "السافانا الجافة", "أحراش الشابارال"],
                "correct": 1,
                "explanationEn": "Peatlands cover only ~3% of global land area but store almost twice as much carbon as all the world's forests combined due to anoxic waterlogged preservation.",
                "explanationAr": "تغطي أراضي الخث 3% فقط من اليابسة لكنها تحتجز كربوناً يعادل ضعف ما تخزنه جميع غابات العالم مجتمعة بسبب بطء التحلل في بيئتها الرطبة الخالية من الأكسجين.",
                "source": "UNEP Global Peatlands Assessment / Nature"
            },
            {
                "id": 68,
                "qEn": "What is the deepest benthic oceanic zone, specifically located inside deep-sea trenches below 6,000 meters depth?",
                "qAr": "ماذا يُطلق على أعمق نطاق قاعي للمحيطات يقع تحديداً داخل الخنادق المحيطية تحت عمق 6000 متر؟",
                "optionsEn": ["Hadal zone", "Abyssal zone", "Neritic zone", "Littoral zone"],
                "optionsAr": ["نطاق الهدال السحيق (Hadal Zone)", "النطاق السحيق (Abyssal)", "النطاق الجرفي (Neritic)", "النطاق الشاطئي (Littoral)"],
                "correct": 0,
                "explanationEn": "The Hadal zone (named after Hades) encompasses the deepest ocean trenches from 6,000 m down to ~11,000 m, hosting specialized piezophilic organisms.",
                "explanationAr": "نطاق الهدال (Hadal zone) يشمل قيعان الخنادق المحيطية من 6000 متر حتى 11000 متر، وتعيش فيه كائنات مقاومة للضغط الفائق.",
                "source": "Schmidt Ocean Institute / Deep Sea Research"
            },
            {
                "id": 69,
                "qEn": "What process carried out by hydrothermal vent bacteria forms organic compounds from hydrogen sulfide and methane in the complete absence of sunlight?",
                "qAr": "ما هي العملية الحيوية التي تنتج بها بكتيريا الفوهات المائية الحارة مركبات عضوية دون أي ضوء شمس؟",
                "optionsEn": ["Photosynthesis", "Chemosynthesis", "Fermentation", "Photolysis"],
                "optionsAr": ["البناء الضوئي", "البناء الكيميائي (Chemosynthesis)", "التخمر اللاهوائي", "التحلل الضوئي"],
                "correct": 1,
                "explanationEn": "Chemosynthesis uses chemical energy released from the oxidation of inorganic molecules (such as hydrogen sulfide) to fix carbon into biomass without sunlight.",
                "explanationAr": "البناء الكيميائي يعتمد على أكسدة كبريتيد الهيدروجين والميثان المنبعث من فوهات الأعماق لإنتاج الطاقة العضوية في غياب الضوء التام.",
                "source": "NOAA Ocean Exploration / Nature 1977 Discovery"
            },
            {
                "id": 70,
                "qEn": "The Amazon Rainforest is estimated to contain roughly what fraction of the world's known terrestrial biodiversity?",
                "qAr": "تقدر الدراسات البيئية العالمية أن غابات الأمازون المطيرة تأوي أي نسبة تقريبية من التنوع الحيوي البري في العالم؟",
                "optionsEn": ["About 1%", "About 10% (one in ten known species)", "Over 75%", "Approximately 50%"],
                "optionsAr": ["حوالي 1%", "حوالي 10% (نوع من كل عشرة أنواع معروفة على الأرض)", "أكثر من 75%", "حوالي 50%"],
                "correct": 1,
                "explanationEn": "The Amazon Basin covers over 6 million sq km and is estimated to shelter ~10% of all known species on Earth, making it a critical planetary biodiversity repository.",
                "explanationAr": "تضم غابات الأمازون نحو 10% من كافة الأنواع الحية المعروفة علمياً على كوكب الأرض، ما يجعلها أكبر مستودع للتنوع الحيوي البري.",
                "source": "WWF / Science Advances Amazon Assessment"
            }
        ]
    },
    {
        "level": 8,
        "titleEn": "Level 8: Scientific Charts & Data Analysis",
        "titleAr": "المستوى 8: المخططات العلمية وتحليل البيانات الرصدية",
        "difficulty": "advanced",
        "questions": [
            {
                "id": 71,
                "qEn": "What does the famous 'Keeling Curve' chart, initiated by Charles David Keeling at Mauna Loa Observatory in 1958, directly record?",
                "qAr": "ما الذي يسجله ويوثقه 'منحنى كيلينغ' (Keeling Curve) الشهير في مرصد مونا لوا بهاواي منذ عام 1958؟",
                "optionsEn": ["Global ocean sea surface salinity", "Atmospheric Carbon Dioxide (CO₂) concentration in ppm", "Stratospheric ozone depletion rate", "Solar flare frequency"],
                "optionsAr": ["ملوحة سطح المحيطات", "تركيز غاز ثاني أكسيد الكربون (CO₂) في الغلاف الجوي بالأجزاء في المليون (ppm)", "معدل تآكل أوزون الستراتوسفير", "تكرار التوهجات الشمسية"],
                "correct": 1,
                "explanationEn": "The Keeling Curve continuous time series documents the steady rise in atmospheric CO₂ from ~315 ppm in 1958 to over 420 ppm today, along with seasonal photosynthetic oscillations.",
                "explanationAr": "يوثق منحنى كيلينغ التزايد المستمر لتركيز ثاني أكسيد الكربون من 315 جزءاً بالمليون في 1958 إلى أكثر من 420 جزءاً بالمليون حالياً مع تذبذبات التنفس النباتي الموسمي.",
                "source": "Scripps Institution of Oceanography / NOAA ESRL"
            },
            {
                "id": 72,
                "qEn": "In climatology, what does a 'temperature anomaly' of +1.2°C signify relative to a 1951–1980 baseline?",
                "qAr": "ماذا يعني 'شذوذ درجة الحرارة' (Temperature Anomaly) بمقدار +1.2°C مقارنة بخط الأساس 1951-1980؟",
                "optionsEn": ["The actual temperature was 1.2°C absolute", "The observed period is 1.2°C warmer than the long-term baseline average", "A measurement margin of error of 1.2 degrees", "Daytime temperature exceeded nighttime by 1.2°C"],
                "optionsAr": ["أن درجة الحرارة المطلقة كانت 1.2 مئوية", "أن الفترة المرصودة أدفأ بمقدار 1.2 درجة مئوية عن متوسط خط الأساس المرجعي", "أن هامش الخطأ في الرصد 1.2 درجة", "أن النهار كان أدفأ من الليل بـ 1.2 درجة"],
                "correct": 1,
                "explanationEn": "A temperature anomaly represents the deviation (departure) of observed temperature from a long-term reference average, filtering out elevation and local biases.",
                "explanationAr": "شذوذ درجة الحرارة هو مقدار انحراف القيمة المقاسة عن المتوسط المناخي المرجعي لسنوات خط الأساس، مما يزيل تأثير التضاريس المحلية.",
                "source": "NASA GISS Surface Temperature Analysis (GISTEMP)"
            },
            {
                "id": 73,
                "qEn": "What do the saw-tooth seasonal oscillations visible on the annual Keeling Curve reflect?",
                "qAr": "ما الذي تعكسه التذبذبات السنوية الشبيهة بأسنان المنشار على منحنى كيلينغ لغاز CO₂؟",
                "optionsEn": ["Orbital distance fluctuations", "Seasonal photosynthetic draw-down by Northern Hemisphere terrestrial vegetation", "Volcanic winter eruptions", "Solar cycle variations"],
                "optionsAr": ["تقلبات المسافة المدارية للأرض", "امتصاص النباتات في النصف الشمالي للـ CO₂ خلال الصيف وإطلاقه بالخريف والشتاء", "انبعاثات البراكين الدورية", "دورات النشاط الشمسي"],
                "correct": 1,
                "explanationEn": "Because landmass and deciduous vegetation predominate in the Northern Hemisphere, spring and summer photosynthesis absorbs atmospheric CO₂, causing an annual cyclical drop.",
                "explanationAr": "نظراً لتركز معظم اليابسة والغابات النفضية في نصف الكرة الشمالي، يسحب النمو النباتي الربيعي غاز CO₂ فينخفض التركيز صيفاً ويرتفع شتاءً.",
                "source": "Scripps / NOAA Climate.gov"
            },
            {
                "id": 74,
                "qEn": "Which satellite altimetry missions have provided continuous, precision measurements of global mean sea level rise since 1992?",
                "qAr": "أي سلسلة من مهمات الأقمار الصناعية الرادارية وفرت قياسات متصلة وفائقة الدقة لارتفاع مستوى سطح البحر منذ 1992؟",
                "optionsEn": ["Landsat series", "TOPEX/Poseidon, Jason-1, Jason-2, Jason-3, and Sentinel-6 Michael Freilich", "Hubble Space Telescope", "Meteosat-1"],
                "optionsAr": ["سلسلة لاندسات (Landsat)", "مهمات TOPEX/Poseidon، وسلسلة Jason، وقمر Sentinel-6", "تلسكوب هابل الفضائي", "ميتيوسات 1"],
                "correct": 1,
                "explanationEn": "Radar altimeters on TOPEX/Poseidon, Jason 1-3, and Sentinel-6 have tracked global mean sea level rise at ~3.4 mm/year with millimeter accuracy since 1992.",
                "explanationAr": "سلسلة أقمار مقاييس الارتفاع الرادارية المشتركة بين ناسا والوكالة الفرنسية والأوروبية ترصد ارتفاع البحار بمعدل ~3.4 ملم/سنة بدقة مليمترية.",
                "source": "NASA JPL / CNES / EUMETSAT"
            },
            {
                "id": 75,
                "qEn": "What twin-satellite mission measures monthly variations in Earth's gravitational field to track mass loss in ice sheets and aquifers?",
                "qAr": "ما هي المهمة الفضائية التوأم التي تقيس تغيرات حقل الجاذبية الأرضية شهرياً لتتبع ذوبان الصفائح الجليدية والمياه الجوفية؟",
                "optionsEn": ["GRACE and GRACE-Follow-On (GRACE-FO)", "Voyager 1 and 2", "Aqua and Terra", "CALIPSO and CloudSat"],
                "optionsAr": ["مهمة جريس التوأم وجريس-FO (GRACE & GRACE-FO)", "فوياجر 1 و 2", "أكوا وتيرا", "كاليبسو وكلودسات"],
                "correct": 0,
                "explanationEn": "GRACE (Gravity Recovery and Climate Experiment) tracks microscopic distance changes between two satellites caused by gravitational mass changes like melting ice.",
                "explanationAr": "تقيس مهمة جريس التغيرات الميكرونية في المسافة بين القمرين الناتجة عن اختلاف قوى الجاذبية الأرضية عند تغير كتل المياه والجليد.",
                "source": "NASA JPL / German Aerospace Center (DLR)"
            },
            {
                "id": 76,
                "qEn": "What paleoclimatological archive provides continuous, high-resolution direct samples of ancient atmospheric gas bubbles dating back 800,000 years?",
                "qAr": "ما هو الأرشيف المناخي الطبيعي الذي يوفر عينات مباشرة من فقاعات الهواء المحتبسة في الغلاف الجوي القديم حتى 800 ألف سنة؟",
                "optionsEn": ["Tree rings (Dendrochronology)", "Antarctic deep ice cores (e.g., EPICA Dome C)", "Speleothems in caves", "Fossilized pollen"],
                "optionsAr": ["حلقات نمو الأشجار", "عينات اللباب الجليدي العميق في أنتاركتيكا (مثل EPICA Dome C)", "صواعد ونوازل الكهوف", "حبوب اللقاح المتحجرة"],
                "correct": 1,
                "explanationEn": "Antarctic ice cores (like EPICA Dome C) preserve trapped air bubbles yielding direct samples of ancient greenhouse gas concentrations over 8 glacial-interglacial cycles.",
                "explanationAr": "عينات اللباب الجليدي في أنتاركتيكا (مشروع EPICA) تحتجز فقاعات هواء أصلية محصورة توثق تركيز الغازات على مدى 800,000 عام عبر 8 دورات جليدية.",
                "source": "EPICA Community Members / Nature 2004"
            },
            {
                "id": 77,
                "qEn": "In satellite remote sensing, what does the Normalized Difference Vegetation Index (NDVI) measure?",
                "qAr": "ما الذي يقيسه مؤشر الاختلاف الخضري الطبيعي (NDVI) في الاستشعار عن بعد عبر الأقمار الصناعية؟",
                "optionsEn": ["Soil moisture depth", "Photosynthetic density and green vegetation canopy health", "Ocean surface salinity", "Atmospheric aerosol density"],
                "optionsAr": ["عمق رطوبة التربة", "كثافة البناء الضوئي وصحة الغطاء النباتي الأخضر (NDVI)", "ملوحة مياه البحر", "كثافة الهباء الجوي في السحب"],
                "correct": 1,
                "explanationEn": "NDVI uses the ratio (NIR - Red) / (NIR + Red) because healthy chlorophyll absorbs red light and strongly reflects near-infrared (NIR) wavelengths.",
                "explanationAr": "يعتمد مؤشر NDVI على مقارنة امتصاص الكلوروفيل للضوء الأحمر وانعكاسه القوي للأشعة تحت الحمراء القريبة لتحديد حيوية النبات.",
                "source": "USGS Earth Resources Observation and Science (EROS) Center"
            },
            {
                "id": 78,
                "qEn": "What is the primary contribution to global sea level rise alongside thermal expansion of ocean water?",
                "qAr": "ما هو المكون الفيزيائي الرئيسي الآخر لارتفاع مستوى سطح البحر إلى جانب التمدد الحراري للمياه؟",
                "optionsEn": ["Rainfall over oceans", "Mass loss from land-based glaciers and continental ice sheets", "Sediment runoff from rivers", "Submarine volcanic eruptions"],
                "optionsAr": ["هطول الأمطار على المحيطات", "ذوبان وكتل الجليد المتساقطة من الأنهار الجليدية والصفائح القارية على اليابسة", "الرواسب الطينية للأنهار", "الثورات البركانية القاعية"],
                "correct": 1,
                "explanationEn": "Global sea level rise is driven primarily by two mechanisms: thermal expansion of warming ocean water and the addition of water from melting land ice (glaciers and ice sheets).",
                "explanationAr": "يقود ارتفاع البحار عاملان رئيسيان: التمدد الحراري لماء المحيط عند ارتفاع حرارته، وإضافة كتل مائية جديدة من ذوبان جليد اليابسة والصفائح القارية.",
                "source": "IPCC Sixth Assessment Report (AR6) WG1"
            },
            {
                "id": 79,
                "qEn": "What does an ocean temperature-salinity (T-S) diagram classify and track in physical oceanography?",
                "qAr": "ما الذي يساعد مخطط الحرارة والملوحة (T-S Diagram) في تصنيفه وتتبعه في علم المحيطات الفيزيائي؟",
                "optionsEn": ["Whale migration routes", "Distinct oceanic water masses and density stratification", "Tsunami wave velocities", "Coral bleaching risk only"],
                "optionsAr": ["مسارات هجرة الحيتان", "الكتل المائية المحيطية المختلفة وتطابق كثافاتها (Water Masses)", "سرعات موجات التسونامي", "مخاطر ابيضاض المرجان"],
                "correct": 1,
                "explanationEn": "T-S diagrams allow oceanographers to identify distinct water masses (e.g., Antarctic Bottom Water, North Atlantic Deep Water) by their conservative thermodynamic signatures.",
                "explanationAr": "يستخدم علماء المحيطات مخطط T-S لتحديد الكتل المائية المحيطية الفريدة (مثل مياه قاع أنتاركتيكا ومياه شمال الأطلسي العميقة) وتتبع اختلاطها.",
                "source": "Descriptive Physical Oceanography / Talley et al."
            },
            {
                "id": 80,
                "qEn": "How does Effective Radiative Forcing (+2.72 W/m², IPCC AR6) fundamentally differ from Earth's observed Energy Imbalance (EEI)?",
                "qAr": "كيف يختلف التأثير الإشعاعي الفعال (+2.72 واط/م² في تقرير IPCC AR6) جوهرياً عن اختلال ميزانية طاقة الأرض المقاس (EEI)؟",
                "optionsEn": ["They describe identical quantities under different names", "Radiative forcing measures the imposed net energy perturbation relative to 1750, whereas EEI is the actual ongoing net heat uptake rate (CERES/Argo ~0.76 W/m²)", "Radiative forcing only accounts for solar cycles", "EEI measures core geothermal flow alone"],
                "optionsAr": ["أنهما يعبران عن نفس المقدار تماماً بأسماء مختلفة", "التأثير الإشعاعي يقيس اضطراب الطاقة الصافي المفروض مقارنة بعام 1750، بينما EEI هو المعدل الفعلي لامتصاص وتخزين الحرارة حالياً في المحيطات (~0.76 واط/م²)", "التأثير الإشعاعي يقيس دورات الشمس فقط", "EEI يقيس تدفق حرارة باطن الأرض وحدها"],
                "correct": 1,
                "explanationEn": "Radiative forcing (+2.72 W/m² relative to 1750) is the unadjusted external perturbation. As the planet warms, Planck and other feedbacks increase outgoing infrared radiation, leaving the actual observed Earth's Energy Imbalance (EEI) at ~0.76 to 1.0 W/m² absorbed mainly by oceans.",
                "explanationAr": "التأثير الإشعاعي هو الاضطراب الخارجي المحتجز للطاقة (+2.72 واط/م²). ومع ارتفاع حرارة الكوكب، تشع الأرض مزيداً من الأشعة تحت الحمراء إلى الفضاء، فيصبح صافي اختلال طاقة الأرض الحقيقي المخزن في المحيطات (EEI) بين 0.76 و 1.0 واط/م².",
                "source": "IPCC AR6 WG1 Chapter 7 / Loeb et al., Geophysical Research Letters (CERES & Argo)"
            }
        ]
    },
    {
        "level": 9,
        "titleEn": "Level 9: Earth Systems & Biogeochemistry",
        "titleAr": "المستوى 9: أنظمة الأرض المعقدة والتفاعلات الجيوكيميائية",
        "difficulty": "very_advanced",
        "questions": [
            {
                "id": 81,
                "qEn": "What geological event ~2.4 to ~2.1 billion years ago permanently oxygenated Earth's atmosphere via cyanobacterial photosynthesis?",
                "qAr": "ما هو الحدث الجيولوجي الحاسم قبل نحو 2.4 إلى 2.1 مليار سنة الذي أدى لتراكم الأكسجين الحر في الغلاف الجوي؟",
                "optionsEn": ["Cambrian Explosion", "Great Oxidation Event (GOE)", "Late Heavy Bombardment", "Permian-Triassic extinction"],
                "optionsAr": ["الانفجار الكامبري", "حدث الأكسدة العظيم (Great Oxidation Event - GOE)", "القصف الشديد المتأخر", "انقراض العصر البرمي"],
                "correct": 1,
                "explanationEn": "The Great Oxidation Event occurred when oceanic iron sinks were exhausted, allowing biogenic oxygen from cyanobacteria to accumulate in the atmosphere.",
                "explanationAr": "حدث الأكسدة العظيم وقع عندما تشبعت مركبات الحديد الذائب في المحيطات وبدأ الأكسجين الناتج عن البكتيريا الزرقاء بالتراكم في الغلاف الجوي.",
                "source": "Nature / Scientific American / PNAS"
            },
            {
                "id": 82,
                "qEn": "What process in the long-term geological carbon cycle acts as Earth's natural multi-million-year thermostat by removing CO₂ through chemical reactions with silicate rocks?",
                "qAr": "ما هي العملية الجيوكيميائية طويلة الأمد التي تعمل كـ'منظم حراري' للأرض بسحب غاز CO₂ عبر التفاعل مع صخور السيليكات؟",
                "optionsEn": ["Volcanic degassing", "Silicate weathering (Carbonate-Silicate cycle)", "Mantle convection", "Subduction melting"],
                "optionsAr": ["الانبعاث البركاني الغازي", "التجوية الكيميائية لصخور السيليكات (Silicate Weathering)", "الحمل الحراري للوشاح", "انصهار القشرة المنغرزة"],
                "correct": 1,
                "explanationEn": "Silicate weathering reacts atmospheric CO₂ dissolved in rainwater with silicate minerals to form bicarbonate ions, which rivers transport to oceans to form carbonate limestone.",
                "explanationAr": "تتفاعل صخور السيليكات مع الأمطار الحمضية المحملة بـ CO₂ لتكوين الكربونات التي تترسب كصخور كلسية، ما يسحب الكربون من الجو على مدى ملايين السنين.",
                "source": "Walker, Hays, and Kasting (1981) / Nature Geoscience"
            },
            {
                "id": 83,
                "qEn": "What is the primary thermodynamic mechanism driving convection currents in Earth's mantle and plate motion?",
                "qAr": "ما هي الآلية الثرموديناميكية الأساسية التي تحرك تيارات الحمل الحراري في الوشاح وتدفع حركة الصفائح التكتونية؟",
                "optionsEn": ["Solar radiation absorption", "Radioactive decay of primordial isotopes (U, Th, K) combined with primordial heat of planetary accretion", "Ocean tidal drag", "Electromagnetic Lorentz forces"],
                "optionsAr": ["امتصاص الإشعاع الشمسي السطحي", "التحلل الإشعاعي للنظائر المشعة (اليورانيوم والثوريوم والبوتاسيوم) مع حرارة تشكل الأرض البدائية", "احتكاك المد والجزر المحيطي", "قوى لورنتز الكهرومغناطيسية"],
                "correct": 1,
                "explanationEn": "Mantle convection is powered by radioactive decay of unstable isotopes (238U, 235U, 232Th, 40K) and the release of primordial heat retained since Earth's formation.",
                "explanationAr": "تتولد طاقة حمل الوشاح من التحلل الإشعاعي لنظائر اليورانيوم والثوريوم والبوتاسيوم المشعة، بالإضافة إلى الحرارة الكامنة منذ اصطدام وتشكل الأرض.",
                "source": "Geological Society of America / Treatise on Geophysics"
            },
            {
                "id": 84,
                "qEn": "What geochemical anomaly found in the K-Pg boundary clay layer globally provided primary evidence for an extraterrestrial asteroid impact 66 million years ago?",
                "qAr": "ما هو العنصر الكيميائي النادر الذي اكتُشف بتركيزات عالية في طبقة طمي الحد الفاصل K-Pg وأثبت اصطدام كويكب قبل 66 مليون سنة؟",
                "optionsEn": ["Titanium anomaly", "Iridium anomaly (Alvarez hypothesis)", "Uranium anomaly", "Silicon enrichment"],
                "optionsAr": ["شذوذ عنصر التيتانيوم", "شذوذ عنصر الإيريديوم (Iridium Anomaly)", "شذوذ اليورانيوم", "إثراء السيليكون"],
                "correct": 1,
                "explanationEn": "Luis and Walter Alvarez discovered a global clay layer enriched in iridium—an element depleted on Earth's crust but abundant in asteroids—proving the Chicxulub impact.",
                "explanationAr": "اكتشف لويس ووالتر ألفاريز طبقة إيريديوم غنية عالمياً، وهو عنصر نادر جداً في قشرة الأرض ولكنه وفير في النيازك، مما أكد اصطدام كويكب تشيكشولوب.",
                "source": "Alvarez et al., Science 1980 / Lunar and Planetary Institute"
            },
            {
                "id": 85,
                "qEn": "What is the geodynamo effect responsible for generating Earth's planetary magnetic field?",
                "qAr": "ما هي الآلية الفيزيائية المسماة 'الدينامو الجيولوجي' (Geodynamo) المسؤولة عن توليد المجال المغناطيسي للأرض؟",
                "optionsEn": ["Permanent magnetization of surface crustal magnetite", "Convection and Coriolis helical motion of molten electrically conductive iron in the liquid outer core", "Static charges in the lower mantle", "Ionospheric solar currents"],
                "optionsAr": ["المغناطيسية الدائمة لخام المغنيتيت في القشرة", "حركة الحمل وتأثير كوريوليس للحديد السائل الموصل للكهرباء في اللب الخارجي", "الشحنات الساكنة في الوشاح السفلي", "التيارات الشمسية في طبقة الأيونوسفير"],
                "correct": 1,
                "explanationEn": "Thermal and compositional convection of molten iron in Earth's outer core, organized into columnar helices by Coriolis forces, produces self-sustaining magnetic dynamo action.",
                "explanationAr": "يولد دوران الأرض وتأثير كوريوليس حركة لولبية لتيارات الحديد والنيكل السائلة الموصلة في اللب الخارجي، مما ينتج تياراً كهربائياً وحقلاً مغناطيسياً مستداماً.",
                "source": "Nature / Annual Review of Earth and Planetary Sciences"
            },
            {
                "id": 86,
                "qEn": "What sudden paleoclimate hyperthermal event ~56 million years ago caused global temperatures to spike by 5–8°C over tens of thousands of years?",
                "qAr": "ما هو الحدث المناخي الفجائي قبل نحو 56 مليون سنة الذي قفز بدرجات الحرارة العالمية بنحو 5 إلى 8 درجات مئوية؟",
                "optionsEn": ["Younger Dryas", "Paleocene-Eocene Thermal Maximum (PETM)", "Eemian Interglacial", "Little Ice Age"],
                "optionsAr": ["درياس الأصغر", "الحد الأقصى الحراري للباليوسين والإيوسين (PETM)", "فترة إيميان بين الجليدية", "العصر الجليدي الصغير"],
                "correct": 1,
                "explanationEn": "The PETM was marked by an enormous release of carbon (~3,000–7,000 Gt) into Earth's exogenic system, driving rapid global warming and widespread deep-sea ocean acidification.",
                "explanationAr": "الحد الأقصى الحراري (PETM) شهد انبعاثاً هائلاً للكربون قاد إلى احترار عالمي سريع وتحمض في المحيطات، ويعد نظيراً جيولوجياً لتغير المناخ الحالي.",
                "source": "Nature Geoscience / Science"
            },
            {
                "id": 87,
                "qEn": "What is the critical phenomenon called where the melting of reflective polar ice exposes darker ocean water, absorbing more solar radiation and accelerating warming?",
                "qAr": "ماذا تسمى ظاهرة التغذية الراجعة التي يؤدي فيها ذوبان الجليد الأبيض إلى كشف مياه بحر داكنة تمتص حرارة أكثر وتسرع الذوبان؟",
                "optionsEn": ["Ice-albedo feedback", "Cloud condensation nuclei effect", "Thermohaline shutdown", "Biogeochemical saturation"],
                "optionsAr": ["التغذية الراجعة لبياض الجليد (Ice-Albedo Feedback)", "تأثير نوى تكاثف السحب", "توقف الدورة الحرارية", "التشبع البيوجيوكيميائي"],
                "correct": 0,
                "explanationEn": "Sea ice has a high albedo (~0.5–0.7), reflecting solar energy, whereas open ocean has a low albedo (~0.06), absorbing ~94% of insolation and magnifying warming in a positive feedback loop.",
                "explanationAr": "يعكس الجليد نحو 60% من ضوء الشمس، بينما يمتص البحر المكشوف 94% من الطاقة، مما يرفع حرارة المياه ويسرع من وتيرة الذوبان في حلقة تعزيز ذاتي.",
                "source": "National Snow and Ice Data Center (NSIDC)"
            },
            {
                "id": 88,
                "qEn": "What is the Gutenberg Discontinuity in deep Earth geophysics?",
                "qAr": "ما هو 'انقطاع غوتنبرغ' (Gutenberg Discontinuity) في فيزياء باطن الأرض؟",
                "optionsEn": ["The boundary between continental crust and oceanic crust", "The core-mantle boundary (CMB) at ~2,890 km depth separating solid silicate mantle from liquid outer core", "The boundary between inner and outer core", "The base of the oceanic sediment layer"],
                "optionsAr": ["الحد الفاصل بين القشرة القارية والمحيطية", "الحد الفاصل بين الوشاح الصخري الصلب واللب الخارجي السائل على عمق 2890 كم (Core-Mantle Boundary)", "الحد الفاصل بين اللب الداخلي والخارجي", "قاع الرواسب البحرية"],
                "correct": 1,
                "explanationEn": "Discovered by Beno Gutenberg, this boundary at ~2,891 km marks a sharp discontinuity where seismic S-waves terminate (proving the outer core is liquid) and P-wave velocity drops.",
                "explanationAr": "انقطاع غوتنبرغ على عمق 2890 كم يفصل بين وشاح الأرض الصلب ولبها الخارجي السائل، وتتوقف عنده موجات القص الزلزالية (S-waves) لأنها لا تعبر السوائل.",
                "source": "USGS Geophysics / Bull. Seismol. Soc. Am."
            },
            {
                "id": 89,
                "qEn": "What boundary marks the sharp jump in seismic wave velocities between Earth's solid crust and the denser peridotite uppermost mantle?",
                "qAr": "ما هو الحد الفاصل الشهير الذي تقفز عنده سرعة الموجات الزلزالية بين القشرة الأرضية ووشاح الأرض العلوي؟",
                "optionsEn": ["Mohorovičić Discontinuity (Moho)", "Lehmann Discontinuity", "Conrad Discontinuity", "Gutenberg Discontinuity"],
                "optionsAr": ["انقطاع موهوروفيتش / الموهو (Mohorovičić Discontinuity - Moho)", "انقطاع ليمان", "انقطاع كونراد", "انقطاع غوتنبرغ"],
                "correct": 0,
                "explanationEn": "Andrija Mohorovičić discovered in 1909 that seismic waves refract and accelerate sharply at the crust-mantle boundary due to higher density peridotite rocks.",
                "explanationAr": "اكتشف موهوروفيتش عام 1909 انكسار وتسارع الموجات الزلزالية عند انتقالها من صخور القشرة إلى صخور البريدوتيت الأكثر كثافة في الوشاح العلوي.",
                "source": "USGS Earthquake Science / Encyclopaedia Britannica"
            },
            {
                "id": 90,
                "qEn": "What is the primary role of the enzyme RuBisCO in photosynthetic carbon assimilation within the Calvin-Benson cycle?",
                "qAr": "ما هو الدور البيوكيميائي الرئيسي لإنزيم الروبيسكو (RuBisCO) في تثبيت الكربون في دورة كالفن-بنسون للبناء الضوئي؟",
                "optionsEn": ["Synthesizing ATP from ADP and phosphate", "Catalyzing the primary carboxylation of ribulose-1,5-bisphosphate (RuBP) with CO₂ to form 3-phosphoglycerate (3-PGA)", "Transcribing chloroplast messenger RNA", "Hydrolyzing complex starch into maltose"],
                "optionsAr": ["بناء مركب الطاقة ATP من الفوسفات", "تحفيز الكربكسلة الأولية لمركب ريبولوز 1،5-ثنائي الفوسفات (RuBP) بدمجه مع CO₂ لإنتاج 3-PGA", "نسخ الرنا المرسال في البلاستيدات الخضراء", "تحليل النشا المعقد إلى سكر مالتوز"],
                "correct": 1,
                "explanationEn": "RuBisCO does not synthesize glucose directly; it catalyzes the rate-limiting carboxylation step fusing CO₂ with RuBP into two 3-phosphoglycerate (3-PGA) precursors which the Calvin cycle subsequently reduces into triose-phosphate sugars.",
                "explanationAr": "لا يقوم الروبيسكو بإنتاج الجلوكوز مباشرة؛ بل يحفز الخطوة المحددة للسرعة عبر دمج CO₂ مع RuBP لتكوين جزيئين من 3-فوسفوغليسيرات (3-PGA)، ثم تُختزل لاحقاً في الدورة لإنتاج السكريات الثلاثية.",
                "source": "Berg et al., Biochemistry / Annual Review of Plant Biology"
            }
        ]
    },
    {
        "level": 10,
        "titleEn": "Level 10: Expert Earth Science Reasoning",
        "titleAr": "المستوى 10: التحدي العلمي والتحليل الفيزيائي والجيوفيزيائي",
        "difficulty": "expert",
        "questions": [
            {
                "id": 91,
                "qEn": "What physical property of seismic shear waves (S-waves) definitively proved that Earth's outer core is in a liquid state?",
                "qAr": "ما هي الخاصية الفيزيائية للموجات الزلزالية الثانوية (S-waves) التي أثبتت بشكل قاطع أن اللب الخارجي للأرض سائل؟",
                "optionsEn": ["They refract upwards toward the surface", "Transverse shear waves cannot propagate through fluids because liquids possess zero shear modulus (rigidity)", "They speed up by 200%", "They reverse their electrical polarity"],
                "optionsAr": ["أنها تنكسر لأعلى نحو السطح", "أن موجات القص المستعرضة لا تنتقل عبر السوائل لأن معامل صلابة السوائل يساوي صفراً", "أن سرعتها تزداد إلى الضعف", "أنها تقلب قطبيتها الكهربائية"],
                "correct": 1,
                "explanationEn": "Shear waves require shear stress restoring force to propagate. Since liquids have zero shear modulus (μ = 0), S-waves cannot travel through the liquid outer core, creating a global S-wave shadow zone.",
                "explanationAr": "موجات القص المستعرضة تتطلب وسيطاً ذا مقاومة للقص (صلابة). وبما أن معامل صلابة السوائل صفر، فإنها تنعدم تماماً عند ملامسة اللب الخارجي السائل مكونة منطقة ظل زلزالي.",
                "source": "Oldham (1906) / Shearer: Introduction to Seismology"
            },
            {
                "id": 92,
                "qEn": "What paleomagnetic pattern recorded in oceanic basalt stripes on either side of mid-ocean ridges provided critical confirmation of seafloor spreading?",
                "qAr": "ما هو النمط المغناطيسي القديم المسجل في بازلت قاع المحيط حول حيد منتصف الأطلسي الذي أكد اتساع قاع البحر؟",
                "optionsEn": ["Randomly scattered iron crystal orientations", "Symmetrical zebra-stripe patterns of magnetic polarity reversals (Vine-Matthews-Morley hypothesis)", "Uniform northward magnetization only", "Zero remanent magnetism"],
                "optionsAr": ["توجهات عشوائية غير منتظمة", "خطوط متناظرة من الانعكاسات المغناطيسية القطبية للأرض (Vine-Matthews-Morley)", "مغناطيسية شمالية موحدة دون أي تغير", "انعدام المغناطيسية تماماً"],
                "correct": 1,
                "explanationEn": "As magma solidifies at mid-ocean ridges, magnetic minerals align with Earth's current field. Symmetrical zebra stripes of normal and reversed polarity prove new crust is created continuously.",
                "explanationAr": "عندما تتصلب حمم البازلت عند حيد المحيط، تسجل بلورات الحديد اتجاه الحقل المغناطيسي للأرض وقت التصلب، مما شكل أشرطة متناظرة تثبت اتساع القاع مع كل انقلاب مغناطيسي.",
                "source": "Vine and Matthews (1963) / Nature"
            },
            {
                "id": 93,
                "qEn": "According to the Stefan-Boltzmann law and radiative equilibrium without an atmosphere, what would Earth's mean surface temperature be?",
                "qAr": "وفقاً لقانون ستيفان-بولتزمان والاتزان الإشعاعي دون غلاف جوي، كم ستكون درجة حرارة سطح الأرض؟",
                "optionsEn": ["Approximately +15°C", "Approximately -18°C (~255 Kelvin)", "Approximately -70°C", "Exactly 0°C"],
                "optionsAr": ["حوالي +15°C", "حوالي -18°C تحت الصفر (255 كلفن)", "حوالي -70°C", "صفر مئوية تماماً"],
                "correct": 1,
                "explanationEn": "Earth's effective blackbody radiation equilibrium temperature at planetary albedo 0.3 is ~255 K (-18°C). The natural greenhouse effect warms it by ~33°C to our hospitable mean of ~+15°C.",
                "explanationAr": "اتزان إشعاع الجسم الأسود لكوكب بوضاءة 0.3 يعطي حرارة -18 درجة مئوية تحت الصفر. وبفضل الاحتباس الحراري الطبيعي ترتفع الحرارة بنحو 33 درجة لتصل إلى +15 مئوية.",
                "source": "Pierrehumbert: Principles of Planetary Climate / NASA"
            },
            {
                "id": 94,
                "qEn": "What thermodynamic relationship dictates that atmospheric saturation vapor pressure increases by ~7% per 1°C of warming?",
                "qAr": "ما هي العلاقة الثرموديناميكية الفيزيائية التي تحدد أن ضغط تشبع بخار الماء في الهواء يزداد بنحو 7% لكل درجة مئوية ارتفاع في الحرارة؟",
                "optionsEn": ["Clapp-Hornberger pedotransfer soil water retention function", "Clausius-Clapeyron thermodynamic phase equilibrium relation", "Fourier's law of thermal conduction", "Navier-Stokes momentum conservation"],
                "optionsAr": ["دالة كلاب-هورنبرغر لخاصية احتباس مياه التربة المسامية", "معادلة كلاوزيوس-كلابيرون للاتزان الطوري للحرارة الكامنة (Clausius-Clapeyron)", "قانون فورييه للتوصيل الحراري", "معادلة نافيير-ستوكس لحركة الموائع"],
                "correct": 1,
                "explanationEn": "The Clausius-Clapeyron equation describes the vapor-liquid phase transition equilibrium where saturation vapor pressure rises ~6.5% to 7% per °C (unlike the Clapp-Hornberger formulation which models hydraulic soil-moisture retention curves).",
                "explanationAr": "معادلة كلاوزيوس-كلابيرون هي العلاقة الفيزيائية للاتزان الطوري لبخار الماء وتحدد زيادة ضغط التشبع بنحو 7% لكل درجة مئوية (بخلاف معادلة كلاب-هورنبرغر المخصصة لخصائص الاحتفاظ برطوبة التربة المسامية).",
                "source": "Held and Soden (2006) / IAPWS Formulation / Journal of Climate"
            },
            {
                "id": 95,
                "qEn": "In deep-mantle seismology, how do Large Low Shear Velocity Provinces (LLSVPs) differ from Ultra-Low Velocity Zones (ULVZs)?",
                "qAr": "في علم الزلازل لوشاح الأرض العميق، كيف تختلف المقاطعات الكبرى منخفضة سرعة القص (LLSVPs) عن مناطق السرعة الفائقة الانخفاض (ULVZs)؟",
                "optionsEn": ["They are identical features discovered by different authors", "LLSVPs are continent-sized structures (~thousands of km wide, hundreds of km high) beneath Africa and the Pacific, whereas ULVZs are thin, concentrated basal patches (5-40 km thick) directly atop the core-mantle boundary with extreme velocity drops (up to -30% to -50%)", "LLSVPs are located in the upper crust while ULVZs are inside the inner core", "ULVZs are caused only by oceanic tides"],
                "optionsAr": ["هما نفس التركيب الجيولوجي تماماً", "مقاطعات LLSVP هي كتل عملاقة بحجم القارات (آلاف الكيلومترات عرضاً ومئات الكيلومترات ارتفاعاً) تحت إفريقيا والهادئ، بينما ULVZs هي رقع قاعدية رقيقة (سمكها 5-40 كم فقط) فوق اللب مباشرة وتتميز بهبوط زلزالي فائق العنف يصل إلى -30% حتى -50%", "تقع LLSVPs في القشرة السطحية بينما ULVZs داخل اللب الداخلي", "تنشأ ULVZs بسبب مد وجزر المحيطات فقط"],
                "correct": 1,
                "explanationEn": "LLSVPs are massive, thermochemical piles thousands of kilometers wide. In contrast, ULVZs are localized, thin (5–40 km thick) lenses with dramatic seismic velocity drops (-10% to -30% for P-waves, -30% to -50% for S-waves), likely representing partial melt or iron-enriched basal magma remnants.",
                "explanationAr": "مقاطعات LLSVPs كتل وشاحية هائلة بعرض آلاف الكيلومترات، في حين أن مناطق ULVZs هي عدسات موضعية شديدة الرقة (5-40 كم) فوق اللب مباشرة تشهد انخفاضاً زلزالياً فائقاً (-30% إلى -50% لموجات القص) وتشير إلى انصهار جزئي أو صخور غنية جداً بالحديد.",
                "source": "Garnero, McNamara, and Shim (2016), Nature Geoscience / Thorne and Garnero (2004)"
            },
            {
                "id": 96,
                "qEn": "What is the mass balance difference in the cryosphere between accumulation and ablation called?",
                "qAr": "ماذا يسمى الفرق الصافي بين تراكم الجليد وذوبانه أو تبخره (Ablation) في نهر جليدي؟",
                "optionsEn": ["Glacial mass balance", "Isostatic equilibrium", "Crevasse stress index", "Firn compaction ratio"],
                "optionsAr": ["ميزان الكتلة الجليدي (Glacial Mass Balance)", "التوازن الإيزوستاتي", "مؤشر إجهاد الصدوع الجليدية", "نسبة انضغاط الفيرن"],
                "correct": 0,
                "explanationEn": "Glacial mass balance is the difference between snow accumulation and mass loss (ablation via melting, sublimation, and calving). A negative balance causes glacier retreat.",
                "explanationAr": "ميزان الكتلة الجليدي هو الفارق الصافي بين تراكم الثلوج وفقدان الكتلة (الذوبان والانفصال والتبخر). والميزان السالب يعني تراجع النهر الجليدي وتقلصه.",
                "source": "World Glacier Monitoring Service (WGMS) / UNESCO"
            },
            {
                "id": 97,
                "qEn": "What parameter describes the ratio of reflected solar electromagnetic radiation from a planetary surface to total incoming radiation?",
                "qAr": "ما هو المصطلح الفيزيائي الذي يعبر عن نسبة الإشعاع الشمسي المنعكس من سطح الكوكب مقارنة بإجمالي الإشعاع الساقط؟",
                "optionsEn": ["Emissivity", "Bond Albedo / Planetary Albedo", "Refractive Index", "Transmittance"],
                "optionsAr": ["الانبعاثية الإشعاعية", "البياض الكوكبي / الوضاءة (Planetary Albedo)", "معامل الانكسار", "معامل النفاذية"],
                "correct": 1,
                "explanationEn": "Albedo is the dimensionless fraction of incident electromagnetic radiation reflected by a surface. Earth's global average Bond albedo is approximately 0.29 to 0.30.",
                "explanationAr": "الوضاءة (Albedo) هي نسبة الضوء والإشعاع المنعكس عن السطح. وتبلغ وضاءة كوكب الأرض الإجمالية حوالي 0.30 (تعكس 30% وتمتص 70%).",
                "source": "NASA Earth Radiation Budget Experiment (ERBE / CERES)"
            },
            {
                "id": 98,
                "qEn": "What geochemical proxy is most commonly analyzed in benthic foraminiferal calcite shells to reconstruct historical ocean temperatures and global ice volume?",
                "qAr": "ما هو النظير الجيوكيميائي المقاس في أصداف كائنات الفورامينيفرا لإعادة بناء درجات حرارة المحيطات وحجم الجليد القديم؟",
                "optionsEn": ["Carbon-14 (14C)", "Oxygen isotope ratio (δ18O relative to δ16O)", "Strontium-90", "Potassium-40"],
                "optionsAr": ["نظير الكربون 14", "نسبة نظائر الأكسجين (δ18O مقارنة بـ 16O)", "السترونشيوم 90", "البوتاسيوم 40 المشع"],
                "correct": 1,
                "explanationEn": "Because lighter 16O evaporates preferentially and is locked in continental ice sheets during glacials, ocean water and foraminifera calcite shells become enriched in heavy 18O.",
                "explanationAr": "نظراً لأن الأكسجين الخفيف 16 يتبخر أسهل ويحتجز في جليد القارات، فإن مياه المحيطات وأصداف الكائنات تثري بالأكسجين الثقيل 18 خلال العصور الجليدية.",
                "source": "Zachos et al., Science 2001 / Lisiecki and Raymo (2005)"
            },
            {
                "id": 99,
                "qEn": "What principle in physical geology and mechanics describes the gravitational equilibrium between Earth's lithosphere and the asthenosphere, where tectonic plates 'float' according to their thickness and density?",
                "qAr": "ما هو المبدأ الجيولوجي والميكانيكي الذي يفسر الطفو والاتزان الجاذبي للغلاف الصخري فوق الغلاف الموري اللدن؟",
                "optionsEn": ["Archimedean Buoyancy alone", "Isostasy (Airy and Pratt models)", "Pascal's Law", "Bernoulli Principle"],
                "optionsAr": ["قانون أرخميدس للطفو المائي فقط", "التوازن التضاغطي / الإيزوستاسية (Isostasy - نماذج آيري وبرات)", "قانون باسكال", "مبدأ برنولي"],
                "correct": 1,
                "explanationEn": "Isostasy explains how topographical loads like high mountain ranges possess deep crustal roots extending into the mantle, balancing buoyant and gravitational forces.",
                "explanationAr": "الإيزوستاسية (التوازن التضاغطي) تشرح كيف تمتلك الجبال العالية جذوراً قشرية عميقة تغوص في الوشاح لتحقيق اتزان الطفو والجاذبية مثل الجبال الجليدية.",
                "source": "Watts: Isostasy and Flexure of the Lithosphere"
            },
            {
                "id": 100,
                "qEn": "What is the formal stratigraphic and Earth system science status of the proposed 'Anthropocene' epoch as evaluated by the International Commission on Stratigraphy (ICS / IUGS)?",
                "qAr": "ما هو الوضع الطباقي والعلمي الرسمي لمصطلح 'الأنثروبوسين' (Anthropocene) وفقاً لتقييم اللجنة الدولية للطبقات والاتحاد الدولي للعلوم الجيولوجية (ICS / IUGS)؟",
                "optionsEn": ["An officially ratified geological period replacing the Quaternary", "A powerful interdisciplinary Earth system concept marking human impact, which was formally rejected in 2024 by the ICS/IUGS as an official chronostratigraphic unit", "A myth with no measurable scientific evidence", "A recognized Mesozoic subdivision"],
                "optionsAr": ["عصر جيولوجي رسمي معتمد بالكامل بديلاً للعصر الرباعي", "مفهوم علمي قوي في علوم نظام الأرض يصف التأثير البشري، لكنه رُفض رسمياً عام 2024 من قبل اللجنة الدولية للطبقات (ICS) كوحدة زمنية جيولوجية رسمية على المقياس الدولي", "أسطورة غير مدعومة بأي أدلة رصدية", "أحد أقسام حقبة الحياة الوسطى"],
                "correct": 1,
                "explanationEn": "In March 2024, the Subcommission on Quaternary Stratigraphy and IUGS voted against ratifying the Anthropocene as a formal geological epoch (favoring its continued use as an overarching, informal Earth-system geological 'event').",
                "explanationAr": "في مارس 2024، صوتت اللجنة الفرعية للطبقات الرباعية والاتحاد الدولي للعلوم الجيولوجية (IUGS) بعدم إدراج الأنثروبوسين كعصر رسمي في الجدول الطباقي القياسي، مع تفضيل استخدامه كمفهوم علمي أو 'حدث جيولوجي' يصف التأثيرات البشرية الكوكبية.",
                "source": "International Commission on Stratigraphy (ICS) / IUGS Statement March 2024 / Nature News"
            }
        ]
    }
]
