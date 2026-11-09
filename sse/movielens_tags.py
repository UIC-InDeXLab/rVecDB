"""Draft grouping of the 1,128 MovieLens genome tags into SSE blocks: genre / tone / style / theme / other.

genre, tone, style are listed explicitly; "other" (excluded from training/evaluation) is names, awards,
quality judgments, franchises, places/eras and meta tags; everything left is "theme".
Writes data/movielens/tag_groups.csv  (tag, group)  — CHECK BY HAND and edit; the CSV is the source of truth.

Usage: .venv/bin/python -m sse.movielens_tags
"""
import csv
import re
from collections import Counter

from .awa2 import ROOT

GENRE = """action|adventure|animation|animated|anime|biographical|biography|biopic|black comedy|blaxploitation|
buddy movie|caper|cartoon|chick flick|comedy|coming of age|coming-of-age|costume drama|courtroom drama|crime|
cyberpunk|dark comedy|dark fantasy|disaster|documentary|drama|dystopia|distopia|epic|fairy tale|fairy tales|
fake documentary|family drama|fantasy|farce|film noir|gangster|gangsters|grindhouse|heist|high fantasy|
historical|horror|martial arts|kung fu|wuxia|mockumentary|modern fantasy|monster|murder mystery|musical|mystery|
neo-noir|noir|noir thriller|parody|period piece|post apocalyptic|post-apocalyptic|psychological|road movie|
romance|romantic comedy|satire|sci fi|sci-fi|science fiction|scifi|screwball|screwball comedy|sex comedy|slasher|
space opera|spaghetti western|splatter|spoof|sports|spy|steampunk|stand-up comedy|super hero|super-hero|
superhero|superheroes|suspense|swashbuckler|teen movie|thriller|tragedy|war movie|western|zombie|zombies|
slapstick|off-beat comedy|pulp|educational|british comedy|kids and family|family|disney animated feature|computer animation|
claymation|stop motion|stop-motion|short|silent|vampire|vampires|werewolf|werewolves|alien invasion|
haunted house|serial killer|prison escape|bank robbery|treasure hunt|car chase|gross-out|stoner movie"""

TONE = """absurd|affectionate|atmospheric|bittersweet|bizarre|bleak|brutal|campy|camp|cathartic|cheesy|claustrophobic|
compassionate|confrontational|corny|creepy|crude humor|cute|cynical|dark|dark humor|deadpan|depressing|
disturbing|downbeat|dramatic|dreamlike|earnest|eerie|emotional|enigmatic|erotic|exciting|feel good movie|
feel-good|forceful|frightening|fun|fun movie|funny|funny as hell|gloomy|goofy|grim|gritty|gruesome|
hallucinatory|happy ending|hard to watch|harsh|heartbreaking|heartwarming|hilarious|hillarious|humor|humorous|
inspirational|inspiring|intense|intimate|ironic|irreverent|light|lyrical|macabre|melancholic|melancholy|
meditative|moody|moving|nostalgic|nostalgia|ominous|over the top|paranoid|passionate|poignant|quirky|
reflective|ridiculous|romantic|sad|sappy|sarcasm|satirical|scary|sentimental|sexy|silly|silly fun|suspenseful|
sweet|tear jerker|tense|thought-provoking|touching|understated|upbeat|violent|visceral|weird|whimsical|wistful|
witty|strange|surreal|crazy|beautiful|cute!|gore|gratuitous violence|cool|entertaining|gory|goretastic|bloody|tense|uplifting|unsettling|sad but good|
dumb but funny|very funny|action packed|fast paced|slow|slow paced|talky|cerebral|intellectual|philosophical|
psychedelic|surrealism|magic realism|existentialism|eccentricity|zany|kick-butt women"""

STYLE = """3d|70mm|amazing cinematography|amazing photography|artistic|artsy|art house|awesome soundtrack|beautiful scenery|
beautifully filmed|black and white|cgi|bad cgi|cinematography|colourful|complex|complicated|complicated plot|
dialogue|dialogue driven|entirely dialogue|dynamic cgi action|effects|special effects|ensemble cast|flashbacks|
graphic design|great cinematography|great dialogue|great music|great soundtrack|good music|good soundtrack|
handycam|independent film|indie|multiple storylines|narrated|no dialogue|non-linear|nonlinear|
notable soundtrack|plot twist|twist|twist ending|twists & turns|surprise ending|alternate endings|
unusual plot structure|stylish|stylized|visual|visually appealing|visually stunning|visuals|stunning|scenic|
breathtaking|quotable|highly quotable|low budget|big budget|made for tv|long|too long|too short|
character study|storytelling|minimalist|fight scenes|sword fight|sword fighting|realistic action|
enormously long battle scene|explosions|music|soundtrack|tricky|predictable|non-hollywood ending|
powerful ending|great ending|bad ending|open ending|watch the credits|puppets|chase|gunfight|shootout|mindfuck"""

QUALITY = """awesome|awful|bad|bad acting|bad plot|bad science|bad script|bad sequel|better than expected|boring|
boring!|brilliant|bullshit history|clever|crappy sequel|disappointing|dumb|excellent|excellent script|
exceptional acting|good|good acting|good action|good dialogue|good romantic comedies|good sequel|good story|
great|great acting|great movie|guilty pleasure|horrible|idiotic|interesting|lame|masterpiece|not as good as the first|
not funny|original|original plot|overrated|perfect|plot|plot holes|pointless|pretentious|script|shallow|
so bad it's funny|so bad it's good|stupid|stupid as hell|stupidity|suprisingly clever|underrated|unfunny|
unintentionally funny|unique|unrealistic|very good|very interesting|waste of time|intelligent|book was better|
better than the american version|special|cult|cult classic|cult film|classic|criterion|free to download|
imdb top 250|movielens top pick|afi 100|afi 100 (laughs)|afi 100 (movie quotes)|best of 2005|best war films|
funniest movies|potential oscar nom|easily confused with other movie(s) (title)|oscar winner|oscar|
golden palm|pg|pg-13|story|honest|simple|confusing|intelligent sci-fi|realistic|unlikeable characters|
complex characters|forgettable|no plot|factual|controversial|entertaining|annoying|sequel|sequels|series|franchise|prequel|remake|remade|
trilogy|directorial debut|adaptation|literary adaptation|based on a book|based on book|based on a comic|
based on comic|based on a play|based on a tv show|based on a video game|video game adaptation|
comic book adaption|adapted from:book|adapted from:comic|adapted from:game|book|books|comic|comics|graphic novel|
foreign|scifi cult|product placement|gypsy accent|irish accent|nudity (full frontal - brief)|
nudity (full frontal - notable)|nudity (full frontal)|nudity (rear)|nudity (topless - brief)|
nudity (topless - notable)|nudity (topless)|notable nudity|male nudity|life|time|plot|great dialogue"""

NAMES = """007|007 (series)|aardman|aardman studios|almodovar|amy smart|arnold|author:alan moore|author:neil gaiman|
batman|beatles|bond|c.s. lewis|carrie-anne moss|chris tucker|coen bros|coen brothers|dc comics|depp & burton|
disney|dr. seuss|dreamworks|emma watson|ennio morricone|firefly|francis ford copolla|george orwell|gilliam|
hannibal lecter|harry potter|hitchcock|indiana jones|james bond|jane austen|jay and silent bob|king arthur|
kubrick|kurosawa|liv tyler|lynch|marvel|marx brothers|miyazaki|monty python|mozart|muppets|neil gaiman|
peter pan|philip k. dick|pixar|pixar animation|roald dahl|robert downey jr|robert ludlum|saturday night live|
shakespeare|sophia coppola|spielberg|spock|star trek|star wars|studio ghibli|tarantino|tolkien|tom clancy|
truman capote|view askew|mtv|criterion"""

PLACE_ERA = """18th century|1920s|1930s|1950s|1960s|1970s|1980s|19th century|80s|africa|alaska|alcatraz|antarctica|argentina|
australia|australian|berlin|boston|brazil|british|california|canada|chicago|china|cuba|east germany|egypt|
england|finnish|france|french|german|germany|hawaii|hong kong|india|iran|iraq|ireland|irish|israel|italian|
italy|japan|japanese|las vegas|latin america|london|los angeles|mexico|middle east|minnesota|new jersey|
new orleans|new york|new york city|new zealand|palestine|paris|poland|rio de janeiro|rome|russia|russian|
san francisco|scotland|south africa|south america|spain|spanish|swedish|texas|tokyo|vienna|bollywood|hollywood"""

AWARD = re.compile(r"^(oscar \(|saturn award)")


def split(s):
    return {t.strip() for t in s.replace("\n", "").split("|") if t.strip()}


def main():
    tags = [r["tag"] for r in csv.DictReader(open(ROOT / "data/movielens/ml-25m/genome-tags.csv"))]
    genre, tone, style = split(GENRE), split(TONE), split(STYLE)
    other = split(QUALITY) | split(NAMES) | split(PLACE_ERA)
    rows = []
    for t in tags:
        if AWARD.match(t) or t in other:
            g = "other"
        elif t in genre:
            g = "genre"
        elif t in tone:
            g = "tone"
        elif t in style:
            g = "style"
        else:
            g = "theme"
        rows.append((t, g))
    out = ROOT / "data/movielens/tag_groups.csv"
    with open(out, "w", newline="") as f:
        w = csv.writer(f); w.writerow(["tag", "group"]); w.writerows(rows)
    print("written", out, dict(Counter(g for _, g in rows)))
    unknown = (genre | tone | style) - set(tags)
    if unknown:
        print("listed but not genome tags (ignored):", sorted(unknown))


if __name__ == "__main__":
    main()
