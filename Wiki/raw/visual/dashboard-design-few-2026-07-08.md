---
title: "Information Dashboard Design: Displaying Data for At-a-Glance Monitoring"
author: "Stephen Few"
year: "2013"
pages: "166"
source: "public.magendanz.com"
tags: [visual-design,data-visualization,dashboard,perception]
sha256: "d4cb0d9d595f5d6f"
ingested: "2026-07-08"
kind: "visual-art"
---

www.it-ebooks.info

Information Dashboard Design 
By Stephen Few  
...............................................  
Publisher: O'Reilly 
Pub Date: January 2006 
ISBN: 0‐596‐10016‐7 
Pages: 223 
  
 
www.it-ebooks.info

Copyright 
Copyright © 2006 Stephen Few All rights reserved. 
Printed in Italy. 
Published by O'Reilly Media, Inc. 1005 Gravenstein Highway North Sebastopol, CA 95472 
O'Reilly books may be purchased for educational, business, or sales promotional use. Online editions are 
also available for most titles (safari.oreilly.com). For more information, contact our corporate/institutional 
sales department: 800‐998‐9938 or corporate@oreilly.com. 
Editor 
Colleen Wheeler 
Production Editor 
Genevieve d'Entremont 
Art Director 
Mike Kohnke 
Cover Designer 
Stephen Few 
Interior Designers 
Mike Kohnke, Terri Driscoll 
Production Services 
Specialized Composition, Inc. 
Print History 
  
January 2006: 
First Edition. 
 
The O'Reilly logo is a registered trademark of O'Reilly Media, Inc. Information Dashboard Design and 
related trade dress are trademarks of O'Reilly Media, Inc. 
Many of the designations used by manufacturers and sellers to distinguish their products are claimed as 
trademarks. Where those designations appear in this book, and O'Reilly Media, Inc. was aware of a 
trademark claim, the designations have been printed in caps or initial caps. 
While every precaution has been taken in the preparation of this book, the publisher and author assume no 
responsibility for errors or omissions, or for damages resulting from the use of the information contained 
herein. 
0‐596‐10016‐7 
  
 
www.it-ebooks.info

To my parents, Bob and Joyce Few, whose pride in my journeyhowever strange that journey must have 
sometimes seemedinstilled deep down into my bones the resolve to keep placing one foot in front of the 
other. 
 
 
www.it-ebooks.info

About the Author 
Stephen Few has over 20 years of experience as an IT innovator, consultant, and educator. Today, as 
Principal of the consultancy Perceptual Edge, Stephen focuses on data visualization for analyzing and 
communicating quantitative business information. He is working to raise consciousness and to provide a 
treatment plan that addresses the needs of business in the language of business. His previous book, Show 
Me the Numbers: Designing Tables and Graphs to Enlighten, is a powerful fitness program designed to 
target the data presentation aspects of this problem. 
Today, from his office in Berkeley, California, Stephen provides consulting and training services, speaks 
frequently at conferences, and teaches in the MBA program at the University of California in Berkeley. 
More about his current work can be found at www.perceptualedge.com. 
 
 
www.it-ebooks.info

Introduction 
Few phenomena characterize our time more uniquely and powerfully than the rapid rise and influence of 
information technologies. These technologies have unleashed a tsunami of data that rolls over and flattens 
us in its wake. Taming this beast has become a primary goal of the information industry. One tool that has 
emerged from this effort in recent years is the information dashboard. This single‐screen display of the 
most important information people need to do a job, presented in a way that allows them to monitor 
what's going on in an instant, is a powerful new medium of communication. At least it can be, but only 
when properly designed. 
Most information dashboards that are used in business today fall far short of their potential. The root of 
the problem is not technologyat least not primarilybut poor visual design. To serve their purpose and fulfill 
their potential, dashboards must display a dense array of information in a small amount of space in a 
manner that communicates clearly and immediately. This requires design that taps into and leverages the 
power of visual perception to sense and process large chunks of information rapidly. This can be achieved 
only when the visual design of dashboards is central to the development process and is informed by a solid 
understanding of visual perceptionwhat works, what doesn't, and why. 
No technology can do this for you. You must bring this expertise to the process. Take heartthe visual design 
skills that you need to develop effective dashboards can be learned, and helping you learn them is the sole 
purpose of this book. 
If the information is important, it deserves to be communicated well. 
 
 
www.it-ebooks.info

Acknowledgments 
Without a doubt I owe the greatest debt of gratitude to the many software vendors who have done so 
much to make this book necessary by failing to address or even contemplate the visual design needs of 
dashboards. Their kind disregard for visual design has given me focus, ignited my passion, and guaranteed 
my livelihood for years to come. 
Now, on to those who have contributed more directly and personally to this effort. As a man, I will never be 
able to create, shelter, and nourish an emerging life within this body of mine. In recent years, however, I 
have recognized and pursued the opportunity to breathe life into the products of my imagination and pass 
them on to the world in the form of books. Writing a book is a bit like bearing a child. Working with a 
publisher to help the child learn to walk before venturing into the world is a lesson in trust. The folks at 
O'Reilly Media have taught me to entrust to thembeginning with unspeakable angst, but proceeding 
through unfaltering steps toward ever‐increasing comfortthe collegial care of this beloved child. Many at 
O'Reilly have contributed so much, but two in particular have stood by my side from the beginning with 
soothing voices of confidence and calm. My editor, Colleen Wheeler, knew when to listen in silence, when 
to tease me out of myopia, and when to gently remind me that I was in her considerate and considerable 
care. My acquisitions editor, Steve Weiss, sought me out and wooed me through months of thoughtful 
discussion into the O'Reilly fold. He gave assurances and has made sure that they were fulfilled. 
 
 
www.it-ebooks.info

Sommario 
Copyright ....................................................................................................................................................... 3 
About the Author ........................................................................................................................................... 5 
Introduction ................................................................................................................................................... 6 
Acknowledgments ......................................................................................................................................... 7 
Chapter 1. Clarifying the Vision ....................................................................................................................... 11 
1.1. All That Glitters Is Not Gold .................................................................................................................. 12 
1.2. Even Dashboards Have a History .......................................................................................................... 14 
1.3. Dispelling the Confusion ....................................................................................................................... 15 
1.3.1. What Is a Dashboard?........................................................................................................................ 26 
1.4. A Timely Opportunity ........................................................................................................................... 28 
Chapter 2. Variations in Dashboard Uses and Data ........................................................................................ 29 
2.1. Categorizing Dashboards ...................................................................................................................... 30 
2.1.1. Classifying Dashboards by Role ..................................................................................................... 31 
2.2. Typical Dashboard Data ........................................................................................................................ 33 
2.2.1. The Common Thread in Dashboard Diversity................................................................................ 33 
Chapter 3. Thirteen Common Mistakes in Dashboard Design ........................................................................ 38 
3.1. Exceeding the Boundaries of a Single Screen ....................................................................................... 39 
3.1.1. Fragmenting Data into Separate Screens ...................................................................................... 40 
3.1.2. Requiring Scrolling ......................................................................................................................... 42 
3.2. Supplying Inadequate Context for the Data ......................................................................................... 43 
3.3. Displaying Excessive Detail or Precision ............................................................................................... 45 
3.4. Choosing a Deficient Measure .............................................................................................................. 46 
3.5. Choosing Inappropriate Display Media ................................................................................................ 47 
3.6. Introducing Meaningless Variety .......................................................................................................... 51 
3.7. Using Poorly Designed Display Media .................................................................................................. 52 
3.8. Encoding Quantitative Data Inaccurately ............................................................................................. 56 
3.9. Arranging the Data Poorly .................................................................................................................... 56 
3.10. Highlighting Important Data Ineffectively or Not at All ..................................................................... 57 
3.11. Cluttering the Display with Useless Decoration ................................................................................. 58 
3.12. Misusing or Overusing Color .............................................................................................................. 61 
3.13. Designing an Unattractive Visual Display ........................................................................................... 62 
Chapter 4. Tapping into the Power of Visual Perception ................................................................................ 64 
4.1. Understanding the Limits of Short‐Term Memory ............................................................................... 65 
4.2. Visually Encoding Data for Rapid Perception ....................................................................................... 67 
www.it-ebooks.info

4.2.1. Attributes of Color ......................................................................................................................... 69 
4.2.2. Attributes of Form ......................................................................................................................... 70 
4.2.3. Attributes of Position .................................................................................................................... 71 
4.2.4. Attributes of Motion ...................................................................................................................... 71 
4.2.5. Encoding Quantitative Versus Categorical Data ............................................................................ 71 
4.2.6. Limits to Perceptual Distinctness .................................................................................................. 73 
4.2.7. Using Vivid and Subtle Colors Appropriately ................................................................................. 74 
4.3. Gestalt Principles of Visual Perception ................................................................................................. 74 
4.3.1. The Principle of Proximity ............................................................................................................. 75 
4.3.2. The Principle of Similarity .............................................................................................................. 75 
4.3.3. The Principle of Enclosure ............................................................................................................. 76 
4.3.4. The Principle of Closure ................................................................................................................. 77 
4.3.5. The Principle of Continuity ............................................................................................................ 78 
4.3.6. The Principle of Connection .......................................................................................................... 78 
4.4. Applying the Principles of Visual Perception to Dashboard Design ..................................................... 79 
Chapter 5. Eloquence Through Simplicity ....................................................................................................... 80 
5.1. Characteristics of a Well‐Designed Dashboard .................................................................................... 81 
5.1.1. Condensing Information via Summarization and Exception ......................................................... 82 
5.2. Key Goals in the Visual Design Process ................................................................................................ 83 
5.2.1. Reduce the Non‐Data Pixels .......................................................................................................... 86 
5.2.2. Enhance the Data Pixels ................................................................................................................ 94 
Chapter 6. Effective Dashboard Display Media ............................................................................................. 101 
6.1. Select the Best Display Medium ......................................................................................................... 102 
6.2. An Ideal Library of Dashboard Display Media .................................................................................... 106 
6.2.1. Graphs ......................................................................................................................................... 107 
6.2.2. Icons ............................................................................................................................................. 131 
6.2.3. Text .............................................................................................................................................. 133 
6.2.4. Images ......................................................................................................................................... 133 
6.2.5. Drawing Objects .......................................................................................................................... 134 
6.2.6. Organizers .................................................................................................................................... 135 
6.3. Summary ............................................................................................................................................. 137 
Chapter 7. Designing Dashboards for Usability ............................................................................................. 138 
7.1. Organize the Information to Support Its Meaning and Use ............................................................... 139 
7.1.1. Organize Groups According to Business Functions, Entities, and Use ........................................ 139 
7.1.2. Co‐locate Items That Belong to the Same Group ........................................................................ 139 
www.it-ebooks.info

7.1.3. Delineate Groups Using the Least Visible Means ........................................................................ 140 
7.1.4. Support Meaningful Comparisons ............................................................................................... 141 
7.1.5. Discourage Meaningless Comparisons ........................................................................................ 142 
7.2. Maintain Consistency for Quick and Accurate Interpretation ........................................................... 143 
7.3. Make the Viewing Experience Aesthetically Pleasing ........................................................................ 143 
7.3.1. Choose Colors Appropriately ....................................................................................................... 144 
7.3.2. Choose High Resolution for Clarity .............................................................................................. 145 
7.3.3. Choose the Right Text .................................................................................................................. 145 
7.4. Design for Use as a Launch Pad .......................................................................................................... 145 
7.5. Test Your Design for Usability............................................................................................................. 146 
Chapter 8. Putting It All Together .................................................................................................................. 147 
8.1. Sample Sales Dashboard..................................................................................................................... 148 
Critique of Sales Dashboard Example 1 ................................................................................................. 151 
Critique of Sales Dashboard Example 2 ................................................................................................. 152 
Critique of Sales Dashboard Example 3 ................................................................................................. 153 
Critique of Sales Dashboard Example 4 ................................................................................................. 154 
Critique of Sales Dashboard Example 5 ................................................................................................. 155 
Critique of Sales Dashboard Example 6 ................................................................................................. 156 
Critique of Sales Dashboard Example 7 ................................................................................................. 157 
Critique of Sales Dashboard Example 8 ................................................................................................. 158 
8.2. Sample CIO Dashboard ....................................................................................................................... 159 
8.3. Sample Telesales Dashboard .............................................................................................................. 161 
8.4. Sample Marketing Analysis Dashboard .............................................................................................. 162 
8.5. A Final Word ....................................................................................................................................... 164 
Appendix A. Recommended Reading ............................................................................................................ 165 
Colophon ....................................................................................................................................................... 166 
 
 
 
 
www.it-ebooks.info

Chapter 1. Clarifying the Vision 
Dashboards offer a unique and powerful solution to an organization's need for information, but they usually 
fall far short of their potential. Dashboards must be seen in historical context to understand and appreciate 
how and why they've come about, why they've become so popular, and whydespite many problems that 
undermine their value todaythey offer benfits worth pursuing. To date, little serious attention has been 
given to their visual design. This book strives to fill this gap. However, confusion abounds, demanding a 
clear definition of dashboards before we can explore the visual design principles and practices that must be 
applied if they are to live up to their unique promise. 
 
 
www.it-ebooks.info

 
Problems with dashboards today  
Dashboards in historical context  
Current confusion about what dashboards are  
A working definition of "dashboard"  
A timely opportunity for dashboards 
Above all else, this is a book about communication. It focuses exclusively on a particular medium of 
communication called a dashboard. In the fast‐paced world of information technology (IT), terms are 
constantly changing. Just when you think you've wrapped your mind around the latest innovation, the 
technology landscape shifts beneath you and you must struggle to remain upright. This is certainly true of 
dashboards. 
Live your life on the surface of these shifting sands, and you'll never get your balance. Look a little deeper, 
however, and you'll discover more stable ground: a bedrock of objectives, principles, and practices for 
information handling that remains relatively constant. Dashboards are unique in several exciting and useful 
ways, but despite the hype surrounding them, what they are and how they work as a means of delivering 
information are closely related to some long‐familiar concepts and technologies. It's time to cut through 
the hype and learn the practical skills that can help you transform dashboards from yet another fad riding 
the waves of the technology buzz into the effective means to enlighten that they really can be. 
Today, everybody wants a dashboard. Like many newcomers to the technology scene, dashboards are sexy. 
Software vendors work hard to make their dashboards shimmy with sex appeal. They taunt, "You don't 
want to be the only company in your neighborhood without one, do you?" 
They warn, "You can no longer live without one." They whisper sweetly, "Still haven't achieved the 
expected return on investment (ROI) from your expensive data warehouse? Just stick a dashboard in front 
of it and watch the money pour in." Be still my heart. 
Those gauges, meters, and traffic lights are so damn flashy! You can imagine that you're sitting behind the 
wheel of a German‐engineered sports car, feeling the wind whip through your hair as you tear around 
curves on the autobahn at high speeds, all without leaving your desk. 
Everyone wants a dashboard today, but often for the wrong reasons. Rest assured, however, that 
somewhere beyond the hype and sizzle lives a unique and effective solution to familiar business problems 
that are rooted in a very real need for information. That's the dashboard that deserves to live on your 
screen. 
1.1. All That Glitters Is Not Gold 
Dashboards can provide a unique and powerful means to present information, but they rarely live up to 
their potential. Most dashboards fail to communicate efficiently and effectively, not because of inadequate 
technology (at least not primarily), but because of poorly designed implementations. No matter how great 
the technology, a dashboard's success as a medium of communication is a product of design, a result of a 
display that speaks clearly and immediately. Dashboards can tap into the tremendous power of visual 
perception to communicate, but only if those who implement them understand visual perception and apply 
www.it-ebooks.info

that understanding through design principles and practices that are aligned with the way people see and 
think. Software won't do this for you. It's up to you. 
Unfortunately, most vendors that provide dashboard software have done little to encourage the effective 
use of this medium. They focus their marketing efforts on flash and dazzle that subvert the goals of clear 
communication. They fight to win our interest by maximizing sizzle, highlighting flashy display mechanisms 
that appeal to our desire to be entertained. Once implemented, however, these cute displays lose their 
spark in a matter of days and become just plain annoying. An effective dashboard is the product not of cute 
gauges, meters, and traffic lights (Figure 1‐1), but rather of informed design: more science than art, more 
simplicity than dazzle. It is, above all else, about communication. 
 
Figure 1‐1. A typical flashy dashboard. Can't you just feel the engine revving? 
This failure by software vendors to focus on what we actually need is hardly unique to dashboards. Most 
software suffers from the same shortcomingdespite all the hype about user‐friendliness, it is difficult to 
use. This sad state is so common, and has been the case for so long, we've grown accustomed to the pain. 
On those occasions when this ugly truth breeches the surface of our consciousness, we usually blame the 
problem on ourselves rather than the software, framing it in terms of "computer illiteracy." If we could only 
adapt more to the computer and how it works, there wouldn't be a problemor so we reason. In his 
insightful book entitled The Inmates Are Running the Asylum, master designer Alan Cooper writes: 
The sad thing about dancing bearware [Cooper's term for poorly designed software 
that is difficult to use] is that most people are quite satisfied with the lumbering 
beast. Only when they see some real dancing do they begin to suspect that there is a 
world beyond ursine shuffling. So few software‐based products have exhibited any 
www.it-ebooks.info

real dancing ability that most people are honestly unaware that things could be 
bettera lot better.1 
Cooper argues that this failure is rooted in an approach to software development that simply doesn't work. 
In a genuine attempt to please their customers, software engineers focus on checking all the items, one by 
one, off of lists of requested features. This approach makes sense to technology‐oriented software 
engineers, but it results in lumbering beasts. Customers are expert in knowing what they need to 
accomplish, but not in knowing how software ought to be designed to support their needs. Allowing 
customers to design software through feature requests is the worst form of disaster by committee. 
Software vendors should bring design vision and expertise to the development process. They ought to 
know the difference between superficial glitz and what really works. But they're so exhausted from working 
ungodly hours trying to squeeze more features into the next release that they're left with no time to do the 
research needed to discover what actually works, or even to step back and observe how their products are 
really being used (and failing in the process). 
The part of information technology that focuses on reporting and analysis currently goes by the name 
business intelligence (BI). To date, BI vendors have concentrated on developing the underlying technologies 
that are used to gather data from source systems, transform data into a more usable form, store data in 
high‐performance databases, access data for use, and present data in the form of reports. Tremendous 
progress has been made in these areas, resulting in robust technologies that can handle huge repositories 
of data. However, while we have managed to warehouse a great deal of information, we have made little 
progress in using that information effectively. Relatively little effort has been dedicated to engaging human 
intelligence, which is what this industry, by definition, is supposed to be about. 
A glossary on the Gartner Group's web site defines business intelligence as "An interactive process for 
exploring and analyzing structured, domain‐specific information… to discern business trends or patterns, 
thereby deriving insights and drawing conclusions" 
(http://www.gartner.com/6_help/glossary/GlossaryB.jsp). To progress in this worthwhile venture, the BI 
industry must shift its focus now to an engaging interaction with human perception and intelligence. To do 
this, vendors must base their efforts on a firm understanding of how people perceive and think, building 
interfaces, visual displays, and methods of interaction that fit seamlessly with human ability. 
1.2. Even Dashboards Have a History 
In many respects, "dashboard" is simply a new name for the Executive Information Systems (EISs) first 
developed in the 1980s. These implementations remained exclusively in the offices of executives and never 
numbered more than a few, so it is unlikely that you've ever actually seen one. I sat through a few vendor 
demos back in the 1980s but never did see an actual system in use. The usual purpose of an EIS was to 
display a handful of key financial measures through a simple interface that "even an executive could 
understand." Though limited in scope, the goal was visionary and worthwhile, but ahead of its time. Back 
then, before data warehousing and business intelligence had evolved the necessary data‐handling 
methodologies and given shape to the necessary technologies, the vision simply wasn't practical; it couldn't 
be realized because the required information was incomplete, unreliable, and spread across too many 
disparate sources. Thus, in the same decade that the EIS arose, it also went into hibernation, preserving its 
vision in the shadows until the time was ripe… That is, until now. 
                                                           
1The Inmates Are Running the Asylum (Indianapolis, IN: SAMS Publishing, 1999), 59. 
www.it-ebooks.info

During the 1990s, data warehousing, online analytical processing (OLAP), and eventually business 
intelligence worked as partners to tame the wild onslaught of the information age. The emphasis during 
those years was on collecting, correcting, integrating, storing, and accessing information in ways that 
sought to guarantee its accuracy, timeliness, and usefulness. From the early days of data warehousing on 
into the early years of this new millennium, the effort has largely focused on the technologies, and to a 
lesser degree the methodologies, needed to make information available and useful. The direct beneficiaries 
so far have mostly been folks who are highly proficient in the use of computers and able to use the 
available tools to navigate through large, often complex databases. 
What also emerged in the early 1990s, but didn't become popular until late in that decade, was a new 
approach to management that involved the identification and use of key performance indicators (KPIs), 
introduced by Robert S. Kaplan and David P. Norton as the Balanced Scorecard. The advances in data 
warehousing and its technology partners set the stage for this new interest in management through the use 
of metricsand not just financial metricsthat still dominates the business landscape today. Business 
Performance Management (BPM), as it is now commonly known, has become an international 
preoccupation. The infrastructure built by data warehousing and the like, as well as the interest of BPM in 
metrics that can be monitored easily, together tilled and fertilized the soil in which the hibernating seeds of 
EIS‐type displays were once again able to grow. 
What really caused heads to turn in recognition of dashboards as much more than your everyday fledgling 
technology, however, was the Enron scandal in 2001. The aftermath put new pressure on corporations to 
demonstrate their ability to closely monitor what was going on in their midst and to thereby assure 
shareholders that they were in control. This increased accountability, combined with the concurrent 
economic downturn, sent Chief Information Officers (CIOs) on a mission to find anything that could help 
managers at all levels more easily and efficiently keep an eye on performance. Most BI vendors that hadn't 
already started offering a dashboard product soon began to do so, sometimes by cleverly changing the 
name of an existing product, sometimes by quickly purchasing the rights to an existing product from a 
smaller vendor, and sometimes by cobbling together pieces of products that already existed. The 
marketplace soon offered a vast array of dashboard software from which to choose. 
1.3. Dispelling the Confusion 
Like many products that hit the high‐tech scene with a splash, dashboards are veiled in marketing hype. 
Virtually every vendor in the BI space claims to sell dashboard software, but few clarify what dashboards 
actually are. I'm reminded of the early years of data warehousing, wheneager to learn about this new 
approach to data managementI asked my IBM account manager how IBM defined the term. His response 
was classic and refreshingly candid: "By data warehousing we at IBM mean whatever the customer thinks it 
means." I realize that this wasn't IBM's official definition, which I'm sure existed somewhere in their 
literature, but it was my blue‐suited friend's way of saying that as a salesperson, it was useful to leave the 
term vague and flexible. As long as a product or service remains undefined or loosely defined, it is easy to 
claim that your company sells it. 
Those rare software vendors that have taken the time to define the term in their marketing literature start 
with the specific features of their products as the core of the definition, rather than a generic description. 
As a result, vendor definitions tend to be self‐validating lists of technologies and features. For example, Dr. 
Gregory L. Hovis, Director of Product Deployment for Snippets Software, Inc., asserts: 
www.it-ebooks.info

Able to universally connect to any XML or HTML data source, robust dashboard 
products intelligently gather and display data, providing business intelligence 
without interrupting work flow… An enterprise dashboard is characterized by a 
collection of intelligent agents (or gauges), each performing frequent bidirectional 
communication with data sources. Like a virtual staff of 24x7 analysts, each agent in 
the dashboard intelligently gathers, processes and presents data, generating alerts 
and revising actions as conditions change.1 
An article in the June 16, 2003 edition of Computerworld cites statistics from a study done by AMR 
Research, Inc., which declares that "more than half of the 135 companies… recently surveyed are 
implementing dashboards."2 
Unfortunately, the author never tells us what dashboards are. He teases us with hints, stating that 
dashboards and scorecards are BI tools that "have found a new home in the cubicles," having moved from 
where they once resided (exclusively in executive suites) under the name Executive Information Systems. 
He gives examples of how dashboards are being used and speaks of their benefits, but leaves it to us to 
piece together a sense of what they are. The closest he comes to a definition is when he quotes John 
Hagerty of AMR Research, Inc.: "Dashboards and scorecards are about measuring." 
While conducting an extensive literature review in 2003 in search of a good working definition, I visited 
DataWarehousingOnline.com and clicked on the link to "Executive Dashboard" articles. In response, I 
received the same 18 web pages of links that I found when I separately clicked on links for "Balanced 
Scorecard," "Data Quality and Integration," and "Data Mining." Either the links weren't working properly, or 
this web portal for the data warehousing industry at the time believed that these terms all meant the same 
thing.3 
I finally decided to begin the task of devising a working definition of my own by examining every example of 
a dashboard I could find on the Web, in search of their common characteristics. You might find it 
interesting to take a similar journey. In the next few pages, you'll see screenshots of an assortment of 
dashboards, which were mostly found on the web sites of vendors that sell dashboard software. Take the 
time now to browse through these examples and see if you can discern common threads that might be 
woven into a useful definition. 
                                                           
1 Gregory L. Hovis, "Stop Searching for InformationMonitor it with Dashboard Technology," DM Direct, February 2002. 
2 Mark Leon, "Dashboard Democracy," Computerworld, June 16, 2003 
3 By including these examples from the web sites of software vendors and a few other sources, I do not mean to 
endorse any of these dashboards or the software products used to create them as examples of good design, nor as 
extraordinary examples of poor design. To varying degrees they all exhibit visual design problems that I'll address in 
later chapters. 
www.it-ebooks.info

 
Figure 1‐2. This dashboard from Business Objects relies primarily on graphical means to display a series of performance 
measures. along with a list of alerts, Notice that the title of this dashboard is "My KPIs." Key performance indicators and 
dashboards appear to be synonymous in the minds of most vendors. Notice the gauges as well. We'll see quite a few of them. 
 
www.it-ebooks.info

Figure 1‐3. This dashboard from Oracle Corporation displays a collection of sales measures for analyzing product performance by 
category. All of the measures are displayed graphically. We'll find that this emphasis on graphical display media is fairly 
common. 
 
Figure 1‐4. This dashboard from Informatica Corporation displays measures of revenue by sales channel along with a list of 
reports that can be viewed separately. The predominance of graphical display media that we observed on the previous 
dashboards appears on this one as well, notably in the form of meters designed to look like speedometers. The list of reports 
adds portal functionality, enabling this dashboard to operate as a launch pad to complementary information. 
www.it-ebooks.info

 
Figure 1‐5. This dashboard from Principa provides an overview of a company's financial performance compared to targets for the 
month of March, both in tabular form and as a series of gauges. The information can be tailored by selecting different months 
and amounts of history. Once again, we see a strong expression of the dashboard metaphor, this time in the form of graphical 
devices that were designed to look like fuel gauges. 
www.it-ebooks.info

 
Figure 1‐6. This dashboard from Cognos, Inc. displays a table and five graphsone in the form of a world mapto communicate 
sales information. Despite the one table, there's a continued emphasis on graphical media. Notice also that a theme regarding 
the visual nature and need for visual appeal of dashboards is emerging in these examples. 
www.it-ebooks.info

 
Figure 1‐7. This dashboard from Hyperion Solutions Corporation displays regional sales revenue in three forms: on a map, in a 
bar graph, and in a table. Data can be filtered by means of three sets of radio buttons on the left. These filtering mechanisms 
build rudimentary analytical functionality into this dashboard. Visual decoration reinforces the theme that dashboards 
intentionally strive for visual appeal. 
www.it-ebooks.info

 
Figure 1‐8. This dashboard from Corda Technologies, Inc. features flight‐loading measures for an airline using four panels of 
graphs. Here again we see an attention to the visual appeal of the display. Notice also in the instructions at the top that an 
ability to interact with the graphs has been built into the dashboard, so that users can access additional information in pop‐ups 
and drill into greater levels of detail. 
www.it-ebooks.info

 
Figure 1‐9. This dashboard from Visual Mining, Inc. displays various measures of a city's transit system to give the executives in 
charge a quick overview of the system's current and historical performance. Use of the colors green, yellow, and red to indicate 
good, satisfactory, and bad performance, as you can see on the three graphical displays arranged horizontally across the middle, 
is common on dashboards. 
 
www.it-ebooks.info

Figure 1‐10. This dashboard from Infommersion, Inc. gives executives of a hotel chain the means to view multiple measures of 
performance, one hotel at a time. It is not unusual for dashboards to divide the full set of data into individual views, as this one 
does by using the listbox in the upper‐left corner to enable viewers to select an individual hotel by location. The great care that 
we see in this example to realistically reproduce the dashboard metaphor, even down to the sheen on polished metal, is an 
effort that many vendors take quite seriously. 
 
Figure 1‐11. This dashboard from Celequest Corporation integrates a series of related tables and graphs that allow executives to 
view several aspects of sales simultaneously. It exhibits an effort to combine a rich set of related data on the screen to provide a 
comprehensive overview of a company's sales performance. 
www.it-ebooks.info

 
Figure 1‐12. This dashboard from General Electric, called a "digital cockpit," provides a tabular summary of performance, 
complemented by a color‐coded indicator light for each measure's status. Rather than a dashboard designed by a software 
vendor to exhibit its product, this is an actual working dashboard that was designed by a company to serve its own business 
needs. In this example, no effort was made to literally represent the dashboard (or cockpit) metaphor. 
 
www.it-ebooks.info

Figure 1‐13. This dashboard is used by the Treasury Board of Canada to monitor the performance of a project. Here again we 
have a dashboard that was designed by an organization for its own use. This time, the dashboard metaphor makes a token 
appearance in the form of gauges. The traffic‐light colors green, yellow, and redhere with the addition of blue for the 
exceptionally good status of "ahead of schedule"are also used. Unlike some of the examples that we've seen that displayed 
relatively little information, this one makes the attempt to provide the comprehensive overview that would be needed to 
effectively monitor progress and performance. 
1.3.1. What Is a Dashboard? 
As you have no doubt determined by examining these examples, there's a fair degree of diversity in the 
products that go by the name "dashboard." One of the few characteristics that most vendors seem to agree 
on is that for something to be called a dashboard it must include graphical display mechanisms such as 
traffic lights and a variety of gauges and meters, many similar to the fuel gauges and speedometers found 
in automobiles. This clearly associates BI dashboards with the familiar versions found in cars, thereby 
leveraging a useful metaphorbut the metaphor alone doesn't provide an adequate definition. About the 
only other thread that is common to these dashboard examples is that they usually attempt to provide an 
overview of something that's currently going on in the business. 
After a great deal of research and thought, I composed a definition of my own that captures the essence of 
what I believe a dashboard is (clearly biased toward the characteristics of this medium that I find most 
useful and unique). To serve us well, this definition must clearly differentiate dashboards from other forms 
of data presentation, and it must emphasize those characteristics that effectively support the goal of 
communication. Here's my definition, which originally appeared in Intelligent Enterprise magazine: 
A dashboard is a visual display of the most important information needed to achieve 
one or more objectives; consolidated and arranged on a single screen so the 
information can be monitored at a glance.1 
Just as the dashboard of a car provides critical information needed to operate the vehicle at a glance, a BI 
dashboard serves a similar purpose, whether you're using it to make strategic decisions for a huge 
corporation, run the daily operations of a team, or perform tasks that involve no one but yourself. The 
means is a single‐screen display, and the purpose is to efficiently monitor the information needed to 
achieve one's objectives. 
Visual display of the most information needed to achieve one or more objectives 
which fits entirely on a single computer screen so it can be monitored at a glance 
Let's go over the salient points: 
Dashboards are visual displays. The information on a dashboard is presented visually, usually as a 
combination of text and graphics, but with an emphasis on graphics. Dashboards are highly graphical, not 
because it is cute, but because graphical presentation, handled expertly, can often communicate with 
greater efficiency and richer meaning than text alone. How can you best present the information so that 
human eyes can take it in quickly and human brains can easily extract the correct and most important 
meanings from it? To design dashboards effectively, you must understand something about visual 
perceptionwhat works, what doesn't, and why.  
 
Dashboards display the information needed to achieve specific objectives. To achieve even a 
single objective often requires access to a collection of information that is not otherwise related, 
                                                           
1 Stephen Few, "Dashboard Confusion," Intelligent Enterprise, March 20, 2004. 
www.it-ebooks.info

often coming from diverse sources related to various business functions. It isn't a specific type of 
information, but information of whatever type that is needed to do a job. It isn't just information 
that is needed by executives or even by managers; it can be information that is needed by anyone 
who has objectives to meet. The required information can be and often is a set of KPIs, but not 
necessarily, for other types of information might also be needed to do one's job.  
 
A dashboard fits on a single computer screen. The information must fit on a single screen, entirely 
available within the viewer's eye span so it can all be seen at once, at a glance. If you must scroll 
around to see all the information, it has transgressed the boundaries of a dashboard. If you must 
shift from screen to screen to see it all, you've made use of multiple dashboards. The object is to 
have the most important information readily and effortlessly available so you can quickly absorb 
what you need to know.  
 
Must the information be displayed in a web browser? That might be the best medium for most 
dashboards today, but it isn't the only acceptable medium, and it might not be the best medium 10 
years from now. Must the information be constantly refreshed in real time? Only if the objectives 
that it serves require real‐time information. If you are monitoring air traffic using a dashboard, you 
must immediately be informed when something is wrong. On the other hand, if you are making 
strategic decisions about how to boost sales, a snapshot of information as of last night, or perhaps 
even the end of last month, should work fine.  
 
Dashboards are used to monitor information at a glance. Despite the fact that information about 
almost anything can be appropriately displayed in a dashboard, there is at least one characteristic 
that describes almost all the information found in dashboards: it is abbreviated in the form of 
summaries or exceptions. This is because you cannot monitor at a glance all the details needed to 
achieve your objectives. A dashboard must be able to quickly point out that something deserves 
your attention and might require action. It needn't provide all the details necessary to take action, 
but if it doesn't, it ought to make it as easy and seamless as possible to get to that information. 
Getting there might involve shifting to a different display beyond the dashboard, using navigational 
methods such as drilling down. The dashboard does its primary job if it tells you with no more than 
a glance that you should act. It serves you superbly if it directly opens the door to any additional 
information that you need to take that action. 
That's the essence of the dashboard. Now let's add to this definition a couple more supporting attributes 
that help dashboards do their job effectively: 
 
Dashboards have small, concise, clear, and intuitive display mechanisms. Display mechanisms that 
clearly state their message without taking up much space are required, so that the entire collection 
of information will fit into the limited real estate of a single screen. If something that looks like a 
fuel gauge, traffic signal, or thermometer fits this requirement best for a particular piece of 
information, that's what you should use, but if something else works better, you should use that 
instead. Insisting on sexy displays similar to those found in a car when other mechanisms would 
work better is counterproductive.  
 
Dashboards are customized. The information on a dashboard must be tailored specifically to the 
requirements of a given person, group, or function; otherwise, it won't serve its purpose. 
A dashboard is a type of display, a form of presentation, not a specific type of information or technology. 
Keep this distinction clear, and you will be freed to focus on what really matters: designing dashboards to 
communicate. 
www.it-ebooks.info

1.4. A Timely Opportunity 
Several circumstances have recently combined to create a timely opportunity for dashboards to add value 
to the workplace, including technologies such as high‐resolution graphics, emphasis on performance 
management and metrics, and a growing recognition of visual perception as a powerful channel for 
inf