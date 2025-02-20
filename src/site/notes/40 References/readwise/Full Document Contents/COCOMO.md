---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/cocomo/","tags":["rw/articles"]}
---

![rw-book-cover](https://en.wikipedia.org/static/apple-touch/wikipedia.png)

Not to be confused with [Kokomo](https://en.wikipedia.org/wiki/Kokomo_(disambiguation)).

The **Constructive Cost Model** (**COCOMO**) is a procedural [software cost estimation model](https://en.wikipedia.org/wiki/Estimation_in_software_engineering) developed by [Barry W. Boehm](https://en.wikipedia.org/wiki/Barry_Boehm). The model parameters are derived from fitting a [regression](https://en.wikipedia.org/wiki/Regression_analysis) formula using data from historical projects (63 projects for COCOMO 81 and 163 projects for COCOMO II).

#### History

The constructive cost model was developed by Barry W. Boehm in the late 1970s1(https://en.wikipedia.org/wiki/COCOMO#cite_note-1) and published in Boehm's 1981 book *Software Engineering Economics*2(https://en.wikipedia.org/wiki/COCOMO#cite_note-2) as a model for estimating effort, cost, and schedule for software projects. It drew on a study of 63 projects at [TRW](https://en.wikipedia.org/wiki/TRW_Inc.) Aerospace where Boehm was Director of Software Research and Technology. The study examined projects ranging in size from 2,000 to 100,000 [lines of code](https://en.wikipedia.org/wiki/Lines_of_code), and programming languages ranging from [assembly](https://en.wikipedia.org/wiki/Assembly_language) to [PL/I](https://en.wikipedia.org/wiki/PL/I). These projects were based on the [waterfall model](https://en.wikipedia.org/wiki/Waterfall_model) of software development which was the prevalent software development process in 1981.

References to this model typically call it *COCOMO 81*. In 1995 *COCOMO II* was developed and finally published in 2000 in the book *Software Cost Estimation with COCOMO II*.3(https://en.wikipedia.org/wiki/COCOMO#cite_note-cocomo2-3) COCOMO II is the successor of COCOMO 81 and is claimed to be better suited for estimating modern software development projects; providing support for more recent [software development processes](https://en.wikipedia.org/wiki/Software_development_process) and was tuned using a larger database of 161 projects. The need for the new model came as software development technology moved from mainframe and overnight batch processing to desktop development, code reusability, and the use of off-the-shelf software components.

COCOMO consists of a hierarchy of three increasingly detailed and accurate forms. The first level, *Basic COCOMO* is good for quick, early, rough order of magnitude estimates of software costs, but its accuracy is limited due to its lack of factors to account for difference in project attributes (*Cost Drivers*). *Intermediate COCOMO* takes these Cost Drivers into account and *Detailed COCOMO* additionally accounts for the influence of individual project phases. Last one is Complete COCOMO model which addresses the shortcomings of both basic & intermediate.

#### Intermediate COCOMOs

*Intermediate COCOMO* computes software development effort as function of program size and a set of "cost drivers" that include subjective assessment of product, hardware, personnel and project attributes. This extension considers a set of four "cost drivers", each with a number of subsidiary attributes:-

* Product attributes
	+ Required software reliability extent
	+ Size of application database
	+ Complexity of the product
* Hardware attributes
	+ Run-time performance constraints
	+ Memory constraints
	+ Volatility of the virtual machine environment
	+ Required turnabout time
* Personnel attributes
	+ Analyst capability
	+ Software engineering capability
	+ Applications experience
	+ Virtual machine experience
	+ Programming language experience
* Project attributes
	+ Use of software tools
	+ Application of software engineering methods
	+ Required development schedule

Each of the 15 attributes receives a rating on a six-point scale that ranges from "very low" to "extra high" (in importance or value). An effort multiplier from the table below applies to the rating. The product of all effort multipliers results in an *effort adjustment factor (EAF)*. Typical values for EAF range from 0.9 to 1.4.

| Cost Drivers  | Ratings  |
| --- | --- |
| Very Low  | Low  | Nominal  | High  | Very High  | Extra High  |
| Product attributes  |
| Required software reliability  | 0.75  | 0.88  | 1.00  | 1.15  | 1.40  |  |
| Size of application database  |  | 0.94  | 1.00  | 1.08  | 1.16  |  |
| Complexity of the product  | 0.70  | 0.85  | 1.00  | 1.15  | 1.30  | 1.65  |
| Hardware attributes  |
| Run-time performance constraints  |  |  | 1.00  | 1.11  | 1.30  | 1.66  |
| Memory constraints  |  |  | 1.00  | 1.06  | 1.21  | 1.56  |
| Volatility of the virtual machine environment  |  | 0.87  | 1.00  | 1.15  | 1.30  |  |
| Required turnabout time  |  | 0.87  | 1.00  | 1.07  | 1.15  |  |
| Personnel attributes  |
| Analyst capability  | 1.46  | 1.19  | 1.00  | 0.86  | 0.71  |  |
| Applications experience  | 1.29  | 1.13  | 1.00  | 0.91  | 0.82  |  |
| Software engineer capability  | 1.42  | 1.17  | 1.00  | 0.86  | 0.70  |  |
| Virtual machine experience  | 1.21  | 1.10  | 1.00  | 0.90  |  |  |
| Programming language experience  | 1.14  | 1.07  | 1.00  | 0.95  |  |  |
| Project attributes  |
| Application of software engineering methods  | 1.24  | 1.10  | 1.00  | 0.91  | 0.82  |  |
| Use of software tools  | 1.24  | 1.10  | 1.00  | 0.91  | 0.83  |  |
| Required development schedule  | 1.23  | 1.08  | 1.00  | 1.04  | 1.10  |  |

The Intermediate Cocomo formula now takes the form:

*E* = *a**i*(KLoC)*b**i*(EAF)where *E* is the effort applied in person-months, **KLoC** is the estimated number of thousands of delivered lines of code for the project, and **EAF** is the factor calculated above. The coefficient *ai* and the exponent *bi* are given in the next table.

| Software project  | ai | bi | ci |
| --- | --- | --- | --- |
| Organic  | 3.2  | 1.05  | 0.38  |
| Semi-detached  | 3.0  | 1.12  | 0.35  |
| Embedded  | 2.8  | 1.20  | 0.32  |

The Development time *D* and also the most effective number of Persons *P* calculation uses *E* in the same way as in the Basic COCOMO:

*D* = 2.5 *E**c**i* ![{\displaystyle P=E/D}](https://wikimedia.org/api/rest_v1/media/math/render/svg/3c805e20e1b1fccda12d193091b32a26f8970f94)Note that in addition to the EAF, the parameter *ai* is different in *Intermediate COCOMO* from the Basic model:

| Software project  | *ab* |
| --- | --- |
| Organic  | 2.4  |
| Semi-detached  | 3.0  |
| Embedded  | 3.6  |

The parameters *b* and *c* are the same in both models.

#### See also

* [Comparison of development estimation software](https://en.wikipedia.org/wiki/Comparison_of_development_estimation_software)
* [Cost overrun](https://en.wikipedia.org/wiki/Cost_overrun)
* [COSYSMO](https://en.wikipedia.org/wiki/Cosysmo)
* [Estimation in software engineering](https://en.wikipedia.org/wiki/Estimation_in_software_engineering)
* [Function point](https://en.wikipedia.org/wiki/Function_point)
* [Object point](https://en.wikipedia.org/wiki/Object_point)
* [Putnam model](https://en.wikipedia.org/wiki/Putnam_model)
* [SEER-SEM](https://en.wikipedia.org/wiki/SEER-SEM)
* [Software development effort estimation](https://en.wikipedia.org/wiki/Software_development_effort_estimation)
* [Software engineering economics](https://en.wikipedia.org/wiki/Software_engineering_economics)
* [PRICE Systems](https://en.wikipedia.org/wiki/PRICE_Systems)

#### References

1. **[^](https://en.wikipedia.org/wiki/COCOMO#cite_ref-1)** Stutzke, Richard. ["Software Estimating Technology: A Survey"](http://ece.arizona.edu/~ece473/readings/14-Software%20Estimating%20Technology.doc). Retrieved 9 Oct 2016.[![.docx icon.svg](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/.docx_icon.svg/17px-.docx_icon.svg.png)](https://en.wikipedia.org/wiki/DOC_(computing))[DOC](https://en.wikipedia.org/wiki/DOC_(computing))
2. **[^](https://en.wikipedia.org/wiki/COCOMO#cite_ref-2)** Boehm, Barry (1981). [*Software Engineering Economics*](https://archive.org/details/softwareengineer0000boeh). Prentice-Hall. [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier)) [0-13-822122-7](https://en.wikipedia.org/wiki/Special:BookSources/0-13-822122-7).
3. **[^](https://en.wikipedia.org/wiki/COCOMO#cite_ref-cocomo2_3-0)** [Barry Boehm](https://en.wikipedia.org/wiki/Barry_Boehm), Chris Abts, A. Winsor Brown, Sunita Chulani, Bradford K. Clark, Ellis Horowitz, Ray Madachy, Donald J. Reifer, and Bert Steece. *[Software Cost Estimation with COCOMO II](https://en.wikipedia.org/w/index.php?title=Software_Cost_Estimation_with_COCOMO_II_(book)&action=edit&redlink=1)* (with CD-ROM). Englewood Cliffs, NJ:Prentice-Hall, 2000. [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier)) [0-13-026692-2](https://en.wikipedia.org/wiki/Special:BookSources/0-13-026692-2)

#### Further reading

* Kemerer, Chris F. (May 1987). ["An Empirical Validation of Software Cost Estimation Models"](http://www.pitt.edu/~ckemerer/CK%20research%20papers/EmpiricalValidationSwCost_Kemerer87.pdf) (PDF). *Communications of the ACM*. **30** (5): 416–42. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1145/22899.22906](https://doi.org/10.1145%2F22899.22906).

#### External links

* [COCOMO 81 data](https://web.archive.org/web/20170902182304/http://openscience.us/repo/effort/cocomo/coc81.html) on tera-PROMISE
* [Analysis of the COCOMO 81 data](http://shape-of-code.coding-guidelines.com/2016/05/19/cocomo-how-not-to-fit-a-model-to-data/) obtains a different value for the Organic exponent.
