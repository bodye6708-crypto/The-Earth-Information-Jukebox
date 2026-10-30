"""
Educational Children's Stories on Earth Science and Geosphere
Includes dual-language narration, questions, and learning path.
"""

CHILDREN_STORIES = [
    {
        "id": "blue_marble",
        "titleEn": "The Blue Marble in the Sky",
        "titleAr": "الرخامة الزرقاء في أعماق الفضاء",
        "targetAge": "6-12",
        "character": "Captain Astro & Sparky the Satellite",
        "coverImage": "/textures/earth_nasa_day.jpg",
        "chapters": [
            {
                "chapterNumber": 1,
                "titleEn": "A World Floating in the Dark",
                "titleAr": "عالم يسبح في الظلام السحيق",
                "textEn": "When astronauts look out from the International Space Station, Earth looks like a glowing blue marble swirling with white clouds, floating peacefully in the deep velvet darkness of space.",
                "textAr": "عندما ينظر رواد الفضاء من نافذة محطة الفضاء الدولية، يظهر كوكب الأرض كأنه رخامة زرقاء لامعة تلتف حولها غيوم بيضاء ناصعة، تسبح في هدوء داخل ظلمة الفضاء المخملية.",
                "audioPrompt": "Look down at Earth! Isn't our home wonderful with its bright blue oceans and swirling white clouds?",
                "interactiveQuestion": {
                    "qEn": "Why does Earth look predominantly blue from space?",
                    "qAr": "لماذا يظهر كوكب الأرض بلون أزرق ساطع من الفضاء الخارجي؟",
                    "optionsEn": ["Because of blue flowers", "Because oceans cover 71% of its surface", "Because of blue rocks"],
                    "optionsAr": ["بسبب الأزهار الزرقاء", "لأن المحيطات تغطي 71% من مساحة سطحه", "بسبب الصخور الزرقاء"],
                    "correct": 1
                }
            },
            {
                "chapterNumber": 2,
                "titleEn": "The Magic Shield: Our Atmosphere",
                "titleAr": "الدرع السحري: غلافنا الجوي",
                "textEn": "Earth wears a thin, glowing blanket of air called the atmosphere. It protects us from space rocks, filters harsh radiation, and gives every animal, plant, and child clean air to breathe!",
                "textAr": "يرتدي كوكب الأرض بطانية رقيقة مضيئة من الهواء تسمى الغلاف الجوي. إنه يحمينا من الشهب والنيازك الفضائية، ويصفي أشعة الشمس القاسية، ويمنحنا الهواء العليل لنتنفس!",
                "interactiveQuestion": {
                    "qEn": "What layer of the atmosphere gives us the air we breathe and our weather?",
                    "qAr": "ما هي طبقة الغلاف الجوي التي تمنحنا الهواء الذي نتنفسه وتصنع طقسنا والغيوم؟",
                    "optionsEn": ["Troposphere", "Outer Space", "The Moon"],
                    "optionsAr": ["التروبوسفير", "الفضاء الخارجي", "القمر"],
                    "correct": 0
                }
            }
        ]
    },
    {
        "id": "journey_center",
        "titleEn": "Journey to the Center of the Earth",
        "titleAr": "رحلة استكشافية إلى مركز الأرض",
        "targetAge": "7-13",
        "character": "Professor Geo & Rocky the Drill",
        "coverImage": "/textures/earth_nasa_night.jpg",
        "chapters": [
            {
                "chapterNumber": 1,
                "titleEn": "Diving Beneath the Crust",
                "titleAr": "الغوص تحت القشرة الصلبة",
                "textEn": "If we could drill deep beneath the ground, past the soil and rocks of the crust, we would reach the gigantic mantle, where super-hot rocks move slowly like honey over millions of years!",
                "textAr": "لو استطعنا الحفر عميقاً تحت أقدامنا لما وراء صخور القشرة الأرضية، لوصلنا إلى الوشاح العملاق، حيث تتحرك الصخور شديدة السخونة ببطء شديد كالعسل المنساب عبر ملايين السنين!",
                "interactiveQuestion": {
                    "qEn": "What is the very center of Earth made of?",
                    "qAr": "مما يتكون مركز ولب الأرض الداخلي في أعمق نقطة؟",
                    "optionsEn": ["Solid iron and nickel", "Water ice", "Hollow air"],
                    "optionsAr": ["حديد ونيكل صلب فائق الكثافة", "جليد مائي", "هواء فارغ"],
                    "correct": 0
                }
            }
        ]
    }
]
