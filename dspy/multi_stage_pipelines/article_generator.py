import dspy
lm = dspy.LM('openai/gpt-4o-mini', api_key="OPENAI_API_KEY")
dspy.configure(lm=lm)

class Outline(dspy.Signature):
    """Outline a thorough overview of a topic."""

    topic: str = dspy.InputField()
    title: str = dspy.OutputField()
    sections: list[str] = dspy.OutputField()
    section_subheadings: dict[str, list[str]] = dspy.OutputField(desc="mapping from section headings to subheadings")

class DraftSection(dspy.Signature):
    """Draft a top-level section of an article."""

    topic: str = dspy.InputField()
    section_heading: str = dspy.InputField()
    section_subheadings: list[str] = dspy.InputField()
    content: str = dspy.OutputField(desc="markdown-formatted section")

class DraftArticle(dspy.Module):
    def __init__(self):
        self.build_outline = dspy.ChainOfThought(Outline)
        self.draft_section = dspy.ChainOfThought(DraftSection)

    def forward(self, topic):
        outline = self.build_outline(topic=topic)
        sections = []
        for heading, subheadings in outline.section_subheadings.items():
            section, subheadings = f"## {heading}", [f"### {subheading}" for subheading in subheadings]
            section = self.draft_section(topic=outline.title, section_heading=section, section_subheadings=subheadings)
            sections.append(section.content)
        return dspy.Prediction(title=outline.title, sections=sections)

draft_article = DraftArticle()
article = draft_article(topic="World Cup 2002")

print(article)





# OUTPUT : 

# Prediction(
#     title='Overview of the 2002 FIFA World Cup',
#     sections=["## Historical Context\n\n### Previous World Cups\nThe FIFA World Cup has a rich history, with the inaugural tournament taking place in 1930. By 2002, the tournament had evolved significantly, showcasing the world's best teams and players. Previous editions, particularly the 1998 World Cup in France, set high expectations for the competition. The 1998 tournament was notable for its dramatic matches and the emergence of new footballing nations, which paved the way for a more diverse competition in 2002.\n\n### Selection of Hosts\nThe decision to host the 2002 World Cup in South Korea and Japan was groundbreaking. It was the first time the tournament was held in Asia, reflecting FIFA's commitment to expanding the reach of football. The selection process was competitive, with several countries vying for the opportunity. Ultimately, the co-hosting arrangement allowed both nations to showcase their culture and hospitality, while also promoting football in a region that had been historically underrepresented in the World Cup.\n\n### Significance of Asia\nThe 2002 World Cup was significant not only for its location but also for its impact on Asian football. The tournament provided a platform for Asian teams to compete at the highest level, with South Korea making an unprecedented run to the semifinals. This achievement inspired a new generation of players and fans in Asia, highlighting the continent's potential in the global football arena. The success of the tournament in Asia also encouraged FIFA to consider more Asian nations for future events, further integrating the region into the world of football.", "## Tournament Format\n\nThe 2002 FIFA World Cup featured a well-structured tournament format that included a group stage followed by a knockout stage, leading to the final match. This format ensured that teams had multiple opportunities to compete, while also maintaining the thrill of elimination.\n\n### Group Stage\nIn the group stage, 32 teams were divided into eight groups of four. Each team played three matches against the other teams in their group. Points were awarded as follows: three points for a win, one point for a draw, and none for a loss. The top two teams from each group, based on total points, advanced to the knockout stage. This phase was crucial as it set the stage for the teams that would continue their journey in the tournament.\n\n### Knockout Stage\nThe knockout stage consisted of four rounds: the Round of 16, Quarter-finals, Semi-finals, and the Final. In this phase, matches were single-elimination, meaning that the losing team was eliminated from the tournament. If a match ended in a draw after 90 minutes, it proceeded to extra time, and if still tied, a penalty shootout determined the winner. This format heightened the stakes and excitement, as every match could potentially end a team's World Cup dream.\n\n### Final Match\nThe final match was the culmination of the tournament, featuring the two teams that had successfully navigated the knockout stage. This match determined the World Cup champion and was held at the iconic International Stadium Yokohama. The final not only showcased the best of football talent but also brought together fans from around the world to witness the pinnacle of the sport.", "## Key Matches\n\n### Opening Match\nThe 2002 FIFA World Cup kicked off on June 3, 2002, with a thrilling opening match between Brazil and Turkey at the International Stadium in Yokohama. Brazil, one of the tournament favorites, showcased their attacking prowess, ultimately winning the match 2-1. This game set the tone for the tournament, highlighting Brazil's ambition to reclaim the title.\n\n### Quarterfinals\nThe quarterfinals featured some of the most intense matchups of the tournament. Notably, the clash between Brazil and Belgium was a highlight, where Brazil emerged victorious with a 2-0 win, thanks to goals from Ronaldo. This match solidified Brazil's status as a formidable contender, while Belgium's spirited performance earned them respect on the world stage.\n\n### Semifinals\nIn the semifinals, Brazil faced Turkey once again, this time in a high-stakes encounter. The match, held on June 26, 2002, saw Brazil dominate with a 1-0 victory, courtesy of a stunning goal from Ronaldo. This win propelled Brazil into the final, where they aimed to secure their fifth World Cup title.\n\n### Final\nThe grand finale took place on June 30, 2002, at the Yokohama International Stadium, where Brazil faced Germany. In a match that would go down in history, Brazil triumphed 2-0, with Ronaldo scoring both goals. This victory not only crowned Brazil as the World Cup champions but also marked Ronaldo's redemption, as he finished the tournament as the top scorer with eight goals.", '## Star Players\n\nThe 2002 FIFA World Cup in South Korea and Japan was a showcase of extraordinary talent, with several players standing out for their remarkable performances. Here, we highlight four of the tournament\'s star players who left an indelible mark on the competition.\n\n### Ronaldo\nRonaldo, often referred to as "O Fenômeno," was the standout player of the tournament. He scored a total of eight goals, including two in the final against Germany, leading Brazil to its fifth World Cup title. His incredible speed, skill, and finishing ability made him a nightmare for defenders, and his comeback from injury prior to the tournament added to the narrative of his success.\n\n### Zinedine Zidane\nZinedine Zidane was another key player in the 2002 World Cup, although his tournament was marred by a disappointing performance in the final. Nevertheless, Zidane\'s elegance on the ball and his ability to control the midfield were evident throughout the tournament. His leadership and vision were crucial in guiding France to the knockout stages, even if they ultimately fell short of defending their title.\n\n### Rivaldo\nRivaldo was instrumental in Brazil\'s success, contributing not only with goals but also with his playmaking abilities. He scored a stunning goal against Belgium in the quarter-finals and was pivotal in creating opportunities for his teammates. His technical skills and creativity made him one of the most exciting players to watch during the tournament.\n\n### Roberto Carlos\nRoberto Carlos, known for his powerful free kicks and defensive prowess, was a key figure in Brazil\'s backline. His ability to join the attack and contribute offensively, combined with his defensive skills, made him a vital player for the team. His famous free-kick against France in the 1997 Tournoi de France is still remembered as one of the greatest goals in football history, and he continued to showcase his talent in the 2002 World Cup.\n\nThese players not only excelled individually but also contributed to the rich tapestry of the tournament, making the 2002 FIFA World Cup a memorable event in football history.', "## Controversies\n\n### Refereeing Decisions\nThe 2002 FIFA World Cup was marred by several contentious refereeing decisions that drew widespread criticism. Notably, the officiating in matches involving South Korea, particularly against Italy in the quarter-finals, raised eyebrows. Key decisions, such as the disallowance of a legitimate Italian goal and the controversial red card issued to Francesco Totti, led many to question the impartiality of the referees. These incidents fueled speculation about potential biases and the overall quality of officiating during the tournament.\n\n### Match Fixing Allegations\nIn the aftermath of the tournament, allegations of match-fixing began to surface, particularly concerning the matches involving South Korea. Some analysts and commentators suggested that the South Korean team's unexpected success, which included victories over Italy and Spain, was too remarkable to be purely coincidental. These allegations were further exacerbated by the questionable officiating in those matches, leading to a cloud of suspicion that lingered over the tournament's integrity.\n\n### Fan Reactions\nThe controversies surrounding the 2002 World Cup elicited strong reactions from fans around the globe. Many supporters expressed their frustration and disbelief at the refereeing decisions, particularly those that seemed to favor the co-hosts. Social media and fan forums became hotbeds for discussions, with some fans calling for reforms in officiating standards. The emotional responses highlighted the passion and investment that fans have in the World Cup, as well as the potential for controversies to overshadow the spirit of the game.", "## Impact on Football\n\n### Growth of Football in Asia\nThe 2002 FIFA World Cup was a watershed moment for football in Asia, as it was the first time the tournament was held on the continent. The successful co-hosting by South Korea and Japan not only showcased the region's ability to host major sporting events but also ignited a passion for football among millions of fans. The tournament's popularity led to increased investment in grassroots programs and infrastructure, fostering a new generation of players and fans. As a result, Asian football associations began to prioritize the development of their leagues and national teams, leading to a more competitive landscape in international football.\n\n### Legacy of the Tournament\nThe legacy of the 2002 World Cup is multifaceted. It not only elevated the status of Asian football but also set a precedent for future tournaments in terms of organization and fan engagement. The event demonstrated the potential for football to unite diverse cultures and foster international camaraderie. Additionally, the tournament's memorable moments, such as South Korea's remarkable run to the semifinals, inspired a sense of pride and achievement across the continent. The success of the event has continued to influence how future World Cups are planned and executed, with an emphasis on inclusivity and global participation.\n\n### Changes in FIFA Regulations\nIn the aftermath of the 2002 World Cup, FIFA recognized the need for regulatory changes to enhance the integrity and competitiveness of the sport. The tournament highlighted issues such as match-fixing and the importance of fair play, prompting FIFA to implement stricter regulations and oversight mechanisms. These changes aimed to protect the sport's integrity and ensure that the focus remained on the athletes and their performances. Furthermore, the tournament's success led to discussions about expanding the World Cup format, ultimately influencing the structure of future tournaments."]
# )