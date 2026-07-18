---
layout: post
mathjax: true
comments: true
title:  "Las Vegas: Historical Arc, Present Relevance, and Forward Projection"
date:   2026-01-30 00:00:00 +0000
categories: history economics urban
---

<!-- A249 -->
<script>console.log("A249");</script>

Las Vegas presents an economic natural experiment on the pricing of amenities. The analysis that follows is economic and business-model focused, and treats social conditions, crime, homelessness, and lived quality of life as outside its scope. The historical model treated rooms, food, and entertainment as loss leaders whose purpose was to bring gamblers into a house whose statistical edge on games generated the operating profit. The contemporary model treats those same amenities as profit centers priced at market rates or above, with gambling reduced to one revenue line among several. This article advances an unlearning hypothesis. Contemporary Strip operators have unlearned the historical loss-leader lesson that cheap amenities draw the visitor volume that lets gambling profit pay for everything, and have replaced that model with one in which each amenity carries its own positive margin. The two models optimize different objective functions, and the article develops the mathematical conditions under which each is preferred. The article traces the historical arc from the 1905 railroad watering stop through the mob-era Strip, the corporate megaresort transformation, and the current amenity-priced regime, assesses the city's regional, national, and global relevance as of the mid 2020s, and projects the load-bearing constraints that will shape the next twenty-five years.

## Prehistory and Founding

The Las Vegas valley served the Old Spanish Trail as a spring-fed campsite from the 1820s. Rafael Rivera's 1829 traverse identified the meadows that gave the site its Spanish name. Mormon missionaries established a mission and stockade in 1855, abandoning it by 1858 after conflict with local Southern Paiute bands and internal Mormon reassignment. The site's next economic function was as a Union Pacific Railroad watering stop on the Salt Lake to Los Angeles line, formally auctioned as a townsite on 15 May 1905 [Stanton 2020][ref_stanton_2020].

Nevada's 1859 Comstock Lode discovery had established the state's silver mining economy, but by 1900 the mining base was in decline. The state legislature legalized wide-open gambling on 19 March 1931 as a revenue measure amid the Great Depression, restoring what had been legal in some form from 1869 to 1909. The Hoover Dam construction from 1931 to 1936 brought thousands of workers to nearby Boulder City, and gambling houses in downtown Las Vegas captured their off-duty wages [Moehring 2000][book_moehring_2000] [Findlay 1986][book_findlay_1986]. The 1922 Colorado River Compact signed by seven basin state commissioners divided the river between an Upper Basin and a Lower Basin at 7.5 million acre-feet per year each [Colorado River Compact 1922][ref_colorado_compact_1922]. The Boulder Canyon Project Act of 1928 subsequently apportioned the Lower Basin share among California, Arizona, and Nevada, giving Nevada a 300000 acre-foot annual allocation whose apparent smallness in 1928 would become central to metropolitan growth constraints in the twenty-first century.

## Mob Era and the Invention of the Loss-Leader Casino

The Fremont Street casinos of the 1930s operated as sawdust-floor gambling halls without significant non-gaming amenities. The transformation began in 1941 when Thomas Hull opened El Rancho Vegas on what was then the Los Angeles Highway outside the city limits, escaping Las Vegas municipal taxes and licensing. Hull's Californian resort experience led him to bundle gambling with a swimming pool, western-themed restaurants, and stables, creating the first Strip resort format [Moehring 2000][book_moehring_2000] [Schwartz 2006][book_schwartz_roll_2006]. That extraterritorial siting persists to the present. The Las Vegas Strip has never been within the City of Las Vegas municipal boundaries. It sits in the unincorporated township of Paradise, Nevada, within Clark County, with attendant implications for property taxation, municipal service provisioning, and political representation that distinguish the Strip's tax base from that of the incorporated city to the north.

The Flamingo project began under Hollywood Reporter founder William R. Wilkerson, who conceived and initiated construction of a sophisticated hotel casino modeled on the Beverly Hills and European resort format before Meyer Lansky's syndicate financing displaced him from the project in 1946 [Wilkerson 2000][book_wilkerson_2000]. Bugsy Siegel completed the Flamingo under mob control and opened it in December 1946, formalizing what would become the Strip model. Siegel understood that the fixed cost of a lavish resort could be amortized against gambling revenue if the resort itself drew enough visitors to gamble. Rooms below break-even, buffets priced under cost, and marquee entertainment at wages that no free-standing venue could sustain were rational business decisions if each visitor's expected gambling loss exceeded the amenity subsidy. The mathematics that governed this model can be summarized as follows.

The house edge on a wager provides the fundamental profit mechanism. For a wager of amount $W$ against a game with house hold percentage $h$, the expected value to the player is

$$E[X] = -h \cdot W$$

which equals the expected revenue to the house per dollar wagered. Aggregate gaming revenue $R_g$ across $N$ visitors each generating handle $H$ is then

$$R_g = N \cdot H \cdot h$$

Let $c$ denote the per-visitor amenity subsidy. The casino's expected profit per visitor is the gaming margin minus the subsidy,

$$\pi = h \cdot H - c$$

The Strip's original insight was that $H$ scales with duration of stay, and duration of stay scales with the attractiveness of amenities. If $H = \alpha(c)$ with $\alpha'(c) > 0$, then subsidizing amenities is profit-maximizing up to the point at which the marginal gaming revenue return on subsidy dollars equals one,

$$h \cdot \alpha'(c) = 1$$

The mob-era operators found this range empirically. Cheap steak at the counter, cheap rooms upstairs, and Frank Sinatra on stage all fed the pit downstairs [Schwartz 2003][book_schwartz_2003].

The Rat Pack era from 1959 through the mid 1960s consolidated the Strip's national visibility. Sinatra, Dean Martin, Sammy Davis Jr., Peter Lawford, and Joey Bishop performed at the Sands while filming Ocean's 11 during daylight hours. The Copa Room performances were priced at \\$5.95 including dinner, a rate that could not have supported the performers' contracts as free-standing entertainment. The pit paid the difference. Contemporary journalistic accounts of the Strip's mob-era operations, including Reid and Demaris's 1963 exposé, documented the ownership structures and cash-skim practices in enough detail to prompt sustained federal interest [Reid and Demaris 1963][book_reid_demaris_1963].

Federal pressure on mob-associated casino ownership intensified through the 1960s. The Kefauver Committee's Special Committee to Investigate Organized Crime in Interstate Commerce, chaired by Senator Estes Kefauver, held hearings from May 1950 through May 1951 and its Third Interim Report established the first congressional documentation of mob influence in Nevada gaming [Kefauver 1951][ref_kefauver_1951]. The Nevada Corporate Gaming Act of 1967 and its 1969 expansion, codified in Nevada Revised Statutes chapter 463, enabled publicly traded corporations to hold gaming licenses without individual licensing of every shareholder [Nevada Revised Statutes 463][ref_nrs_463]. This opened a legal path for Howard Hughes's 1966 to 1970 acquisition of the Desert Inn, Sands, Frontier, Silver Slipper, Castaways, and Landmark for approximately \\$300 million [Denton and Morris 2001][book_denton_morris_2001].

## Corporate Consolidation and Megaresort Transformation

The corporate era proceeded in three overlapping phases. First, the Hughes buyouts and subsequent MGM, Hilton, and Harrah's expansions of the 1970s introduced institutional accounting and public reporting to the Strip. Second, Steve Wynn's 1989 opening of the Mirage, financed with \\$630 million in Michael Milken junk bonds, established the megaresort template of 3000-plus rooms combined with themed attractions such as the erupting volcano and the white tiger habitat. Third, the 1990s theme-park phase produced the 1990 Excalibur, the 1993 openings of Luxor and Treasure Island and MGM Grand, the 1997 New York-New York, and the 1998 Bellagio followed in 1999 by Mandalay Bay and Paris and the Venetian, each attempting to replicate the Mirage's amenity-heavy model at larger scale [Earley 2000][book_earley_2000] [Rothman 2002][book_rothman_2002]. Historical revenue and property data curated by the UNLV Center for Gaming Research provides the primary quantitative record for this transformation [UNLV Center for Gaming Research][ref_unlv_cgr].

The financial character of the Strip shifted during this expansion. Let $R_g(t)$ denote gaming revenue and $R_{ng}(t)$ denote non-gaming revenue. The non-gaming share is

$$r_{ng}(t) = \frac{R_{ng}(t)}{R_g(t) + R_{ng}(t)}$$

Nevada Gaming Control Board revenue reports show that non-gaming revenue on the Strip exceeded gaming revenue for the first time in fiscal year 2000, at which point $r_{ng} > 0.5$, and by fiscal year 2019 $r_{ng}$ reached approximately 0.65 [Nevada Gaming Control Board][ref_nevada_gcb]. The revenue mix change had a structural rather than incidental cause. Public corporate ownership required investor returns benchmarked against real estate investment trusts and hospitality chains rather than against gambling operators. Investors would not accept below-cost pricing on rooms and food if those items could be priced at market and generate their own profit contribution.

CityCenter, opened December 2009 at a construction cost of approximately \\$8.5 billion, represented the culmination of the amenity-heavy strategy. The 16.8-million-square-foot complex included the Aria hotel, the Vdara hotel, the Mandarin Oriental, the Crystals shopping mall, and the Veer Towers residential development. The project was undertaken by MGM Mirage in partnership with Dubai World and delivered into a market decimated by the 2008 to 2009 financial crisis. CityCenter's post-opening operations lost approximately \\$1.5 billion cumulative through 2013 before returning to positive EBITDA [MGM 10-K 2013][ref_mgm_10k_2013].

The 2010s brought further shifts. The Cosmopolitan opened December 2010 targeting a younger, more design-conscious demographic. Encore Beach Club opened May 2010 and Marquee at the Cosmopolitan opened December 2010, formalizing the electronic dance music nightclub as a Strip revenue center generating cover charges of \\$30 to \\$75, bottle service minimums of \\$500 to \\$10000, and cocktail prices of \\$18 to \\$28. Resort fees, introduced quietly through the late 2000s at \\$10 to \\$15 per night, escalated by the early 2020s to \\$35 to \\$50 per night at most major Strip properties. Parking, historically free as a foundational amenity, began being charged in 2016 at MGM Resorts properties. Self-parking rates rose from approximately \\$15 per day at launch to approximately \\$18 to \\$25 per day by 2024, with premium properties charging at the upper end of that range [LVCVA Annual Reports][ref_lvcva_annual].

## The Amenity-Priced Regime

By the mid 2020s, the Las Vegas Strip revenue mix and pricing structure differ fundamentally from the mob-era model. Consider the per-visitor economics under both regimes. Under the mob-era model, room and food subsidies of perhaps \\$30 to \\$50 per visitor were justified by expected gambling losses per visitor of \\$100 to \\$200. The subsidy ratio satisfied $c / (h \cdot H) < 1$, and the marginal condition $h \cdot \alpha'(c) \geq 1$ held over the operating range.

Under the amenity-priced regime, the same visitor pays \\$250 to \\$500 per night for a room, \\$75 to \\$150 per person for dinner, \\$50 to \\$150 for a show, \\$18 to \\$28 per cocktail, and \\$35 to \\$50 in resort fees. Per-visitor revenue decomposes as

$$r_v = r_{room} + r_{food} + r_{show} + r_{beverage} + r_{fees} + h \cdot H$$

where each amenity term now carries its own positive profit margin rather than being subsidized against the gaming term. The visitor may still gamble, but the gambling contribution $h \cdot H$ is now a fraction of the sum of amenity contributions. Non-gaming revenue's rise to 65 percent of Strip resort revenue is the direct expression of this shift.

The Las Vegas Convention and Visitors Authority reports declining visitor volume relative to peak. Annual visitation peaked at 42.9 million in 2016 and fell to 40.8 million in 2019 before the 2020 pandemic collapse to 19.0 million. Recovery reached 40.8 million in 2023 and 41.7 million in 2024, still below the 2016 peak despite population growth in the drive-market catchment [LVCVA Annual Reports][ref_lvcva_annual]. Average length of stay contracted from 3.4 nights in 2010 to 3.1 nights in 2024, and the share of visitors who gambled fell from 87 percent in the late 1990s to 68 percent in 2019 to approximately 65 percent in 2024 [LVCVA Annual Reports][ref_lvcva_annual].

The unlearning hypothesis proposed at the outset can now be stated with more precision. The Strip operators have not abandoned the loss-leader model. They have replaced it with a model that treats each amenity as a standalone profit center. The two models optimize different objective functions. The loss-leader model maximized aggregate gaming revenue by drawing high-volume visitors. The amenity-priced model maximizes per-visitor revenue extraction across a bundle of separately priced services. The second model produces higher revenue per visitor at the cost of lower visitor volume and reduced visitor loyalty. Whether it produces higher total profit depends on the price elasticity of visitor volume with respect to per-visitor cost,

$$\epsilon_{V,c} = -\frac{\partial \ln V}{\partial \ln c}$$

Total revenue $R = r_v \cdot V$ is increasing in $c$ if and only if $\epsilon_{V,c} < r_v / c$, which under the amenity-priced regime requires that the elasticity remain moderate as amenity charges rise. If pricing pushes $\epsilon_{V,c}$ toward or above that ratio, further amenity price increases reduce total revenue.

## Regional Relevance

The Las Vegas metropolitan statistical area held approximately 2.34 million residents in the 2020 census and reached an estimated 2.42 million by 2024 US Census Bureau intercensal estimates [US Census Bureau][ref_census_bureau]. The region accounts for approximately 74 percent of Nevada's population and generates approximately 75 percent of Nevada's economic output [US BEA Regional][ref_bea_regional]. Nevada state general fund revenue depends heavily on gaming taxes, which generated approximately \\$1.15 billion in fiscal year 2024, representing approximately 20 percent of total general fund revenue [Nevada Gaming Control Board][ref_nevada_gcb]. The concentration exposes state finances to Strip revenue volatility.

Employment in the leisure and hospitality sector accounts for approximately 27 percent of Las Vegas metropolitan area jobs, the highest concentration among major US metropolitan areas [US BLS QCEW][ref_bls_qcew]. Construction and real estate represent additional cyclically sensitive sectors. The regional economy's beta with respect to the national business cycle is elevated relative to more diversified metropolitan areas, a fact exposed sharply in the 2008 to 2011 downturn when the metropolitan area lost approximately 8 percent of nonfarm jobs and residential property values fell by approximately 60 percent from peak.

The binding regional constraint is water. Las Vegas draws approximately 90 percent of its water supply from Lake Mead via the Colorado River Compact of 1922 [Colorado River Compact 1922][ref_colorado_compact_1922]. The compact's total 15 million acre-foot annual apportionment between Upper and Lower Basins rests on a hydrologically optimistic base period, a mismatch that has structured basin water politics since [Reisner 1986][book_reisner_1986] [Fleck 2016][book_fleck_2016]. Lake Mead's water surface elevation stood at 1229 feet above sea level in 2000 and declined to a low of 1041 feet in July 2022 before partially recovering to 1064 feet by mid 2025. The Southern Nevada Water Authority's Intake No. 1 at 1050 feet and Intake No. 2 at 1000 feet elevation, completed in 1971 and 2000 respectively, were joined in 2015 by Intake No. 3 at 860 feet elevation and in 2020 by the Low Lake Level Pumping Station, which together provide operational withdrawal down to approximately 875 feet reservoir elevation. Hoover Dam reaches dead pool at 895 feet elevation, at which level the dam ceases to release water downstream to Arizona, California, and Mexico [US Bureau of Reclamation][ref_bureau_reclamation].

Per-capita water use in the Las Vegas Valley declined from 314 gallons per capita per day in 2000 to approximately 121 gallons per capita per day in 2024, driven by turf removal programs, water reuse, and progressive rate structures. The SNWA reuses approximately 99 percent of water discharged to sewers by returning treated effluent to Lake Mead via the Las Vegas Wash, receiving return-flow credits under the Colorado River Compact allocation [SNWA Water Resource Plan][ref_snwa_report]. The consumptive water balance available to southern Nevada is

$$W_{avail} = A + R - C_{loss}$$

where $A$ is the base Colorado River Compact allocation of 300000 acre-feet per year, $R$ is the return-flow credit from treated effluent returned to Lake Mead, and $C_{loss}$ is unrecovered evaporative and system losses. Per-capita consumptive use has continued to decline at approximately 1 to 2 percent per year through the 2020s, approximating

$$c(t) = c_0 \, e^{-\lambda (t - t_0)}$$

with $\lambda \approx 0.015$ per year against a 2024 baseline of $c_0 \approx 121$ gallons per capita per day. The metropolitan population ceiling under the binding water constraint is

$$P_{max}(t) = \frac{W_{avail}}{c(t)}$$

Whether the trajectory of $c(t)$ decline can accommodate continued metropolitan population growth in the presence of continued Lake Mead decline is the open regional question.

Beyond gaming and tourism, the metropolitan area functions as a warehousing and distribution node serving the Southern California and Phoenix drive markets. Defense installations in the surrounding region include Nellis Air Force Base immediately northeast of the metropolitan area, Creech Air Force Base as the primary United States Air Force unmanned aerial vehicle operations base, and the Nevada National Security Site formerly known as the Nevada Test Site. The University of Nevada Las Vegas is the primary regional research university. Healthcare, higher education, and manufacturing capacity primarily serve the metropolitan area rather than establishing regional hub status in those categories. Nevada's mining and utility-scale solar generation industries are geographically dispersed across the state rather than concentrated in the metropolitan area.

## Housing Cycle and Residential Real Estate

The Las Vegas metropolitan area's housing market and construction employment constitute a second load-bearing economy alongside gaming and tourism, and the housing cycle amplifies rather than offsets regional business-cycle exposure. From 2000 through 2006 the metropolitan area experienced one of the largest housing booms in the United States, with the Case-Shiller Las Vegas index approximately doubling over the period. Investor and speculative buying was a significant share of transactions, and subprime and Alt-A financing supported purchases that in retrospect could not be sustained by underlying household incomes [Case-Shiller Las Vegas][ref_case_shiller_lv].

The subsequent collapse from 2007 through 2011 was correspondingly the largest in the country. The Case-Shiller Las Vegas index fell by approximately 62 percent from peak to trough, and foreclosure rates in Clark County reached the highest in the United States, with roughly one in fourteen homes receiving a foreclosure filing during 2010 alone [Attom Foreclosure Data][ref_attom_foreclosure]. Construction employment collapsed by more than 60 percent from peak. The housing crash was not incidental to the recession's severity in Las Vegas. It was the primary transmission mechanism, and its duration exceeded the national recovery by several years.

Recovery from 2012 through 2019 restored the Case-Shiller Las Vegas index to roughly 90 percent of its 2006 peak. The 2020 to 2022 pandemic period produced a second sharp acceleration driven by California in-migration and remote-work-enabled buyer inflows, taking the Las Vegas index above the 2006 peak in nominal terms. Subsequent moderation through 2024 and 2025 has been comparatively mild, though inventory levels and interest-rate sensitivity remain concerns.

The structural implication is that the housing cycle amplifies the gaming cycle rather than offsetting it. In a national recession, hospitality employment contracts as visitor volume falls, construction employment contracts as new inventory demand disappears, and property values decline as investors sell. The three effects reinforce rather than cancel, producing the elevated business-cycle beta observed empirically. Any forward projection of the metropolitan area's economic trajectory must treat housing cycle risk as a first-order variable rather than a second-order footnote.

## Labor Economy and the Culinary Union

The dominant labor institution in the Las Vegas metropolitan area is the Culinary Workers Union Local 226, an affiliate of UNITE HERE representing approximately 60000 hotel and casino workers on the Strip and in downtown properties in housekeeping, food service, kitchen, bartending, and other operational roles. Local 226 negotiates master contracts with the major Strip operators including MGM Resorts, Caesars Entertainment, Wynn Resorts, and their peers, and its contract cycles set wage floors and benefit structures for a substantial share of the metropolitan area workforce [Culinary Workers Union Local 226][ref_culinary_226].

The 2023 to 2028 contract cycle covering approximately 40000 workers at MGM Resorts and Caesars Entertainment properties concluded in November 2023 after strike authorization votes and negotiations that attracted national attention. The negotiated agreement included wage increases of approximately 32 percent over five years and preserved the union-administered health benefit trust structure that distinguishes Las Vegas hospitality employment from most non-union comparable markets.

Beyond wages and benefits, Local 226 exercises political influence disproportionate to its membership size. Nevada holds an early presidential primary position, and the union's endorsement mechanics and voter turnout operations have been decisive factors in Nevada Democratic caucuses and primaries since at least 2008. Presidential campaigns from Barack Obama in 2008 through subsequent cycles have treated Culinary Union endorsement as a Nevada gating factor rather than a discretionary asset.

The absence of comparable union representation in gaming and tourism industries in Reno-Sparks, Phoenix, and other Southwestern metropolitan competitors distinguishes Las Vegas's labor market. A business locating operational roles in Las Vegas should treat the union environment as a structural fact rather than a variable, and should distinguish union-scope operational functions from non-union professional, technical, and administrative functions.

## California Business Relocation

Las Vegas's non-gaming economic development is sometimes assumed to be an obvious beneficiary of California business departures, an assumption the geography and industry composition do not fully support. California business relocations distribute across destinations chosen for business-specific optimality rather than for proximity alone. Tesla and Oracle relocated headquarters to Texas. Palantir moved from Palo Alto to Denver. Various finance and technology firms have relocated to Salt Lake City, Austin, Phoenix, and Nashville. The list of destinations reflects factors including workforce availability, existing industry cluster presence, tax structure, employee cost of living, and physical infrastructure rather than a single optimizing rule.

Of California business relocations that stay in the Western time zone, Arizona has captured substantial share. Phoenix metropolitan area developments include TSMC's semiconductor fabrication complex in north Phoenix and Intel's Ocotillo expansion in Chandler, along with technology and finance firm relocations to Scottsdale and Chandler [TSMC Arizona][ref_tsmc_arizona]. Arizona's advantages relative to Nevada include a larger existing technology employer base, a Phoenix metropolitan area labor market roughly twice the size of the Las Vegas metropolitan area, and existing industrial water infrastructure sized for high-consumption manufacturing.

Of California business relocations that cross the Sierra Nevada into the state of Nevada, the Reno-Sparks metropolitan area in northern Nevada has captured the bulk of the industrial and technology activity rather than Las Vegas. Tesla's Nevada Gigafactory at the Tahoe-Reno Industrial Center began operations in 2016 and produces electric-vehicle battery cells and modules in partnership with Panasonic [Tesla Nevada][ref_tesla_nevada]. Switch operates a major data center campus at the same industrial center. Apple, Google, and Microsoft each have data center operations in northern Nevada. The reasons for Reno's concentration of industrial and technology activity include a 200-mile drive from the San Francisco Bay Area versus approximately 400 miles from the Bay Area to Las Vegas, an existing industrial base and workforce, Truckee River water access, and cooler summer temperatures that lower data center cooling costs [Nevada GOED][ref_nv_goed].

Las Vegas receives a smaller share of California business relocation activity, concentrated in sectors that align with the existing tourism-hospitality-entertainment complex rather than in general business categories. Notable relocations include the Oakland Raiders in 2020, the Oakland Athletics announced in 2023, and gaming-technology and hospitality firms. Individual and household relocation from California is substantial, driven by lower housing costs and Nevada's absence of state personal income tax, but this pattern does not materially change the metropolitan area's industry concentration in gaming, hospitality, entertainment, conventions, and sports.

The distinction matters for evaluating Las Vegas's relevance claims. California business relocation supports the narrative that Nevada is a desirable business destination, but the specific benefit accrues predominantly to Reno-Sparks and only secondarily to Las Vegas. A general Nevada business-friendly framing risks conflating the northern Nevada industrial-technology story with the southern Nevada tourism-entertainment story. The two subregions of Nevada are functionally distinct economies with different labor markets, physical constraints, and industrial specializations.

## Business Location Considerations

A business evaluating whether to locate a headquarters or satellite office in Las Vegas benefits from a decision framework that separates the metropolitan area's genuine location advantages from the tourism-narrative halo. The dimensions that anchor the decision are cost structure, workforce composition, physical infrastructure, regulatory environment, industry cluster adjacencies, and physical risk factors. Each dimension has a Las Vegas answer that differs from the more generic Nevada answer.

On cost structure, Nevada imposes no state personal income tax and no corporate income tax, which is unusual among United States jurisdictions. The state does levy a Modified Business Tax on wages above threshold at approximately 1.475 percent, a Commerce Tax on gross receipts above four million dollars at approximately 0.05 to 0.33 percent depending on industry, and a state and local sales tax in Clark County at 8.375 percent [Nevada Department of Taxation][ref_nv_dor]. Property tax effective rates run near 0.5 percent, below the national median. Commercial office lease rates for Class A space in the mid 2020s run roughly \\$30 to \\$40 per square foot per year, and industrial and warehouse space runs roughly \\$10 to \\$14 per square foot per year, both materially below Bay Area comparables and roughly at parity with Phoenix and Reno-Sparks [CBRE Las Vegas][ref_cbre_las_vegas]. Residential median home price sits near \\$450000 in 2024, reducing the housing cost hurdle for employee relocation from higher-cost California markets.

On workforce composition, the metropolitan area labor force concentrates heavily in leisure and hospitality, construction, real estate, retail trade, and administrative support. Professional and business services are present but not dominant, and technology-specific workforce depth is thin outside gaming technology, casino management systems, hospitality technology, and sports-betting operations. Specialized workforce strengths include casino operations, event management, entertainment production, and hospitality management at levels difficult to match elsewhere in the United States. Median household income runs modestly below the national median. Workforce mobility includes a continuous inflow from California and other higher-cost states, providing some professional-services and executive-level talent that would be harder to recruit locally.

On physical infrastructure, Harry Reid International Airport is among the busiest United States airports by passenger volume and offers direct nonstop service to essentially every major United States city plus substantial international connectivity [Harry Reid International Airport][ref_lasairport]. The air hub is a genuine business asset for satellite offices whose staff travel frequently. Highway infrastructure includes Interstate 15 connecting Los Angeles and Salt Lake City, which supports both trucking logistics and business travel from Southern California. Rail freight is limited. Power availability is reasonable and pricing competitive within the Southwest. Data center presence is smaller than the Reno-Sparks industry cluster, though some data center operations exist within the metropolitan area. Water availability for water-intensive industrial operations is the binding physical constraint discussed earlier and is expected to tighten further through 2050.

On regulatory environment, Nevada business registration is straightforward, permitting is generally faster than California, and the environment is business-friendly outside the gaming and cannabis licensing systems that are heavily regulated by design. The state court system handles commercial disputes with typical Western United States efficiency.

Positive fit categories for satellite offices in Las Vegas include sales offices covering the Southwest United States market from Los Angeles through Phoenix, event and conference and hospitality-industry outposts that leverage the convention infrastructure, executive travel hubs that leverage the Harry Reid International connectivity, gaming and sports-betting technology development centers that align with the existing regulatory expertise and operator concentration, Southern California overflow warehousing and distribution, hospitality-technology and event-management-technology development shops, regional customer support and back-office operations, entertainment production and media ancillary functions, and small executive offices for founders and senior executives seeking a low-tax base with international air connectivity.

Negative fit categories include engineering and research anchor offices requiring deep specialized technology talent, biotechnology and pharmaceutical research, financial services headquarters requiring proximity to Wall Street or the Bay Area venture capital ecosystem, higher education research centers requiring proximity to major research universities, advanced manufacturing requiring a mature supplier ecosystem, aerospace and defense industrial base operations, semiconductor manufacturing given the Phoenix cluster's dominance in that specialty, water-intensive industrial operations facing the tightening Colorado River constraint, and government relations offices requiring proximity to Washington DC or Sacramento.

A business seeking to locate a satellite office in Las Vegas should verify that the office function fits at least one of the positive-fit categories, that the required workforce can be sourced locally or through relocation inflow from California, that the office does not require deep specialized talent Las Vegas lacks, that it does not benefit substantially from proximity to a specific industry cluster elsewhere, and that its operational profile does not require water-intensive infrastructure or is not exposed to extreme heat risk on a business-critical timeline. When these conditions are met, Las Vegas offers a competitive location with material tax advantages, air connectivity, and hospitality-adjacent industry depth. When they are not met, Reno-Sparks for industrial and technology, Phoenix for semiconductor and technology, Salt Lake City for Silicon Slopes technology, or the business-optimum state elsewhere in the West typically dominates.

## National Relevance

Las Vegas serves the national economy as a convention and trade show hub, a professional sports market, and a large-scale entertainment production venue. The Las Vegas Convention Center and the Sands Expo host events including the Consumer Electronics Show at approximately 138000 attendees in January 2024, the SEMA Show at approximately 160000 attendees in November 2024, and the World of Concrete at approximately 55000 attendees each January. Total convention attendance reached 5.9 million in 2019 before pandemic disruption and recovered to 5.5 million in 2023 and 6.2 million in 2024 [LVCVA Annual Reports][ref_lvcva_annual].

The professional sports transition has been rapid. The Vegas Golden Knights of the National Hockey League began play in October 2017 and won the Stanley Cup in 2023. The Las Vegas Raiders of the National Football League relocated from Oakland in 2020 and opened Allegiant Stadium at approximately \\$1.9 billion construction cost with \\$750 million in public financing from a hotel room tax. The Las Vegas Aces of the Women's National Basketball Association won consecutive championships in 2022 and 2023. Major League Baseball's Athletics announced relocation from Oakland in 2023 with an approved 33000-seat stadium on the former Tropicana site at approximately \\$1.75 billion construction cost including \\$380 million in public financing. The National Basketball Association has intermittently identified Las Vegas as an expansion candidate [Las Vegas Review-Journal][ref_las_vegas_review_journal].

The Sphere at the Venetian, opened September 2023 at approximately \\$2.3 billion construction cost, represents a distinctive entertainment technology deployment. The 366-foot-diameter, 516-foot-tall structure includes a 160000-square-foot 16K resolution interior LED screen and a 580000-square-foot exterior LED display. The venue hosted U2 residency performances from September 2023 through March 2024 and subsequent Dead and Company, Eagles, and Backstreet Boys residencies. Whether the Sphere business model generates positive economics against its capital cost remains uncertain [Sphere Entertainment 10-K][ref_msg_sphere_10k].

The Las Vegas Grand Prix returned to the Formula One calendar in November 2023 after previous 1981 and 1982 Caesars Palace Grand Prix events. The 6.201 kilometer street circuit runs down Las Vegas Boulevard past the Bellagio fountains and Caesars Palace, with Liberty Media investing approximately \\$500 million in the paddock building and infrastructure. Initial attendance and hotel-rate impact fell below projections in 2023 but improved in 2024 [Liberty Media 10-K][ref_liberty_media_10k].

National relevance in other industry categories is limited. Boxing and mixed martial arts host major national fight cards at Las Vegas venues including T-Mobile Arena and MGM Grand Garden Arena, and the city functions as a national market for adult-oriented entertainment. Higher education, healthcare, defense industrial base, financial services, and manufacturing do not extend beyond the metropolitan area at a nationally relevant scale. The city's national position rests on the tourism-entertainment complex that gambling originally built and its subsequent extensions into conventions, professional sports, and immersive entertainment.

## Global Relevance

The most consequential shift in Las Vegas's global position occurred in 2006 when the Macau Special Administrative Region's gaming revenue surpassed the Las Vegas Strip's gaming revenue. Define the ratio

$$\rho_{MV}(t) = \frac{R_M(t)}{R_V(t)}$$

where $R_M(t)$ is Macau gaming revenue and $R_V(t)$ is Las Vegas Strip gaming revenue in year $t$. Macau's 2006 gaming revenue reached approximately \\$6.95 billion against the Strip's \\$6.69 billion so that $\rho_{MV}(2006) \approx 1.04$. By 2013 Macau's gaming revenue peaked at approximately \\$45.2 billion against the Strip's \\$6.5 billion, giving $\rho_{MV}(2013) \approx 6.95$. Macau's subsequent contraction under Chinese anticorruption enforcement and pandemic border closures reduced 2020 gaming revenue to approximately \\$7.6 billion. Recovery reached approximately \\$22.7 billion in 2023 and approximately \\$29 billion in 2024 against the Strip's approximately \\$8.8 billion in 2024, giving $\rho_{MV}(2024) \approx 3.30$, still below the 2013 peak but decisively above unity [Macau DICJ][ref_macau_dicj] [Nevada Gaming Control Board][ref_nevada_gcb].

The Las Vegas Sands Corporation, founded by Sheldon Adelson and operator of the Venetian and Palazzo on the Strip, divested its Las Vegas properties in 2022 to VICI Properties and Apollo Global Management for approximately \\$6.25 billion. Las Vegas Sands retained its Macau operations under the Sands China Limited subsidiary comprising the Venetian Macao and the Londoner Macao and the Parisian Macao and Sands Macao and the Four Seasons Macao, and its Singapore operations comprising Marina Bay Sands. The divestment expressed a corporate judgment that Asian gaming markets offered better risk-adjusted returns than the Las Vegas Strip [Las Vegas Sands 10-K][ref_lvs_10k].

Wynn Resorts pursued a similar geographic reweighting. Steve Wynn opened Wynn Macau in September 2006 and Wynn Palace in Cotai in August 2016, and the company reports Macau as its largest segment by revenue and EBITDA in most years. The company also operates Wynn Encore Boston Harbor, opened June 2019 at approximately \\$2.6 billion construction cost, and announced Wynn Al Marjan Island in Ras al Khaimah, United Arab Emirates, targeted for 2027 opening as the first integrated resort casino in the UAE [Wynn Resorts 10-K][ref_wynn_10k].

MGM Resorts International retains its Las Vegas Strip concentration but has expanded regionally within the United States through MGM National Harbor in Maryland, MGM Springfield in Massachusetts, and Empire City in New York, and internationally through MGM Cotai in Macau. The company is among the applicants for one of three New York City-area downstate casino licenses in the 2025 to 2026 licensing round, with its Empire City property as its proposed development site [MGM 10-K 2024][ref_mgm_10k_2024].

Singapore's two integrated resorts are Marina Bay Sands operated by Las Vegas Sands and Resorts World Sentosa operated by Genting, which together generated approximately \\$6.5 billion in gaming revenue in 2024. The Philippines' Entertainment City complex in Manila generated approximately \\$5 billion. Vietnam, Cambodia, and South Korea host smaller casino industries oriented largely toward foreign visitors under domestic gambling restrictions. The Middle East casino frontier is expected to open in 2027 with Wynn Al Marjan and subsequent projects in Ras al Khaimah [Asia Gaming Brief][ref_agb_briefings].

The global gaming industry structure that Las Vegas dominated for approximately four decades has been replaced by a multipolar structure in which Asian centers generate the majority of revenue, US regional and tribal casinos capture the majority of US gaming revenue outside Nevada, and the Las Vegas Strip retains its distinctive position as an integrated entertainment-plus-gaming destination rather than as a pure gambling market. The city's global brand recognition remains high, and its role as a template for integrated resort development has been widely emulated. The commercial ranking, however, has shifted substantially.

Outside the gaming industry and the integrated resort template it exports, Las Vegas has limited global relevance. The Sphere at the Venetian represents a distinctive entertainment technology export with proposed international deployments, but the technology remains at experimental scale rather than defining a global category. International convention attendance provides an incremental global component but Las Vegas competes with global convention centers rather than defining that category. Higher education, research, manufacturing, financial services, and the other categories that anchor multi-industry globally-relevant cities are absent at scale. Not every city has global relevance across categories, and Las Vegas's global position is essentially defined by a single industry and its integrated resort format.

## US Domestic Competition

Tribal gaming under the Indian Gaming Regulatory Act of 1988, Public Law 100-497 codified at 25 USC chapter 29, has grown from approximately \\$121 million in 1988 to approximately \\$41.8 billion in 2023, approaching total US commercial casino gaming revenue of approximately \\$66.5 billion in 2024. Tribal and commercial together define a US gaming market above \\$100 billion in annual gross revenue [IGRA 1988][ref_igra_1988] [NIGA Report][ref_niga_report] [AGA State of the States 2024][ref_aga_report]. California tribal casinos alone generate approximately \\$9 billion annually, drawing from the Los Angeles and Bay Area drive markets that once fed Las Vegas. Arizona tribal casinos generate approximately \\$2.5 billion annually. New Mexico tribal casinos and Oklahoma tribal casinos each generate over \\$2 billion. The regional competition has substantially reduced the drive-market catchment for casual gamblers from the western United States who once traveled to Las Vegas primarily for gambling.

Commercial casino expansion outside Nevada has been similarly rapid. Pennsylvania authorized casinos in 2004 and reached approximately \\$5.5 billion in 2024 gaming revenue, second only to Nevada among states. Michigan, Ohio, Indiana, Missouri, Illinois, Louisiana, Maryland, and New Jersey each generate over \\$2 billion annually in commercial gaming revenue [AGA State of the States 2024][ref_aga_report]. The New York downstate license process concluding in 2025 authorizes three new commercial casinos in the New York City metropolitan area, further reducing the incentive for East Coast residents to travel to Las Vegas for gambling.

Online sports betting and iGaming represent the most recent structural change. The Supreme Court's 2018 decision in Murphy v. National Collegiate Athletic Association struck down the Professional and Amateur Sports Protection Act of 1992 on Tenth Amendment anticommandeering grounds, opening state-by-state legalization of sports betting [Murphy v NCAA 2018][ref_murphy_ncaa_2018]. By early 2026, thirty-nine states plus the District of Columbia have legal sports betting, generating approximately \\$13.7 billion in gross revenue in 2024. Online casino gaming is legal in seven states generating approximately \\$8.5 billion in 2024 [AGA State of the States 2024][ref_aga_report]. The share of gambling activity that must occur physically in Las Vegas has correspondingly declined.

## Forward Projection

The projection horizon of primary interest is 2026 to 2050. Five constraints will shape the outcome, and two structural transformations will run alongside them.

First, the water constraint on the Colorado River basin will tighten. The 2019 Drought Contingency Plan and the 2023 Lower Basin Historic Consensus-Based Modeling Alternative both anticipate continued reservoir decline under median hydrology assumptions. Southern Nevada's 300000 acre-foot Colorado River allocation is small relative to California's 4.4 million acre-foot allocation and Arizona's 2.8 million acre-foot allocation, which limits Nevada's absolute exposure to allocation reductions but does not eliminate the risk of physical inability to deliver water at reservoir elevations below the low-lake-level pumping station threshold. Continued metropolitan population growth in the presence of continued reservoir decline will require either substantial per-capita consumption reduction below 100 gallons per capita per day, expansion of water reuse, importation from outside the Colorado River basin, or acceptance of a population ceiling.

Second, the climate constraint will tighten. Southern Nevada's annual number of days at or above 105 degrees Fahrenheit averaged 55 days per year in 2010 to 2019 and rose to 68 days per year in 2020 to 2024 according to NOAA National Weather Service records at Harry Reid International Airport [NOAA NWS Las Vegas][ref_noaa_las_vegas]. IPCC Sixth Assessment Working Group II regional projections for the North American Southwest anticipate continued mean temperature rise on the order of 1.5 to 3 degrees Celsius under a range of Representative Concentration Pathway emissions scenarios through 2050 [IPCC AR6 WGII Ch 14][ref_ipcc_ar6_wg2]. The 2024 summer produced 112 days at or above 100 degrees Fahrenheit including 32 consecutive days from 8 June through 9 July. A linear extrapolation of the observed trend gives

$$D_{105}(t) = D_0 + \beta (t - t_0)$$

with $D_0 \approx 68$ days per year at $t_0 = 2024$ and $\beta \approx 1.3$ days per year. Projecting forward, $D_{105}(2050) \approx 102$ days per year. The physical viability of an outdoor entertainment economy, including F1 race weekends in November when temperatures remain manageable and pool-club summer operations when temperatures do not, is a load-bearing assumption of the current business model that the trend places under increasing pressure.

Third, the competition constraint will tighten. Regional and tribal casino expansion continues, online sports betting and iGaming legalization continues, and Asian gaming markets continue to grow at rates above US market growth. Define the Strip's share of US commercial gaming revenue,

$$s_{LV}(t) = \frac{R_V(t)}{R_{US}(t)}$$

This share has declined from $s_{LV}(2000) \approx 0.30$ to $s_{LV}(2024) \approx 0.13$. Whether $s_{LV}(t)$ stabilizes or continues to erode depends on whether the Strip's distinctive integrated entertainment-plus-gaming offering retains its price premium against regional alternatives.

Fourth, the demographic constraint will tighten. Gambling participation is age-correlated. Approximately 68 percent of adults born 1946 to 1964 report gambling at least once per year, against approximately 57 percent of adults born 1965 to 1980, approximately 51 percent of adults born 1981 to 1996, and approximately 42 percent of adults born 1997 to 2012 [Gambling Participation Survey][ref_agrs_survey]. Let $p_c$ denote the annual gambling participation rate for cohort $c$ and $w_c(t)$ denote the population share of cohort $c$ in year $t$. The aggregate gambling participation rate is

$$P_g(t) = \sum_c w_c(t) \, p_c$$

Under the assumption that $p_c$ is constant across the projection window and $w_c(t)$ evolves with cohort aging and mortality, $P_g(t)$ declines monotonically as the postwar-birth cohort ages out of active travel. The base of gamblers who travel for gambling will contract unless younger cohorts show delayed uptake, in which case $p_c$ becomes age-varying rather than cohort-fixed, or unless the Strip's non-gaming offering attracts these cohorts on its own merits.

Fifth, the pricing-power constraint will tighten. The amenity-priced regime depends on the Strip's ability to sustain premium pricing on rooms, food, entertainment, and ancillary services. The premium depends in turn on the Strip's brand differentiation from regional alternatives. The 2024 to 2025 experience of resort fee, parking fee, and food-and-beverage price increases producing visible visitor pushback in social media and consumer reporting channels suggests that pricing power has approached its practical ceiling under current visitor expectations. Whether the operators respond with pricing moderation, product differentiation, or continued extraction until the market corrects sharply is an open corporate strategy question.

Alongside these five constraints, transformative infrastructure could reshape the Southern California drive-market catchment. Brightline West began construction in April 2024 on a high-speed rail line between Las Vegas and Rancho Cucamonga in the eastern Los Angeles basin, targeted for opening in 2028 to 2030 at approximately \\$12 billion in construction cost. The line would compress a four-hour drive to approximately two hours of transit time and would connect to the Metrolink commuter rail system serving downtown Los Angeles [Brightline West][ref_brightline_west]. The passenger volume impact on the drive market, which currently supplies the largest share of Las Vegas visitors, would be first-order rather than incremental if delivered on the projected schedule. The Boring Company Vegas Loop tunnels under the Las Vegas Convention Center have been operational since 2021 as Tesla-based small-scale intra-city transit, and contemplated expansion under the Strip and to Harry Reid International Airport would extend that footprint, though at a smaller scale than intercity rail [Boring Company Vegas Loop][ref_boring_loop].

The second structural transformation is the diversification prospect on the energy-and-compute axis. The 2020s wave of artificial-intelligence-driven data center construction has intensified competition among Western United States locations for large-scale compute infrastructure. The relevant siting variables are power availability at competitive tariffs, water for cooling, ambient temperature affecting cooling energy demand, and regulatory speed on siting and interconnection. On these variables Reno-Sparks continues to dominate Las Vegas within Nevada, and Phoenix continues to dominate both Nevada markets on integrated semiconductor-plus-compute clustering. Nevada's utility-scale solar generation capacity, dispersed across state land holdings, offers a policy lever that has not yet been fully directed toward metropolitan-area diversification. Any off-gaming future for Las Vegas will require deliberate investment in the power and water infrastructure that data centers demand, together with grid interconnection capacity that does not currently favor southern Nevada. In the absence of such investment, diversification into deep technology remains constrained by structural fundamentals that do not favor the metropolitan area, and the diversification path more likely takes the form of hospitality-adjacent extensions into sports, entertainment technology, and events rather than deep technology parity with Reno-Sparks or Phoenix.

The overall forward projection can be stated as follows, with epistemic status of high-confidence trend continuation rather than precise point forecast. Las Vegas is expected to retain its distinctive integrated entertainment destination role through the 2026 to 2050 window but is likely to operate under increasingly binding physical, competitive, and demographic constraints. The city's growth trajectory will likely flatten from the historical 2 to 3 percent annual population growth to something closer to 0.5 to 1 percent annual growth by the 2040s. The Strip's revenue mix will likely continue to shift toward non-gaming, and the gambling share may fall below 30 percent of total resort revenue by 2035. Competition from Asian gaming centers and US regional casinos will likely constrain the Strip's ability to grow gaming revenue in real terms. The city's relative position within the global gaming industry is likely to continue declining in market-share terms while remaining large in absolute terms.

Whether the amenity-priced regime is a stable equilibrium or a transitional overshoot is the load-bearing open question. If it is stable, the Strip transitions from a gambling city that happens to have entertainment to an entertainment city that happens to have gambling. If it is a transitional overshoot, some future operator will rediscover the loss-leader model at scale and pull market share back from a competitor set that has forgotten how to price amenities below cost. The historical pattern of business-cycle discipline in the industry suggests that a serious recession would compress amenity pricing sharply and would reveal which properties can sustain their debt loads under recessed room rates.

## Load-Bearing Open Questions

- What is the price elasticity of Strip visitor volume with respect to per-visitor amenity cost, and where does the current pricing structure sit on the elasticity curve?
- What is the population ceiling of the Las Vegas metropolitan area under the binding Colorado River water constraint, and what capital investment in reuse, importation, or per-capita consumption reduction would raise that ceiling?
- Does the demographic decline in gambling participation among younger cohorts represent a permanent preference shift, a delayed uptake pattern, or a substitution toward online sports betting and iGaming?
- Can Sphere-scale immersive entertainment venues generate positive returns on capital costs of \\$2 billion or more, or does the Sphere represent a one-off subsidized experiment?
- Does the Las Vegas convention and trade show hub role reinforce or substitute for the leisure tourism role, and what is the cross-elasticity of demand between the two visitor segments?
- What is the failure mode of a Strip megaresort under a serious recession combined with tight water restrictions, and which properties have the debt structure and operational flexibility to survive that stress?

## References

### Books

- [Denton and Morris 2001][book_denton_morris_2001]
- [Earley 2000][book_earley_2000]
- [Findlay 1986][book_findlay_1986]
- [Fleck 2016][book_fleck_2016]
- [Moehring 2000][book_moehring_2000]
- [Reid and Demaris 1963][book_reid_demaris_1963]
- [Reisner 1986][book_reisner_1986]
- [Rothman 2002][book_rothman_2002]
- [Schwartz 2003][book_schwartz_2003]
- [Schwartz 2006][book_schwartz_roll_2006]
- [Wilkerson 2000][book_wilkerson_2000]

### Reference

- [Asia Gaming Brief][ref_agb_briefings]
- [AGA State of the States 2024][ref_aga_report]
- [Gambling Participation Survey][ref_agrs_survey]
- [US BEA Regional][ref_bea_regional]
- [US BLS QCEW][ref_bls_qcew]
- [Attom Foreclosure Data][ref_attom_foreclosure]
- [US Bureau of Reclamation][ref_bureau_reclamation]
- [US Census Bureau][ref_census_bureau]
- [Boring Company Vegas Loop][ref_boring_loop]
- [Brightline West][ref_brightline_west]
- [Case-Shiller Las Vegas][ref_case_shiller_lv]
- [CBRE Las Vegas][ref_cbre_las_vegas]
- [Colorado River Compact 1922][ref_colorado_compact_1922]
- [Culinary Workers Union Local 226][ref_culinary_226]
- [Harry Reid International Airport][ref_lasairport]
- [IGRA 1988][ref_igra_1988]
- [IPCC AR6 WGII Ch 14][ref_ipcc_ar6_wg2]
- [Kefauver 1951][ref_kefauver_1951]
- [Las Vegas Review-Journal][ref_las_vegas_review_journal]
- [Liberty Media 10-K][ref_liberty_media_10k]
- [LVCVA Annual Reports][ref_lvcva_annual]
- [Las Vegas Sands 10-K][ref_lvs_10k]
- [Macau DICJ][ref_macau_dicj]
- [MGM 10-K 2013][ref_mgm_10k_2013]
- [MGM 10-K 2024][ref_mgm_10k_2024]
- [Sphere Entertainment 10-K][ref_msg_sphere_10k]
- [Murphy v NCAA 2018][ref_murphy_ncaa_2018]
- [Nevada Gaming Control Board][ref_nevada_gcb]
- [NIGA Report][ref_niga_report]
- [Nevada Department of Taxation][ref_nv_dor]
- [Nevada GOED][ref_nv_goed]
- [NOAA NWS Las Vegas][ref_noaa_las_vegas]
- [Nevada Revised Statutes 463][ref_nrs_463]
- [SNWA Water Resource Plan][ref_snwa_report]
- [Stanton 2020][ref_stanton_2020]
- [Tesla Nevada][ref_tesla_nevada]
- [TSMC Arizona][ref_tsmc_arizona]
- [UNLV Center for Gaming Research][ref_unlv_cgr]
- [Wynn Resorts 10-K][ref_wynn_10k]

### Research

- [Borg Mason Shapiro 2015][research_borg_2015]
- [Eadington 1999][research_eadington_1999]
- [Walker 2007][research_walker_2007]

[book_denton_morris_2001]: https://www.penguinrandomhouse.com/books/59015/the-money-and-the-power-by-sally-denton-and-roger-morris/
[book_earley_2000]: https://www.penguinrandomhouse.com/books/59014/super-casino-by-pete-earley/
[book_findlay_1986]: https://global.oup.com/academic/product/people-of-chance-9780195055016
[book_fleck_2016]: https://islandpress.org/books/water-fighting-over
[book_moehring_2000]: https://unpress.nevada.edu/9780874173567/resort-city-in-the-sunbelt-second-edition/
[book_reid_demaris_1963]: https://www.worldcat.org/title/green-felt-jungle/oclc/577895
[book_reisner_1986]: https://www.penguinrandomhouse.com/books/56276/cadillac-desert-by-marc-reisner/
[book_rothman_2002]: https://www.routledge.com/Neon-Metropolis-How-Las-Vegas-Started-the-Twenty-First-Century/Rothman/p/book/9780415926126
[book_schwartz_2003]: https://www.routledge.com/Suburban-Xanadu-The-Casino-Resort-on-the-Las-Vegas-Strip-and-Beyond/Schwartz/p/book/9780415935562
[book_schwartz_roll_2006]: https://www.penguinrandomhouse.com/books/294024/roll-the-bones-by-david-g-schwartz/
[book_wilkerson_2000]: https://www.worldcat.org/title/man-who-invented-las-vegas/oclc/44628988
[ref_agb_briefings]: https://agbrief.com/
[ref_aga_report]: https://www.americangaming.org/resources/state-of-the-states-2024/
[ref_agrs_survey]: https://nationalcouncilonproblemgambling.org/
[ref_bea_regional]: https://www.bea.gov/data/economic-accounts/regional
[ref_bls_qcew]: https://www.bls.gov/cew/
[ref_attom_foreclosure]: https://www.attomdata.com/data/foreclosure-data/
[ref_boring_loop]: https://www.boringcompany.com/vegas-loop
[ref_brightline_west]: https://www.gobrightline.com/west
[ref_bureau_reclamation]: https://www.usbr.gov/lc/region/g4000/hourly/mead-elv.html
[ref_case_shiller_lv]: https://fred.stlouisfed.org/series/LVXRSA
[ref_cbre_las_vegas]: https://www.cbre.com/insights/figures/las-vegas-office-figures
[ref_culinary_226]: https://www.culinaryunion226.org/
[ref_census_bureau]: https://www.census.gov/quickfacts/lasvegascitynevada
[ref_colorado_compact_1922]: https://www.usbr.gov/lc/region/pao/pdfiles/crcompct.pdf
[ref_igra_1988]: https://www.govinfo.gov/app/details/STATUTE-102/STATUTE-102-Pg2467
[ref_ipcc_ar6_wg2]: https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-14/
[ref_kefauver_1951]: https://www.govinfo.gov/app/collection/serialset
[ref_lasairport]: https://www.harryreidairport.com/
[ref_las_vegas_review_journal]: https://www.reviewjournal.com/sports/
[ref_liberty_media_10k]: https://www.libertymedia.com/investors
[ref_lvcva_annual]: https://www.lvcva.com/research/
[ref_lvs_10k]: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001300514&type=10-K&dateb=&owner=include&count=40
[ref_macau_dicj]: https://www.dicj.gov.mo/web/en/information/DadosEstat_mensal/index.html
[ref_mgm_10k_2013]: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000789570&type=10-K&dateb=20140101&owner=include&count=40
[ref_mgm_10k_2024]: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000789570&type=10-K&dateb=&owner=include&count=40
[ref_msg_sphere_10k]: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001874482&type=10-K&dateb=&owner=include&count=40
[ref_murphy_ncaa_2018]: https://www.supremecourt.gov/opinions/17pdf/16-476_dbfi.pdf
[ref_nevada_gcb]: https://gaming.nv.gov/
[ref_niga_report]: https://www.indiangaming.org/
[ref_noaa_las_vegas]: https://www.weather.gov/vef/climate
[ref_nrs_463]: https://www.leg.state.nv.us/nrs/nrs-463.html
[ref_nv_dor]: https://tax.nv.gov/
[ref_nv_goed]: https://goed.nv.gov/
[ref_snwa_report]: https://www.snwa.com/
[ref_stanton_2020]: https://shpo.nv.gov/
[ref_tesla_nevada]: https://www.tesla.com/gigafactory
[ref_tsmc_arizona]: https://www.tsmc.com/english/aboutTSMC/tsmc_arizona
[ref_unlv_cgr]: https://gaming.library.unlv.edu/
[ref_wynn_10k]: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001174922&type=10-K&dateb=&owner=include&count=40
[research_borg_2015]: https://onlinelibrary.wiley.com/doi/10.1111/ajes.12123
[research_eadington_1999]: https://www.aeaweb.org/articles?id=10.1257/jep.13.3.173
[research_walker_2007]: https://link.springer.com/book/10.1007/978-0-387-72325-2
