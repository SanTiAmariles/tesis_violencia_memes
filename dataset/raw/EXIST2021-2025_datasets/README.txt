README: EXIST Competitions Datasets

This package contains the datasets created for the EXIST (sEXism Identification in Social neTworks) competition series. In particular, each folder corresponds to a specific year of the competition, from "EXIST 2021" up to the latest "EXIST 2024". Each folder contains the respective datasets for that year's competition.

Dataset Folders
	1.	EXIST 2021: Contains the datasets used for the first iteration of the competition. More details can be found on the EXIST 2021 website: https://nlp.uned.es/exist2021/.
	2.	EXIST 2022: Contains the datasets used for the second iteration of the competition. More details can be found on the EXIST 2022 website: https://nlp.uned.es/exist2022/.
	3.	EXIST 2023: Contains the datasets used for the third iteration of the competition. More details can be found on the EXIST 2023 website: https://nlp.uned.es/exist2023/.
	4.	EXIST 2024: Contains the datasets used for the latest competition. More details can be found on the EXIST 2024 website: https://nlp.uned.es/exist2024/.
	5.	EXIST 2025: Contains the datasets used for the latest competition. More details can be found on the EXIST 2025 website: https://nlp.uned.es/exist2025/. (Note that the videos from the dataset are not included, but links to them are provided for download.)

Test Sets Availability
Starting from 2022, the test sets are not publicly released to avoid model contamination due to the increasing number of models continuously analyzing data from the web. Instead, the test sets from 2022 onwards will only be accessible via the official repository evaluation application, EvALL. You can access EvALL at the following link: https://evall.uned.es/. Up to date, the EvALL repository includes the EXIST 2025 test sets, which in practice includes to the 2023 and 2024 test sets due to the structure of the EXIST 2025 dataset.


Bibliographic References
Each competition has an overview paper describing the datasets and the results. Please cite the corresponding paper if you use the datasets:
	1.	EXIST 2021 Overview: 
		Rodríguez-Sánchez, F., Carrillo-de-Albornoz, J., Plaza, L., Gonzalo, J., Rosso, P., Comet, M., & Donoso, T. (2021). Overview of EXIST 2021: sEXism Identification in Social neTworks. Procesamiento Del Lenguaje Natural, 67, 195-207. Recuperado de http://journal.sepln.org/sepln/ojs/ojs/index.php/pln/article/view/6389
		
		@article{PLN6389,
			author = {Francisco Rodríguez-Sánchez y Jorge Carrillo-de-Albornoz y Laura Plaza y Julio Gonzalo y Paolo Rosso y Miriam Comet y Trinidad Donoso},
			title = {Overview of EXIST 2021: sEXism Identification in Social neTworks},
			journal = {Procesamiento del Lenguaje Natural},
			volume = {67},
			number = {0},
			year = {2021},
			issn = {1989-7553},
			url = {http://journal.sepln.org/sepln/ojs/ojs/index.php/pln/article/view/6389},
			pages = {195--207}
		}

	2.	EXIST 2022 Overview: 
		Rodríguez-Sánchez, F., Carrillo-de-Albornoz, J., Plaza, L., Mendieta-Aragón, A., Marco-Remón, G., Makeienko, M., Plaza, M., Gonzalo, J., Spina, D., & Rosso, P. (2022). Overview of EXIST 2022: sEXism Identification in Social neTworks. Procesamiento Del Lenguaje Natural, 69, 229-240. Recuperado de http://journal.sepln.org/sepln/ojs/ojs/index.php/pln/article/view/6443
		
		@article{PLN6443,
			author = {Francisco Rodríguez-Sánchez y Jorge Carrillo-de-Albornoz y Laura Plaza y Adrián Mendieta-Aragón y Guillermo Marco-Remón y Maryna Makeienko y María Plaza y Julio Gonzalo y Damiano Spina y Paolo Rosso},
			title = {Overview of EXIST 2022: sEXism Identification in Social neTworks},
			journal = {Procesamiento del Lenguaje Natural},
			volume = {69},
			number = {0},
			year = {2022},
			issn = {1989-7553},
			url = {http://journal.sepln.org/sepln/ojs/ojs/index.php/pln/article/view/6443},
			pages = {229--240}
		}
		
	3.	EXIST 2023 Overview:
		Laura Plaza, Jorge Carrillo-de-Albornoz, Roser Morante, Enrique Amigó, Julio Gonzalo, Damiano Spina, Paolo Rosso:
		Overview of EXIST 2023 - Learning with Disagreement for Sexism Identification and Characterization. CLEF 2023: 316-342.

			@inproceedings{DBLP:conf/clef/PlazaCMAGSR23,
			  author       = {Laura Plaza and
							  Jorge Carrillo{-}de{-}Albornoz and
							  Roser Morante and
							  Enrique Amig{\'{o}} and
							  Julio Gonzalo and
							  Damiano Spina and
							  Paolo Rosso},
			  editor       = {Avi Arampatzis and
							  Evangelos Kanoulas and
							  Theodora Tsikrika and
							  Stefanos Vrochidis and
							  Anastasia Giachanou and
							  Dan Li and
							  Mohammad Aliannejadi and
							  Michalis Vlachos and
							  Guglielmo Faggioli and
							  Nicola Ferro},
			  title        = {Overview of {EXIST} 2023 - Learning with Disagreement for Sexism Identification
							  and Characterization},
			  booktitle    = {Experimental {IR} Meets Multilinguality, Multimodality, and Interaction
							  - 14th International Conference of the {CLEF} Association, {CLEF}
							  2023, Thessaloniki, Greece, September 18-21, 2023, Proceedings},
			  series       = {Lecture Notes in Computer Science},
			  volume       = {14163},
			  pages        = {316--342},
			  publisher    = {Springer},
			  year         = {2023},
			  url          = {https://doi.org/10.1007/978-3-031-42448-9\_23},
			  doi          = {10.1007/978-3-031-42448-9\_23},
			  timestamp    = {Tue, 07 May 2024 20:08:33 +0200},
			  biburl       = {https://dblp.org/rec/conf/clef/PlazaCMAGSR23.bib},
			  bibsource    = {dblp computer science bibliography, https://dblp.org}
			}

	
	4.	EXIST 2024 Overview: 
		Laura Plaza, Jorge Carrillo-de-Albornoz, Víctor Ruiz, Alba Maeso, Berta Chulvi, Paolo Rosso, Enrique Amigó, Julio Gonzalo, Roser Morante, Damiano Spina:
		Overview of EXIST 2024 - Learning with Disagreement for Sexism Identification and Characterization in Tweets and Memes. CLEF (2) 2024: 93-117
		
			@inproceedings{DBLP:conf/clef/PlazaCRMCRAGMS24,
			  author       = {Laura Plaza and
							  Jorge Carrillo{-}de{-}Albornoz and
							  V{\'{\i}}ctor Ruiz and
							  Alba Maeso and
							  Berta Chulvi and
							  Paolo Rosso and
							  Enrique Amig{\'{o}} and
							  Julio Gonzalo and
							  Roser Morante and
							  Damiano Spina},
			  editor       = {Lorraine Goeuriot and
							  Philippe Mulhem and
							  Georges Qu{\'{e}}not and
							  Didier Schwab and
							  Giorgio Maria Di Nunzio and
							  Laure Soulier and
							  Petra Galusc{\'{a}}kov{\'{a}} and
							  Alba Garc{\'{\i}}a Seco de Herrera and
							  Guglielmo Faggioli and
							  Nicola Ferro},
			  title        = {Overview of {EXIST} 2024 - Learning with Disagreement for Sexism Identification
							  and Characterization in Tweets and Memes},
			  booktitle    = {Experimental {IR} Meets Multilinguality, Multimodality, and Interaction
							  - 15th International Conference of the {CLEF} Association, {CLEF}
							  2024, Grenoble, France, September 9-12, 2024, Proceedings, Part {II}},
			  series       = {Lecture Notes in Computer Science},
			  volume       = {14959},
			  pages        = {93--117},
			  publisher    = {Springer},
			  year         = {2024},
			  url          = {https://doi.org/10.1007/978-3-031-71908-0\_5},
			  doi          = {10.1007/978-3-031-71908-0\_5},
			  timestamp    = {Sun, 29 Sep 2024 21:17:18 +0200},
			  biburl       = {https://dblp.org/rec/conf/clef/PlazaCRMCRAGMS24.bib},
			  bibsource    = {dblp computer science bibliography, https://dblp.org}
			}
			
	5.	EXIST 2025 Overview: 
		Laura Plaza, Jorge Carrillo-de-Albornoz, Iván Árcos, Paolo Rosso, Damiano Spina, Enrique Amigó, Julio Gonzalo, Roser Morante:
		EXIST 2025: Learning with Disagreement for Sexism Identification and Characterization in Tweets, Memes, and TikTok Videos. ECIR (5) 2025: 442-449
		
			@inproceedings{DBLP:conf/clef/PlazaCARSAGM25,
			  author       = {Laura Plaza and
							  Jorge Carrillo{-}de{-}Albornoz and
							  Iv{\'{a}}n {\'{A}}rcos and
							  Paolo Rosso and
							  Damiano Spina and
							  Enrique Amig{\'{o}} and
							  Julio Gonzalo and
							  Roser Morante},
			  editor       = {Jorge Carrillo{-}de{-}Albornoz and
							  Alba Garc{\'{\i}}a Seco de Herrera and
							  Julio Gonzalo and
							  Laura Plaza and
							  Josiane Mothe and
							  Florina Piroi and
							  Paolo Rosso and
							  Damiano Spina and
							  Guglielmo Faggioli and
							  Nicola Ferro},
			  title        = {Overview of {EXIST} 2025: Learning with Disagreement for Sexism Identification
							  and Characterization in Tweets, Memes, and TikTok Videos},
			  booktitle    = {Experimental {IR} Meets Multilinguality, Multimodality, and Interaction
							  - 16th International Conference of the {CLEF} Association, {CLEF}
							  2025, Madrid, Spain, September 9-12, 2025, Proceedings},
			  series       = {Lecture Notes in Computer Science},
			  volume       = {16089},
			  pages        = {266--289},
			  publisher    = {Springer},
			  year         = {2025},
			  url          = {https://doi.org/10.1007/978-3-032-04354-2\_16},
			  doi          = {10.1007/978-3-032-04354-2\_16},
			  timestamp    = {Sat, 13 Sep 2025 16:55:52 +0200},
			  biburl       = {https://dblp.org/rec/conf/clef/PlazaCARSAGM25.bib},
			  bibsource    = {dblp computer science bibliography, https://dblp.org}
			}


Terms of Use
By using these datasets, you agree to the terms of use as accepted in the registration form. Sharing of the data is strictly prohibited. Any violation of these terms will result in the revocation of access to the datasets and potential legal consequences.

For any questions or clarifications, please refer to the competition's official website or contact the organizers.

