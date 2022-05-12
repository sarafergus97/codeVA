# The Lunar Myth 🌙
This project is an unplugged basic exploratory data analysis.
*#unplugged #data_cycle #data_science #disruption #null-results

## Classroom Highlights 
This exemplar demonstrates: 
1. Unplugged 🔌 Data Science
2. Finding no relationship
3. Data Tools like the [hedonometer](https://hedonometer.org/timeseries/en_all/?from=2020-11-01&to=2022-04-30)
4. A physical visualization
5. The opportunity for student generated questioning of outliers and of the size of data
6. Represetnations for categorical and numerical data.

This project attempts to address the aesthetic perspective of [communal meaning](http://www.animatingdemocracy.org/sites/default/files/pictures/AestPersp/pdfs/Aesthetics%20Short%20Take.pdf) by searching for patterns in human behavior that we all demonstrate.

## The Project

In this project, I looked into the [lunar effect](https://www.scientificamerican.com/article/lunacy-and-the-full-moon/), which is the idea that human behavior changes when the moon is full. A lot of poeple belive that this is the case. In fact, teachers in my own school often contribute outlandish student behavior with the full moon. So, over the course of about a month, I noted the phase of the moon, the percent illumination, and the "happiness" of New York Times headlines for the day. I measured happiness using the average [hedonometer](https://hedonometer.org/timeseries/en_all/?from=2020-11-01&to=2022-04-30) score for each word in the title. 

I created two visualizations. These two visualizations contrast numerical and categorical data by presenting what is essentially the same information in multiple ways. I created a comparative box-and-whisker relating numerical happiness to the categorical phase of the moon, and then a scatterplot relating the percent illumination of the moon and numerical happiness. 

My first, categorical representation was a physical box and whisker plot shows the spread of happiness in each phase of the moon. It appears that there is no substantial pattern. There was not a lot of data in general, but that was particularly true for full and new moons. This lack of data for an important measurement is something that I explored in the write-up. The most extreme spreads are in the categories with the least data. Prompting students to think about why that is can lead them to a stronger understanding of ideas like outliers and sample size.

*put image here*

The second visualization I created was a scatterplot showing the (lack of) relationship between illumination percent and happiness. Again, we can see that that the box-and-whisker was created for moon phase, a categorical variable, and a scatterplot was created for a continuous numerical variable, percent illumination. I labeled some major points (for example, *War in Ukraine* had a much lower happiness score than any other headlines) in the scatterplot to add a dimension to the data story. In the end, there appears to be no relationship.

*put image here*

In the write up, we conducted some follow-up research to answer the question of why so many people believe in the "lunar effect", even though we didn't find that it had any effect. 

## Teaching Notes

### A Null Result
Many students will choose to explore relationships that do not actually exist (sometimes, this will be painfully clear to you before your student even starts). This example helps to communicate to students that a weak realationships still provide insight and inquiry, and that they should not be afraid to investigate ideas they do not already know about. 

### Numerical or Categorical?
Students sometimes struggle with determining what visualizations to make based on the type of data that they have. Even more so, they struggle with the idea of cleaning data to allow fluidity in data type. For example, I had a student who was working with salary data and wanted to get an idea of what ranges of salaries are most common. She felt that a pie chart would help her in visualizing this. However, her data was numerical salaries. Together, we were able to group her data to allow her to explore categorical representations by adding a column for salary range which, based on the person's salary, could be categories like "40k - 60k" or "Under 20k". This allowed her to get a good understanding of what sorts of data are required for certain visualizations (She first tried a pie chart with the numerical data. It did not look so great.) and of ways that she can manipulate the data she has to answer different kinds of questions. 