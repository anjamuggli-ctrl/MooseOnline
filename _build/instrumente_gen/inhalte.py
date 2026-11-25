# Inhalte der Instrumente für drei Pädagogik-Themen.
# Jedes Instrument: (Kürzel, Dateiname, Titel, Kurzbeschreibung für die Website, Funktion)

# ======================================================================
# L.07 · Lernen und Digitalität
# ======================================================================
def di1(I):
    I.kicker(f"Instrument {I.nr}"); I.title("Planungsraster Klafki digital")
    I.sub("Eine Lerneinheit mit Klafkis Perspektivenschema begründen, neu gelesen unter den Bedingungen der Digitalität.")
    I.p("Klafkis sieben Fragen stehen in Wechselwirkung und haben keine feste Reihenfolge (Klafki, 2007, S. 270 f.). Grundlage ist die **Bedingungsanalyse**: Was bringen Lerngruppe und Lehrperson mit, welche Bedingungen der Schule gelten? Die rechte Spalte ergänzt jede Frage um eine Leitfrage zur Digitalität.")
    I.fields(["Fach, Klasse, Datum", "Thema der Einheit", "Bedingungen (Lerngruppe, Geräte, Zeit, Regeln)"])
    I.h2("Die sieben Fragen")
    I.grid(["Frage nach Klafki", "Leitfrage Digitalität", "Meine Antwort"], widths=[2300, 3300, 4038], height=900, body=[
        ["**1 Gegenwartsbedeutung**", "Wo begegnen die Lernenden dem Thema in Chats, Feeds, Games oder Suchmaschinen?", ""],
        ["**2 Zukunftsbedeutung**", "Was davon wird automatisiert, und was bleibt eine menschliche Aufgabe?", ""],
        ["**3 Exemplarische Bedeutung**", "Welches Konzeptwissen (nicht nur Produktwissen) lernen sie daran?", ""],
        ["**4 Thematische Struktur**", "Wo kommen Auswählen, Verbinden und Quellenprüfung in die Struktur?", ""],
        ["**5 Erweisbarkeit**", "Ist die Aufgabe noch aussagekräftig, wenn Internet und KI erlaubt sind? Wie werden Lernende an den Kriterien beteiligt?", ""],
        ["**6 Zugänglichkeit und Darstellbarkeit**", "Welche Kombination von Modi (Text, Bild, Ton, Simulation) öffnet Zugänge, und für wen schliesst sie welche?", ""],
        ["**7 Lehr-Lern-Prozess**", "Wo arbeiten die Lernenden gemeinsam, wo allein, wo mit, über oder trotz Medien?", ""]])
    I.h2("Folgerung für meine Planung")
    I.lines(3)
    I.source("Fragen nach Klafki, 2007, S. 270–284. Leitfragen: eigene Synthese mit Döbeli Honegger, 2016, und Krommer, 2018.")


def di2(I):
    I.kicker(f"Instrument {I.nr}"); I.title("Mit-über-trotz-Raster")
    I.sub("Prüfen, ob Medien in einer Einheit als Werkzeug, als Thema und als Herausforderung vorkommen.")
    I.p("Medien können **mit** (als Werkzeug), **über** (als Gegenstand der Reflexion) und **trotz** (als Herausforderung für Konzentration und Selbststeuerung) in den Unterricht kommen. Eine ausgewogene Einheit enthält alle drei Zugänge.")
    I.fields(["Einheit / Lektion", "Klasse, Datum"])
    I.grid(["Zugang", "Was die Lernenden konkret tun", "Ziel dahinter", "Dauer"], widths=[1900, 3700, 3000, 1038], height=1100, body=[
        ["**mit Medien**\nMedien als Werkzeug zum Lernen und Gestalten", "", "", ""],
        ["**über Medien**\nMedien, Daten, KI und Algorithmen als Thema", "", "", ""],
        ["**trotz Medien**\nAblenkung, Selbststeuerung, Pausen ohne Gerät", "", "", ""]])
    I.h2("Kurz geprüft")
    I.checklist(["Unterstützt jedes Tool ein klares Ziel, statt nur alte Ziele schneller zu erreichen?",
                 "Lernen die Lernenden ein Prinzip, das auch mit einem anderen Programm gilt?",
                 "Gibt es mindestens eine Phase, in der über die Medien selbst gesprochen wird?",
                 "Ist geplant, wie Ablenkung angesprochen und Selbststeuerung geübt wird?"])
    I.source("Zugänge mit, über und trotz Medien nach der Seite «Lernen und Digitalität» auf mugglionline.ch (Döbeli Honegger, 2016; Krommer, 2018).")


def di3(I):
    I.kicker(f"Instrument {I.nr}"); I.title("Tool-Check")
    I.sub("Ein digitales Werkzeug, eine App oder eine digitale Erklärhilfe vor dem Einsatz kriterienbasiert prüfen.")
    I.fields(["Name des Tools / der Erklärhilfe", "geplanter Einsatz (Fach, Ziel)", "geprüft von, Datum"])
    I.h2("1 · Qualität einer digitalen Erklärung")
    I.grid(["Kriterium", "erfüllt?", "Beobachtung / Beleg"], widths=[3600, 1500, 4538], height=470, body=[
        ["**fachlich korrekt**, wissenschaftlich gesichert", "☐ ja  ☐ nein", ""],
        ["**verständlich**, in zielgruppengerechter Sprache", "☐ ja  ☐ nein", ""],
        ["**multimodal**, mit mindestens zwei Modi", "☐ ja  ☐ nein", ""],
        ["**didaktisch sinnvoll**, vom Einfachen zum Komplexen", "☐ ja  ☐ nein", ""],
        ["**überprüfbar**, mit offengelegten Quellen", "☐ ja  ☐ nein", ""]])
    I.h2("2 · Prüfbereiche für Tools und Technologien")
    I.grid(["Prüfbereich", "Leitfrage", "Einschätzung"], widths=[1900, 4300, 3438], height=560, body=[
        ["**Lernziel**", "Welches Ziel unterstützt das Tool? Eröffnet es neue Ziele oder bedient es nur alte schneller?", ""],
        ["**Konzeptwissen**", "Lernen die Lernenden Prinzipien, die über dieses Produkt hinaus gelten?", ""],
        ["**Gerechtigkeit**", "Profitieren nur die Starken, oder auch jene, die mehr Unterstützung brauchen?", ""],
        ["**Daten und Macht**", "Wer erhebt welche Daten, wer setzt die Regeln, gibt es offene Alternativen?", ""],
        ["**Kontrolle oder Vertrauen**", "Überwacht das Tool vor allem, ob Lernende auf dem vorgegebenen Pfad bleiben?", ""]])
    I.box("Die Gegenfrage", "Passt sich das Tool dem Lernziel an, oder wird das Lernen dem Tool angepasst? (Krommer, 2024)")
    I.fields(["Entscheid:  ☐ einsetzen   ☐ mit Anpassungen einsetzen   ☐ nicht einsetzen", "Begründung"])
    I.source("Teil 1 nach Völker, 2026, S. 30. Teil 2: eigene Synthese nach Krommer, 2018, 2024, 2025a; Döbeli Honegger, 2016; Stalder, 2016.")


def di4(I):
    I.kicker(f"Instrument {I.nr}"); I.title("KI-Antwort prüfen")
    I.sub("Arbeitsblatt für Lernende: eine Antwort oder Rückmeldung einer KI kritisch prüfen, bevor sie verwendet wird.")
    I.fields(["Name, Datum", "Wofür habe ich die KI genutzt?", "Meine Frage (Prompt) an die KI"])
    I.h2("1 · Prüfen")
    I.grid(["Prüffrage", "Ja / Nein / Unsicher", "Wie habe ich das geprüft?"], widths=[4000, 1700, 3938], height=650, body=[
        ["Stimmt die Antwort fachlich? (mit Buch, Heft oder einer zweiten Quelle verglichen)", "", ""],
        ["Verstehe ich jeden Satz? Kann ich ihn in eigenen Worten erklären?", "", ""],
        ["Nennt die KI Quellen, und gibt es diese Quellen wirklich?", "", ""],
        ["Fehlt etwas Wichtiges, oder ist etwas erfunden?", "", ""],
        ["Passt die Antwort zu meiner Aufgabe und zu den Kriterien der Lehrperson?", "", ""]])
    I.h2("2 · Entscheiden")
    I.p("☐ Ich übernehme die Antwort mit Quellenangabe.   ☐ Ich übernehme nur einen Teil.   ☐ Ich verwerfe die Antwort.")
    I.h2("3 · Nachdenken")
    I.p("Was habe ich selbst gedacht, und was hat die KI beigetragen?")
    I.lines(2)
    I.p("Was würde ich beim nächsten Mal anders fragen?")
    I.lines(2)
    I.source("Kriterien angelehnt an Völker, 2026 (fachlich korrekt, verständlich, überprüfbar); Reflexion nach der Seite «Lernen und Digitalität» auf mugglionline.ch.")


def di5(I):
    I.kicker(f"Instrument {I.nr}"); I.title("Projektplaner in fünf Phasen")
    I.sub("Ein Projekt mit Produkt planen und die Gelenkstellen festlegen, an denen die Lehrperson begleitet.")
    I.p("Projektunterricht verbindet eine bedeutsame, lebensnahe Aufgabe mit planvoller, kooperativer Arbeit und einem sichtbaren **Produkt** (Konrad & Traub, 2021). Lernende werden oft allein gelassen und sind überfordert. Plane deshalb die **Gelenkstellen**, an denen du anleitest, nachfragst und Zwischenergebnisse sichtest.")
    I.fields(["Projektthema", "Themenfindung:  ☐ eng (Lehrplan)   ☐ halboffen (Rahmenthema)   ☐ offen", "Produkt (z. B. digitale Ausstellung, Podcast, Modell)", "Zeitrahmen"])
    I.grid(["Phase", "Was die Lernenden tun", "Gelenkstelle: was ich als Lehrperson tue", "Termin"], widths=[1900, 3300, 3300, 1138], height=900, body=[
        ["**1 Themenfindung**\nalle können das Thema akzeptieren", "", "", ""],
        ["**2 Information**\nVorwissen sammeln, recherchieren", "", "", ""],
        ["**3 Planung**\nAblauf, Ziele, Gruppen; revidierbar", "", "", ""],
        ["**4 Produktion**\nTeilaspekte wachsen zum Produkt", "", "", ""],
        ["**5 Abschluss**\nPräsentation und Reflexion", "", "", ""]])
    I.h2("Kultur der Digitalität im Projekt")
    I.checklist(["**Referentialität:** Die Lernenden wählen Material aus, verbinden es neu und geben Quellen an.",
                 "**Gemeinschaftlichkeit:** Es gibt ein gemeinsames Produkt, zu dem alle beitragen.",
                 "**Medienbildung:** Bildrechte, Einwilligungen und Datenschutz werden geklärt.",
                 "**Lernstrategien:** Die Lernenden wissen, was, wie und warum sie arbeiten."])
    I.source("Phasen nach Konrad & Traub, 2021, S. 149 f. (nach Frey, 2007; Gudjons, 1994; Traub, 2012a); Gelenkstellen nach Traub, 2012a; Kultur der Digitalität nach Stalder, 2016.")


def di6(I):
    I.kicker(f"Instrument {I.nr}"); I.title("Lernspiel-Check nach der HERZ-Theorie")
    I.sub("Prüfen, ob ein Lern- oder Computerspiel noch das bietet, was Spielen antreibt.")
    I.p("Nach Mogels HERZ-Theorie wird Spielen von **H**andlung, **E**rleben, **R**ealität und **Z**iel getragen. Wird ein Spiel zur Lernkontrolle mit Punkten und Noten, hat das Handeln Folgen ausserhalb des Spiels und die Ziele sind vorgegeben. Dann hört es oft auf zu motivieren.")
    I.fields(["Spiel / Game", "Einsatz (Fach, Klasse, Ziel)"])
    I.grid(["", "Prüffrage", "ja / teils / nein", "Anpassung"], widths=[600, 4400, 1500, 3138], height=900, body=[
        ["**H**", "**Handlung:** Dürfen Fehler im Spiel folgenlos bleiben, oder zählt jeder Fehler für die Note?", "", ""],
        ["**E**", "**Erleben:** Eröffnet das Spiel neue Erfahrungen, oder sammelt mensch nur Punkte?", "", ""],
        ["**R**", "**Realität:** Können die Lernenden zwischen Spiel und Wirklichkeit unterscheiden und darüber sprechen?", "", ""],
        ["**Z**", "**Ziel:** Dürfen die Lernenden eigene Ziele setzen und verändern?", "", ""]])
    I.h2("Nach dem Spielen")
    I.p("Wie wird das Gespielte mit dem Lernziel verbunden (Nachbesprechung, Transfer, Reflexion)?")
    I.lines(3)
    I.source("HERZ-Theorie nach Mogel, 2008, Kap. 7, S. 229–237; Prüffragen: eigene Anwendung. Zu Gamification: Döbeli Honegger, 2016, Kap. 4.")


def di7(I):
    I.kicker(f"Instrument {I.nr}"); I.title("Klassenvereinbarung digital")
    I.sub("Regeln für Geräte, Klassenchat und KI gemeinsam aushandeln, dazu eine Checkliste für sicheres Bedienen.")
    I.p("Normen der Kommunikation, etwa wer wen wann kontaktieren darf, haben sich gewandelt. Darum braucht es einen Dialog aller Beteiligten (Döbeli Honegger, 2016, S. 67). Regeln, die die Klasse selbst aushandelt, werden eher eingehalten.")
    I.fields(["Klasse, Datum", "beteiligt (Lernende, Lehrpersonen, SHP, Eltern)"])
    I.h2("Unsere Vereinbarung")
    I.grid(["Bereich", "Das gilt bei uns", "Warum?"], widths=[2200, 4400, 3038], height=800, body=[
        ["**Geräte im Unterricht**\nwann offen, wann zu?", "", ""],
        ["**Klassenchat**\nZeiten, Ton, Bilder von anderen", "", ""],
        ["**KI und Internet**\nwofür erlaubt, wie angeben?", "", ""],
        ["**Fotos und Videos**\nnur mit Einwilligung", "", ""],
        ["**Wenn etwas schiefläuft**\nan wen wende ich mich?", "", ""]])
    I.h2("Sicher bedienen: Checkliste")
    I.checklist(["Anmeldung, sichere Passwörter und Zwei-Faktor-Anmeldung sind eingeübt.",
                 "Alle wissen, wo sie was speichern und wer Zugriff hat.",
                 "Das Teilen von Dokumenten wird bewusst eingestellt.",
                 "Plan B für Ausfälle: Updates, Akku, Kabel, Ersatzgerät, Aufgabe ohne Gerät.",
                 "Bei jedem neuen Tool wird zuerst das Konzept gezeigt, dann die Klickfolge."])
    I.fields(["Überprüfen der Vereinbarung am"], 3600)
    I.source("Checkliste: eigene Zusammenstellung, gestützt auf Döbeli Honegger, 2016, Kap. 5. Beteiligte nach Kompetenzbeschreibung L.07.")


def di8(I):
    I.kicker(f"Instrument {I.nr}"); I.title("Planungs-Check Digitalität")
    I.sub("Acht Fragen für die Planung oder Rückschau einer Lerneinheit unter den Bedingungen der Digitalität.")
    I.fields(["Einheit / Lektion", "Klasse, Datum"])
    I.checklist(["**1 Bedeutung:** Habe ich geklärt, wo das Thema im digitalen Alltag der Lernenden vorkommt und was davon künftig automatisiert wird?",
                 "**2 Ziel vor Tool:** Ist klar, welches Ziel ein Tool unterstützt, und eröffnet es neue Ziele statt nur alte schneller zu erreichen?",
                 "**3 Höhere Stufen:** Verlangen die Aufgaben Auswählen, Vergleichen und Beurteilen, nicht nur Wiedergeben?",
                 "**4 Mit, über, trotz:** Kommen Medien als Werkzeug, als Thema und als Herausforderung für die Selbststeuerung vor?",
                 "**5 Konzeptwissen:** Lernen die Lernenden Prinzipien, die über das konkrete Produkt hinaus gelten?",
                 "**6 Qualität geprüft:** Habe ich externe Medien und KI-Ausgaben fachlich und didaktisch vollständig geprüft?",
                 "**7 Gemeinsam:** Gibt es Phasen, in denen Lernende zusammen etwas herstellen und Regeln aushandeln?",
                 "**8 Reflexion:** Sprechen wir darüber, was Medien und KI mit unserem Denken, unserer Identität und unseren Daten machen?"])
    I.h2("Eine Sache, die ich ändere")
    I.lines(3)
    I.tip("Tipp für Praktika: Ändere nur eine Sache, etwa eine Aufgabe eine Taxonomiestufe höher oder ein kurzes Gespräch über die Quelle, und beobachte, was sich verändert.")
    I.source("Eigene Synthese aus den Quellen der Seite «Lernen und Digitalität» (Klafki, 2007; Döbeli Honegger, 2016; Krommer, 2018; Stalder, 2016; Völker, 2026).")


DIG = ("Lernen und Digitalität", "digitalitaet", "Instrumente_Lernen_und_Digitalitaet", [
    ("DI1_Planungsraster-Klafki-digital", "Planungsraster Klafki digital", "Klafkis sieben Fragen mit je einer Leitfrage zur Digitalität und Platz für die eigene Planung.", di1),
    ("DI2_Mit-ueber-trotz-Raster", "Mit-über-trotz-Raster", "Prüft, ob Medien als Werkzeug, als Thema und als Herausforderung vorkommen, mit Kurz-Check.", di2),
    ("DI3_Tool-Check", "Tool-Check", "Fünf Qualitätskriterien für digitale Erklärungen und fünf Prüfbereiche für Tools, mit Entscheid.", di3),
    ("DI4_KI-Antwort-pruefen", "KI-Antwort prüfen", "Arbeitsblatt für Lernende: eine KI-Antwort prüfen, entscheiden und über den eigenen Anteil nachdenken.", di4),
    ("DI5_Projektplaner", "Projektplaner in fünf Phasen", "Phasen, Gelenkstellen der Lehrperson und ein Check zur Kultur der Digitalität im Projekt.", di5),
    ("DI6_Lernspiel-Check-HERZ", "Lernspiel-Check nach der HERZ-Theorie", "Vier Fragen zu Handlung, Erleben, Realität und Ziel, um ein Lernspiel zu prüfen.", di6),
    ("DI7_Klassenvereinbarung-digital", "Klassenvereinbarung digital", "Regeln zu Geräten, Klassenchat, KI und Fotos aushandeln, dazu eine Checkliste für sicheres Bedienen.", di7),
    ("DI8_Planungs-Check", "Planungs-Check Digitalität", "Die acht Fragen des Planungs-Checks zum Ausdrucken, mit Platz für eine Änderung.", di8)])


# ======================================================================
# B.04 · Lernende in Beurteilungsprozesse involvieren
# ======================================================================
def be1(I):
    I.kicker(f"Instrument {I.nr}"); I.title("Kriterien-Werkstatt")
    I.sub("Erfolgskriterien mit der Klasse an Beispielen erarbeiten, statt sie nur an die Wandtafel zu schreiben.")
    I.p("Kriterien werden erst verständlich, wenn Lernende sie an Beispielen entdecken, diskutieren und auf die eigene Arbeit anwenden (Lötscher et al., 2023, S. 62 f.). Die Beispiele müssen nicht perfekt sein.")
    I.fields(["Aufgabe / Produkt", "Lernziel", "Klasse, Datum"])
    I.h2("1 · Beispiele vergleichen")
    I.grid(["Beispiel", "Was gelingt hier? (konkret)", "Was fehlt noch?"], widths=[1600, 4100, 3938], height=760, first_col=["A", "B", "C"])
    I.h2("2 · Kriterien in unserer Sprache")
    I.grid(["Kriterium", "Woran sieht mensch es? (Beleg)"], widths=[4000, 5638], height=520, rows=5, sand_first=False)
    I.h2("3 · Anwenden")
    I.checklist(["Die Lernenden prüfen ihre eigene Arbeit mit den Kriterien, bevor sie abgeben.",
                 "Die Kriterien hängen sichtbar im Zimmer oder liegen der Aufgabe bei.",
                 "Wenn summativ beurteilt wird, wissen alle, was geprüft wird und nach welchen Kriterien."], cols=("Nächste Schritte", "✓"))
    I.source("Nach Lötscher et al., 2023, S. 62–66 (nach Wiliam, 2018); Transparenz als Fairness nach Fraefel, 2023.")


def be2(I):
    I.kicker(f"Instrument {I.nr}"); I.title("Qualitätensuche")
    I.sub("Arbeiten zuerst nach Gelungenem statt nach Fehlern durchsuchen und daraus Kriterien für alle gewinnen.")
    I.p("Winter schlägt vor, Arbeiten offen durchzulesen, gelungene Stellen zu markieren und sie aus dem Konzept der Autorin oder des Autors heraus zu verstehen. Was Lehrpersonen so üben, können auch Lernende an fremden und eigenen Arbeiten lernen.")
    I.fields(["Arbeit von", "gelesen von, Datum"])
    I.h2("Drei Schritte")
    I.bullets(["**Offen durchlesen** und gelungene Stellen markieren (noch nicht korrigieren).",
               "**Genauer anschauen:** Was genau ist an dieser Stelle gelungen?",
               "**Verstehen:** Was wollte die Autorin oder der Autor erreichen?"])
    I.grid(["Gelungene Stelle (Seite, Zeile)", "Was ist daran gelungen?", "Daraus wird ein Kriterium"], widths=[2600, 3600, 3438], height=900, rows=4, sand_first=False)
    I.h2("Neue Kriterien für die ganze Klasse")
    I.lines(3)
    I.source("Nach Winter, 2018, Kap. 12, S. 194–196; Übertragung auf Lernende: eigene Synthese.")


def be3(I):
    I.kicker(f"Instrument {I.nr}"); I.title("Selbstbeurteilung nach einer grösseren Arbeit")
    I.sub("Für Referate, Projekte oder Facharbeiten: über Vorgehen, Lerneffekt und Leistung nachdenken und eine Bitte formulieren.")
    I.fields(["Name", "Arbeit / Projekt", "Datum"])
    I.grid(["Block", "Leitfragen", "Meine Antwort"], widths=[1900, 3500, 4238], height=1100, body=[
        ["**1 Erarbeitung**", "Welches Material habe ich genutzt? Wie viel Zeit? Wie bin ich vorgegangen? Wer hat mich unterstützt?", ""],
        ["**2 Lerneffekt**", "Was habe ich fachlich gelernt? Was über meine Arbeitsweise?", ""],
        ["**3 Eigene Bewertung**", "Was sind Stärken und Schwächen meiner Arbeit? Welche Informationen fehlen noch?", ""],
        ["**4 Hintergründe**", "Welche Fähigkeiten haben mir geholfen? Wo will ich mich weiterentwickeln?", ""],
        ["**5 Bitte an die Lehrperson**", "Wozu wünsche ich mir eine Rückmeldung?", ""]])
    I.box("Drei Arten des Nachdenkens", "**Lernreflexion:** Wie bin ich vorgegangen, was hat geholfen? · **Leistungsreflexion:** Wie weit habe ich die Ziele erreicht? · **Selbstreflexion:** Was gelingt mir bei solchen Arbeiten gut?")
    I.source("Fünf Blöcke nach Winter, 2018, Abb. 8.13 (leicht verändert aus Winter, Schwarz & Volkwein, 2008); Reflexionsarten nach Winter, 2018, Abb. 8.7, S. 114 f.")


def be4(I):
    I.kicker(f"Instrument {I.nr}"); I.title("Peer-Feedback in sieben Schritten")
    I.sub("Einander eine schriftliche Rückmeldung geben, die beim Überarbeiten hilft, nicht beim Benoten.")
    I.p("Beim Peer-Feedback geht es um **gegenseitige Unterstützung**. Ohne Anleitung urteilen Lernende oft sehr hart, darum helfen Regeln und Satzanfänge.")
    I.fields(["Feedback von", "für", "Aufgabe, Datum"])
    I.grid(["Min.", "Schritt", "✓"], widths=[900, 7700, 1038], height=420, body=[
        ["3", "die Arbeit des Peers lesen", "☐"], ["1", "überlegen, ob eine Klärungsfrage nötig ist", "☐"],
        ["2", "Klärungsfragen gegenseitig stellen und beantworten", "☐"], ["2", "Feedback schreiben (unten)", "☐"],
        ["1", "erhaltenes Feedback lesen", "☐"], ["1", "Rückfragen zum Feedback stellen", "☐"],
        ["5", "das Feedback für die Überarbeitung nutzen", "☐"]])
    I.h2("Mein Feedback")
    I.grid(["Satzanfang", "Meine Rückmeldung"], widths=[3200, 6438], height=900, body=[
        ["Ich finde gut, wie du …", ""], ["Nicht verstanden habe ich …", ""], ["Mein Tipp für dich …", ""]])
    I.checklist(["Mein Feedback bezieht sich auf die Kriterien der Aufgabe.", "Ich beschreibe konkrete Stellen statt allgemeine Urteile.", "Ich bin freundlich und ehrlich."], cols=("Selbst-Check", "✓"))
    I.source("Sieben Schritte nach Lötscher et al., 2023, S. 76 (nach Wiliam & Leahy, 2015, S. 147); Satzanfänge nach Lötscher et al., 2023, S. 74–76.")


def be5(I):
    I.kicker(f"Instrument {I.nr}"); I.title("Portfolio-Planer")
    I.sub("Eine Portfolioarbeit so planen, dass die Lernenden an Auswahl, Kriterien und Reflexion beteiligt sind.")
    I.p("Ein Portfolio ist eine zielgerichtete Sammlung von Arbeiten, die Bemühungen, Fortschritte und Leistungen zeigt. Die Lernenden sind an der Auswahl, an den Auswahl- und Beurteilungskriterien beteiligt und reflektieren ihre Arbeit (Winter, 2018, S. 174).")
    I.fields(["Portfolio-Typ:  ☐ Projektportfolio   ☐ Kurs- und Fachportfolio   ☐ Lern-Entwicklungs-Portfolio", "Zeitraum", "Zweck:  ☐ formativ (Lernen begleiten)   ☐ summativ (Teil der Beurteilung)"])
    I.grid(["Schritt", "Was wird vereinbart oder getan?", "Wer entscheidet mit?"], widths=[2400, 4900, 2338], height=800, body=[
        ["**Rahmen vereinbaren**", "", ""], ["**Belege auswählen**\nAuswahlkriterien", "", ""],
        ["**Reflektieren**\nzu jedem Beleg", "", ""], ["**Rückmeldung**\nPeers, Lehrperson", "", ""],
        ["**Präsentieren**", "", ""], ["**Beurteilen**\nKriterien", "", ""]])
    I.h2("Reflexion zu einem Beleg (für Lernende)")
    I.fields(["Warum habe ich diesen Beleg ausgewählt?", "Was zeigt er über mein Lernen?", "Was würde ich heute anders machen?"], 3600)
    I.tip("Vorsicht: Als «Allheilmittel» rasch für alle eingeführt, haben Portfolios wenig Erfolg. Klein beginnen, etwa mit einem Projektportfolio (Winter, 2018, S. 175 f.).")
    I.source("Nach Winter, 2018, Kap. 11, S. 174–176 (Abb. 11.1, aus Winter, 2012b); Lötscher et al., 2023, S. 72 f.")


def be6(I):
    I.kicker(f"Instrument {I.nr}"); I.title("Rückmeldebogen Präsentation")
    I.sub("Peers oder die Lehrperson beobachten einen Vortrag gezielt und geben eine ausformulierte Rückmeldung.")
    I.p("Präsentationen sind flüchtig. Darum lohnt es sich, vorab Personen mit der Beobachtung zu beauftragen. Wer solche Bögen für andere ausfüllt, gewinnt Kriterien für die eigenen Vorträge.")
    I.fields(["Präsentation von", "Thema", "Rückmeldung von, Datum"])
    I.grid(["Bereich", "Das ist gelungen", "Das könntest du verbessern"], widths=[2400, 3619, 3619], height=900, body=[
        ["**Ablauf**\nEinleitung, Hauptteil, Schluss", "", ""],
        ["**Informationsgehalt**\nInhalt, Quellen", "", ""],
        ["**Vortrag**\nSprache, Ansprache, Körpersprache, Auftreten", "", ""],
        ["**Mediennutzung**\nFolien, Bilder, Objekte", "", ""]])
    I.h2("Abschliessende Stellungnahme und Tipp")
    I.lines(3)
    I.source("Nach Winter, 2018, Abb. 13.2, S. 207, und Kap. 13, S. 207 f.")


def be7(I):
    I.kicker(f"Instrument {I.nr}"); I.title("Lernkontrolle anpassen")
    I.sub("Eine Lernkontrolle für heterogene Lernvoraussetzungen planen und dabei fair bleiben.")
    I.fields(["Fach, Klasse", "Lernkontrolle zu", "Funktion:  ☐ formativ (unbenotet)   ☐ summativ"])
    I.h2("1 · Was kann angepasst werden?")
    I.grid(["Möglichkeit", "für wen / wie", "vereinbart mit"], widths=[3400, 3800, 2438], height=500, body=[
        ["☐ Lernziel oder Anspruchsniveau", "", ""], ["☐ Stoffumfang", "", ""], ["☐ Lernzeit oder Zeitpunkt (Anmeldung, wenn bereit)", "", ""],
        ["☐ Form (schriftlich, mündlich, Produkt) bei gleichen Kriterien", "", ""], ["☐ Hilfsmittel", "", ""], ["☐ zweite Chance nach gezieltem Üben", "", ""]])
    I.h2("2 · Fair bleiben")
    I.checklist(["**Objektivität:** keine Bevorzugung, keine Zufälligkeiten",
                 "**Transparenz:** Verfahren und Zweck sind allen bekannt",
                 "**Reliabilität:** gleiche Kriterien für alle",
                 "**Validität:** es wird nur geprüft, was vereinbart wurde",
                 "Angepasste Lernziele sind offen vereinbart und dokumentiert (kantonale Vorgaben).",
                 "Die SHP ist in die Planung einbezogen."])
    I.h2("3 · Vorher selbst einschätzen (für Lernende)")
    I.fields(["Diese Aufgaben sind für mich leicht:", "Diese Aufgaben sind für mich schwer:", "Das übe ich noch:"], 3200)
    I.source("Fairness-Grundsätze nach Fraefel, 2023, S. 146; Differenzierung und SHP nach Marti & Camenisch, 2018; Anpassungsideen angelehnt an Fraefel, 2023; Ruf & Gallin, 2011; Winter, 2018.")


def be8(I):
    I.kicker(f"Instrument {I.nr}"); I.title("Beurteilungs-Check")
    I.sub("Acht Fragen, um eine Unterrichtseinheit auf die Beteiligung der Lernenden an der Beurteilung zu prüfen.")
    I.fields(["Einheit / Lektion", "Klasse, Datum"])
    I.checklist(["**1 Funktion klar:** Wissen die Lernenden bei jeder Aufgabe, ob sie formativ (Übungsraum) oder summativ (Bilanz) ist?",
                 "**2 Kriterien verstanden:** Haben die Lernenden die Erfolgskriterien an Beispielen erarbeitet oder mitformuliert?",
                 "**3 Eigene Ziele:** Können die Lernenden eigene Kriterien oder Nahziele setzen und über das Erwartete hinausgehen?",
                 "**4 Selbstbeurteilung:** Gibt es angeleitete Momente der Lern-, Leistungs- und Selbstreflexion mit Folgerungen fürs Weiterlernen?",
                 "**5 Peer-Feedback:** Ist Peer-Feedback angeleitet, mit Regeln oder Satzanfängen, und dient es der Unterstützung statt der Benotung?",
                 "**6 Anpassung:** Können Lernkontrollen in Zeitpunkt, Form oder Umfang angepasst werden, bei transparenten und fairen Kriterien?",
                 "**7 Echte Mitbestimmung:** Ist klar, worüber die Lernenden mitentscheiden und worüber nicht, sodass keine Pseudopartizipation entsteht?",
                 "**8 Gesamtbeurteilung:** Stützt sich die Note auf ein Mosaik vielfältiger Belege, einschliesslich der Selbstbeurteilung, statt auf einen Mittelwert?"])
    I.h2("Eine Sache, die ich ändere")
    I.lines(3)
    I.tip("Tipp für Praktika: Entwickle eine Aufgabe mit der Klasse zu einer Single-Point-Rubric weiter (Instrument LA4 auf der Seite «Lernen analysieren») und vergleiche danach Selbst-, Peer- und deine Einschätzung.")
    I.source("Eigene Synthese aus den Quellen der Seite «Beurteilung» (Winter, 2018; Lötscher et al., 2023; Fraefel, 2023; Fluckiger, 2010).")


BEU = ("Lernende in Beurteilungsprozesse involvieren", "beurteilung", "Instrumente_Beurteilung", [
    ("BE1_Kriterien-Werkstatt", "Kriterien-Werkstatt", "Erfolgskriterien mit der Klasse an Beispielen erarbeiten, in eigener Sprache festhalten und anwenden.", be1),
    ("BE2_Qualitaetensuche", "Qualitätensuche", "Arbeiten nach Gelungenem durchsuchen und daraus Kriterien für alle gewinnen.", be2),
    ("BE3_Selbstbeurteilung", "Selbstbeurteilung nach einer grösseren Arbeit", "Fünf Blöcke von der Erarbeitung bis zur Bitte an die Lehrperson, mit drei Reflexionsarten.", be3),
    ("BE4_Peer-Feedback", "Peer-Feedback in sieben Schritten", "Ablauf mit Zeitangaben, Satzanfänge für die Rückmeldung und ein Selbst-Check.", be4),
    ("BE5_Portfolio-Planer", "Portfolio-Planer", "Portfolio-Typ, Zweck und Mitbestimmung in jedem Schritt planen, mit Reflexion zu einem Beleg.", be5),
    ("BE6_Rueckmeldebogen-Praesentation", "Rückmeldebogen Präsentation", "Gezielte Beobachtung von Ablauf, Inhalt, Vortrag und Mediennutzung, mit Tipp.", be6),
    ("BE7_Lernkontrolle-anpassen", "Lernkontrolle anpassen", "Anpassungsmöglichkeiten planen, Fairness-Grundsätze prüfen und Lernende selbst einschätzen lassen.", be7),
    ("BE8_Beurteilungs-Check", "Beurteilungs-Check", "Die acht Fragen des Beurteilungs-Checks zum Ausdrucken, mit Platz für eine Änderung.", be8)])


# ======================================================================
# Umgang mit Konflikten, Gewalt und Mobbing
# ======================================================================
def ko1(I):
    I.kicker(f"Instrument {I.nr}"); I.title("Konflikt oder Mobbing? Einschätzungsbogen")
    I.sub("Eine Situation anhand der Merkmale von Mobbing einschätzen, bevor gehandelt wird.")
    I.p("Mobbing liegt vor, wenn die folgenden Merkmale **gemeinsam** zutreffen. Ein Konflikt unter gleich Starken, ein Tobspiel oder ein einzelner Vorfall ist (noch) kein Mobbing, braucht aber trotzdem Aufmerksamkeit.")
    I.fields(["Betroffene Person (Kürzel), Klasse, Zyklus", "Beobachtet von, Zeitraum"])
    I.grid(["Merkmal", "trifft zu?", "Beobachtung (beschreiben, nicht deuten)"], widths=[3300, 1700, 4638], height=750, body=[
        ["**Kräfteungleichgewicht:** Die betroffene Person ist unterlegen (körperlich, zahlenmässig, sozial).", "☐ ja  ☐ nein  ☐ unklar", ""],
        ["**Häufigkeit:** Die Angriffe sind systematisch, etwa wöchentlich.", "☐ ja  ☐ nein  ☐ unklar", ""],
        ["**Dauer:** Sie ziehen sich über Wochen oder Monate hin.", "☐ ja  ☐ nein  ☐ unklar", ""],
        ["**Kein Ausweg:** Die Person kann es nicht aus eigener Kraft beenden.", "☐ ja  ☐ nein  ☐ unklar", ""],
        ["**Ausschluss:** Ziel ist, die Person aus der Gemeinschaft zu drängen.", "☐ ja  ☐ nein  ☐ unklar", ""],
        ["**Digital:** Es gibt auch Angriffe in Chats, Games oder sozialen Medien.", "☐ ja  ☐ nein  ☐ unklar", ""]])
    I.fields(["Einschätzung:  ☐ Konflikt   ☐ einzelne Gewalthandlung   ☐ Verdacht auf Mobbing   ☐ Mobbing", "Nächster Schritt, wer, bis wann"])
    I.box("Merke", "Bei Verdacht auf Mobbing handeln Erwachsene. «Die Kinder sollen das selbst lösen» ist bei Mobbing ein gefährlicher Mythos (Alsaker, 2012).")
    I.source("Merkmale nach Jannan, 2010, und Walker et al., 2026, Kap. 8.1; Abgrenzung nach Schubarth, 2020, S. 36–38.")


def ko2(I):
    I.kicker(f"Instrument {I.nr}"); I.title("Beobachtungsprotokoll Gruppe und Pause")
    I.sub("Vorfälle über mehrere Tage beschreiben und festhalten, wer welche Rolle einnimmt.")
    I.p("Mobbing ist ein **Gruppenphänomen**. In über 85 % der Fälle gibt es Zuschauende. Halte deshalb nicht nur fest, was zwischen zwei Kindern passiert, sondern auch, wie die anderen reagieren. Erwachsene bemerken Vorfälle oft nicht: Beobachte bewusst Pause, Garderobe, Schulweg und, wo möglich, den Klassenchat.")
    I.grid(["Datum, Ort", "Was ist passiert? (beschreiben)", "Wer war beteiligt und wie?"], widths=[1700, 4300, 3638], height=1000, rows=5, sand_first=False)
    I.h2("Rollen in der Gruppe (Kürzel eintragen)")
    I.grid(["Rolle", "Kürzel", "Rolle", "Kürzel"], widths=[2800, 2019, 2800, 2019], height=600, body=[
        ["**Mobbende**\nergreifen die Initiative", "", "**Verteidigende**\nstellen sich auf die Seite der Betroffenen", ""],
        ["**Assistierende**\nmachen aktiv mit", "", "**Aussenstehende**\nhalten sich heraus", ""],
        ["**Verstärkende**\nschauen zu, lachen, feuern an", "", "**Betroffene**", ""]])
    I.h2("Was ich daraus schliesse")
    I.lines(2)
    I.source("Rollen nach Salmivalli et al., 1996, zit. in Hauser et al., 2009, und Walker et al., 2026, Kap. 8.1.")


def ko3(I):
    I.kicker(f"Instrument {I.nr}"); I.title("Klassenregeln gegen Mobbing erarbeiten")
    I.sub("Mit der Klasse Regeln und Konsequenzen aushandeln, angepasst an Zyklus 1, 2 oder 3.")
    I.p("Wo Kinder klare Haltungen und Grenzen von Erwachsenen erleben, gibt es weniger Mobbing (Alsaker, 2012). Regeln, die die Klasse selbst erarbeitet, werden eher mitgetragen. Die Lehrperson setzt sie **konsequent und wertschätzend** durch (Schubarth, 2020).")
    I.fields(["Klasse, Zyklus, Datum", "Einstieg (Geschichte, Bilderbuch, Filmsequenz, Fall)"])
    I.h2("Unsere Regeln")
    I.grid(["Regel (positiv formuliert)", "Was tun wir, wenn jemand sie bricht?"], widths=[5000, 4638], height=800, rows=4, sand_first=False)
    I.h2("Wenn ich sehe, dass jemand geplagt wird")
    I.grid(["Zyklus", "Was die Kinder und Jugendlichen konkret tun können"], widths=[1800, 7838], height=800, body=[
        ["**Zyklus 1**", "«Stopp» sagen, das Kind zu sich holen, sofort eine erwachsene Person holen."],
        ["**Zyklus 2**", "Nicht mitlachen, sich zu zweit oder zu dritt dazustellen, es der Lehrperson oder im Klassenrat sagen."],
        ["**Zyklus 3**", "Nicht weiterleiten, Screenshots sichern, Hilfe holen (Lehrperson, Schulsozialarbeit, Beratung 147), sich öffentlich solidarisch zeigen."]])
    I.fields(["Regeln überprüfen am"], 3200)
    I.source("Eigene Synthese nach Alsaker, 2012; Schubarth, 2020, Tab. 7 und 8; Hauser et al., 2009; Walker et al., 2026.")


def ko4(I):
    I.kicker(f"Instrument {I.nr}"); I.title("No Blame Approach: Leitfaden")
    I.sub("Mobbing lösungsorientiert und ohne Schuldzuweisung in drei Schritten auflösen.")
    I.p("Der No Blame Approach verzichtet auf Schuldzuweisung und Strafe. Der Hergang wird nicht rekonstruiert. Die Lernenden werden als Expertinnen und Experten für ihre Klasse angesprochen. Bei Gewalt- oder Straftaten gelten trotzdem klare Konsequenzen.")
    I.h2("Schritt 1 · Gespräch mit der betroffenen Person")
    I.bullets(["Vertrauen aufbauen, das Vorgehen erklären, keine Details des Mobbings erfragen.", "Nach den Gefühlen fragen.", "Gemeinsam überlegen: Wer mobbt, wer schaut zu, wer könnte helfen?"])
    I.fields(["Datum", "Wie geht es der Person?", "Namen für die Unterstützungsgruppe"])
    I.h2("Schritt 2 · Treffen der Unterstützungsgruppe (ohne die betroffene Person)")
    I.bullets(["6 bis 8 Kinder oder Jugendliche: etwa zur Hälfte Mobbende und Mitlaufende (inkl. Anführende), zur Hälfte hilfsbereite Neutrale.",
               "Einladung ohne Nennung des Grundes; Treffen von etwa 45 Minuten während der Unterrichtszeit.",
               "Sagen, dass es der Person schlecht geht, ohne Schuld zuzuweisen. Keine Warum-Fragen.",
               "Ideen sammeln: «Was kannst du tun, damit es ihr oder ihm besser geht?» Die Verantwortung der Gruppe übergeben."])
    I.grid(["Name", "Idee, was sie oder er tun will"], widths=[2600, 7038], height=440, rows=6, sand_first=False)
    I.h2("Schritt 3 · Nachgespräche (nach etwa 1 bis 2 Wochen)")
    I.grid(["Datum", "mit wem", "Wie hat es sich entwickelt?"], widths=[1600, 2600, 5438], height=560, rows=3, sand_first=False)
    I.tip("Was nicht funktioniert, wird durch etwas anderes ersetzt. Schubarth hält den Ansatz für besonders geeignet für die Grundschule (Zyklus 1 und 2).")
    I.source("Nach Blum & Beck, 2019 und 2024; Schubarth, 2020, S. 186–188.")


def ko5(I):
    I.kicker(f"Instrument {I.nr}"); I.title("Interventionsplan bei Mobbing")
    I.sub("Das Vorgehen in einem konkreten Fall planen, dokumentieren und mit den Beteiligten abstimmen.")
    I.p("Für jeden Fall gilt: einzeln analysieren und methodisch vorgehen. Ein Handlungsleitfaden der Schule klärt, wann wie interveniert wird und wer zusammenarbeitet (Walker et al., 2026, Kap. 8.4).")
    I.fields(["Fall (Kürzel), Klasse, Zyklus", "Phase:  ☐ Testphase   ☐ Konsolidierung   ☐ Manifestation", "Fallverantwortliche Person"])
    I.h2("1 · Schutz zuerst")
    I.checklist(["Die betroffene Person ist informiert und weiss, an wen sie sich wenden kann.", "Sofortmassnahmen zum Schutz sind getroffen (Aufsicht, Sitzplatz, Pausen, Schulweg).", "Bei Drohungen, Gewalt oder sexuellen Übergriffen sind Schulleitung und wenn nötig Polizei informiert."])
    I.h2("2 · Massnahmen")
    I.grid(["Massnahme", "wer", "bis wann", "erledigt"], widths=[4800, 2000, 1600, 1238], height=600, body=[
        ["Gespräch mit der betroffenen Person", "", "", "☐"], ["Unterstützungsgruppe / Gespräch mit Mobbenden", "", "", "☐"],
        ["Arbeit mit der Klasse (Regeln, Rollen, Zivilcourage)", "", "", "☐"], ["Eltern der betroffenen Person informieren", "", "", "☐"],
        ["Eltern der Mobbenden informieren", "", "", "☐"], ["Schulsozialarbeit / Schulpsychologie beiziehen", "", "", "☐"], ["Nachgespräch, Überprüfung", "", "", "☐"]])
    I.h2("3 · Dokumentation")
    I.grid(["Datum", "Ereignis / Gespräch / Ergebnis"], widths=[1600, 8038], height=600, rows=5, sand_first=False)
    I.box("Was schadet", "Mobbende und Betroffene unvorbereitet konfrontieren · ein Kind vor der Klasse blossstellen · die betroffene Person in eine andere Klasse versetzen, ausser in Ausnahmefällen.")
    I.source("Nach Walker et al., 2026, Kap. 8.4–8.5; Schubarth, 2020, S. 135–139 (Phasen Tab. 9); Alsaker, 2012, Kap. 6.")


def ko6(I):
    I.kicker(f"Instrument {I.nr}"); I.title("Elterngespräch bei Mobbing vorbereiten")
    I.sub("Ein Gespräch mit Eltern von betroffenen oder mobbenden Kindern ruhig und lösungsorientiert vorbereiten.")
    I.p("Eltern sollen wissen, dass die Schule Mobbing nicht toleriert und Vorfälle begleitet. Eltern brauchen Unterstützung, nicht Schuldzuweisung (Alsaker, 2012). Schwerpunkt sind gemeinsame Lösungen (Schubarth, 2020).")
    I.fields(["Gespräch mit Eltern von", "Rolle des Kindes:  ☐ betroffen   ☐ mobbend   ☐ beteiligt", "Datum, Teilnehmende"])
    I.grid(["Gesprächsphase", "Meine Notizen"], widths=[3300, 6338], height=900, body=[
        ["**1 Ankommen**\nDank für das Kommen, Ziel und Dauer nennen", ""],
        ["**2 Beobachtungen schildern**\nkonkret, beschreibend, ohne Etiketten", ""],
        ["**3 Sicht der Eltern**\nzuhören, nachfragen", ""],
        ["**4 Gemeinsame Lösungen**\nwas die Schule tut, was die Eltern tun", ""],
        ["**5 Vereinbarung**\nnächster Kontakt, Ansprechperson", ""]])
    I.h2("Hinweise, die ich den Eltern mitgebe")
    I.checklist(["Ruhig zuhören, das Kind ernst nehmen, ihm glauben.", "Nicht über den Kopf des Kindes und der Schule hinweg handeln, etwa andere Eltern direkt konfrontieren.", "Vorfälle notieren, bei Cybermobbing Screenshots sichern, nicht online antworten.", "Beratung: Pro Juventute 147 für Kinder und Jugendliche, Elternberatung."], cols=("Hinweis", "✓"))
    I.source("Nach Jannan, 2010, S. 13 ff.; Alsaker, 2012; Schubarth, 2020, S. 216 f.; Walker et al., 2026, Kap. 8.5.")


def ko7(I):
    I.kicker(f"Instrument {I.nr}"); I.title("Cybermobbing: Was ich tun kann")
    I.sub("Arbeitsblatt für Lernende in Zyklus 2 und 3: sich selbst und andere schützen, Beweise sichern, Hilfe holen.")
    I.p("Cybermobbing ist Mobbing über Chats, soziale Netzwerke, Videoportale oder Games. Online gibt es oft keinen Rückzugsort. Wer online gemobbt wird, wird meist auch in der Schule gemobbt.")
    I.h2("Wenn es mich trifft")
    I.checklist(["**Nicht online zurückschlagen.** Das macht es meistens schlimmer.", "**Beweise sichern:** Screenshots mit Datum, Namen und Link.", "**Blockieren und melden** auf der Plattform.", "**Hilfe holen:** Eltern, Lehrperson, Schulsozialarbeit, Freundinnen und Freunde oder 147 (Pro Juventute, Telefon, SMS, Chat).", "Verbotene Inhalte (z. B. Nacktbilder) nicht speichern oder weiterleiten, sondern melden."], cols=("Das tue ich", "✓"))
    I.h2("Wenn ich sehe, dass es jemand anderen trifft")
    I.checklist(["Nicht liken, nicht teilen, nicht kommentieren.", "Der betroffenen Person privat schreiben: «Ich finde das nicht ok. Brauchst du Hilfe?»", "Einer erwachsenen Person Bescheid geben."], cols=("Das tue ich", "✓"))
    I.h2("Meine Hilfe-Liste")
    I.fields(["Eine erwachsene Person, der ich vertraue", "Schulsozialarbeit (Name, Kontakt)", "Beratung für Kinder und Jugendliche: 147"], 3600)
    I.box("Gut zu wissen", "Cybermobbing ist in der Schweiz kein eigener Straftatbestand. Einzelne Handlungen wie Drohung, Beschimpfung, Verleumdung oder unerlaubte Bildaufnahmen können aber strafbar sein.")
    I.source("Nach Walker et al., 2026, Kap. 8.5; Pro Juventute, Cybermobbing.")


def ko8(I):
    I.kicker(f"Instrument {I.nr}"); I.title("Klassen-Check gegen Mobbing")
    I.sub("Acht Fragen, um zu prüfen, wie gut eine Klasse vor Mobbing geschützt ist.")
    I.fields(["Klasse, Zyklus, Datum"])
    I.checklist(["**1 Begriffe klar:** Können die Lernenden, ihrem Alter entsprechend, Konflikt und Mobbing unterscheiden?",
                 "**2 Regeln:** Gibt es gemeinsam erarbeitete Regeln gegen Mobbing mit bekannten Konsequenzen, die auch durchgesetzt werden?",
                 "**3 Gefäss:** Gibt es ein regelmässiges Gefäss (Kreis, Klassenrat), in dem Konflikte angesprochen werden?",
                 "**4 Zuschauende:** Wissen die Kinder, was sie tun können, wenn jemand geplagt wird, und haben sie es geübt?",
                 "**5 Beobachten:** Beobachte ich auch Pause, Garderobe, Schulweg und Klassenchat, und notiere ich Auffälligkeiten?",
                 "**6 Vertrauen:** Würden sich Kinder mir anvertrauen, bevor es zu spät ist?",
                 "**7 Leitfaden:** Kenne ich den Handlungsleitfaden der Schule und weiss, wann ich Schulleitung, Schulsozialarbeit und Eltern beiziehe?",
                 "**8 Stufengerecht:** Passen meine Massnahmen zum Zyklus und zum Entwicklungsstand meiner Klasse?"])
    I.h2("Eine Sache, die ich angehe")
    I.lines(3)
    I.tip("Tipp für Praktika: Beobachte während einer Woche gezielt die Pausen: Wer spielt mit wem, wer steht allein, wer lacht über wen? Vergleiche deine Notizen mit der Einschätzung der Praxislehrperson.")
    I.source("Eigene Synthese aus den Quellen der Seite «Umgang mit Konflikten, Gewalt und Mobbing» (Alsaker, 2012; Schubarth, 2020; Hauser et al., 2009; Jannan, 2010; Walker et al., 2026).")


KON = ("Umgang mit Konflikten, Gewalt und Mobbing", "konflikte", "Instrumente_Konflikte_Gewalt_Mobbing", [
    ("KO1_Konflikt-oder-Mobbing", "Konflikt oder Mobbing? Einschätzungsbogen", "Die Merkmale von Mobbing beobachtend prüfen und eine Situation begründet einschätzen.", ko1),
    ("KO2_Beobachtungsprotokoll", "Beobachtungsprotokoll Gruppe und Pause", "Vorfälle beschreiben und festhalten, wer in der Gruppe welche Rolle einnimmt.", ko2),
    ("KO3_Klassenregeln", "Klassenregeln gegen Mobbing erarbeiten", "Regeln und Konsequenzen mit der Klasse aushandeln, mit Handlungsmöglichkeiten je Zyklus.", ko3),
    ("KO4_No-Blame-Approach", "No Blame Approach: Leitfaden", "Die drei Schritte mit Gesprächshinweisen und Platz für Unterstützungsgruppe und Nachgespräche.", ko4),
    ("KO5_Interventionsplan", "Interventionsplan bei Mobbing", "Schutz, Massnahmen mit Zuständigkeiten und eine fortlaufende Dokumentation für einen konkreten Fall.", ko5),
    ("KO6_Elterngespraech", "Elterngespräch bei Mobbing vorbereiten", "Gesprächsphasen, Notizen und Hinweise für Eltern von betroffenen oder mobbenden Kindern.", ko6),
    ("KO7_Cybermobbing-Lernende", "Cybermobbing: Was ich tun kann", "Arbeitsblatt für Lernende in Zyklus 2 und 3: Beweise sichern, Hilfe holen, andere unterstützen.", ko7),
    ("KO8_Klassen-Check", "Klassen-Check gegen Mobbing", "Die acht Fragen des Klassen-Checks zum Ausdrucken, mit Platz für einen nächsten Schritt.", ko8)])

THEMEN = [DIG, BEU, KON]
