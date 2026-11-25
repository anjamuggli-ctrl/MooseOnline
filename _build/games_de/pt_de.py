# Deutsche Fassung von Power Town: ersetzt Blöcke und Texte der englischen Vorlage.
Q_DE = r'''var Q = {
 gh: [
  ["Was ist die Atmosphäre?", ["die Gashülle um die Erde","das heisse Innere der Erde","das Eis am Nordpol","das Licht der Sonne"], 0, "Die Atmosphäre ist die Schicht aus Gasen, die die Erde umgibt.", 1],
  ["Welches dieser Gase ist ein Treibhausgas?", ["Methan","Sauerstoff","Stickstoff","Helium"], 0, "Methan (CH₄) ist ein Treibhausgas. Es entsteht zum Beispiel bei Rindern, in Reisfeldern und auf Deponien.", 1],
  ["Wie hoch wäre die Durchschnittstemperatur auf der Erde ohne natürlichen Treibhauseffekt?", ["etwa −18 °C","etwa 0 °C","etwa +15 °C","etwa +30 °C"], 0, "Ohne ihn läge der Durchschnitt bei etwa −18 °C statt bei etwa +15 °C.", 1],
  ["Was bewirken Treibhausgase?", ["Sie lassen das Sonnenlicht grösstenteils durch, halten aber einen Teil der Wärme der Erde zurück.","Sie blockieren das ganze Sonnenlicht.","Sie produzieren Sauerstoff.","Sie machen Löcher in die Ozonschicht."], 0, "Sie halten einen Teil der Infrarotstrahlung (Wärme) zurück und senden sie zur Oberfläche zurück.", 1],
  ["Wodurch verstärkt der Mensch den Treibhauseffekt vor allem?", ["durch das Verbrennen von Kohle, Öl und Gas","durch Solaranlagen","durch den Bau von Staudämmen","durch das Pflanzen von Bäumen"], 0, "Das Verbrennen fossiler Brennstoffe und das Abholzen von Wäldern bringen zusätzliches CO₂ in die Atmosphäre.", 1],
  ["Woher stammt Lachgas (N₂O) vor allem?", ["aus Dünger auf den Feldern","aus alten Kühlschränken","aus brennendem Holz","aus schmelzenden Gletschern"], 0, "Landwirtinnen und Landwirte düngen ihre Felder, dabei wird Lachgas frei.", 2],
  ["Welche Aussage stimmt?", ["Wetter ist ein Tag an einem Ort; Klima ist das durchschnittliche Wetter über etwa 30 Jahre.","Wetter und Klima bedeuten dasselbe.","Klima ist das Wetter einer Woche.","Wetter bedeutet nur Temperatur."], 0, "Klima ist das durchschnittliche Wetter einer Region über lange Zeit, meist 30 Jahre.", 2],
  ["Ist das Ozonloch die Hauptursache der Klimaerwärmung?", ["Nein, die Hauptursache ist die Zunahme der Treibhausgase, vor allem CO₂.","Ja, es lässt mehr Wärme herein.","Ja, es verhindert, dass Wärme entweicht.","Nein, die Sonne wird heisser."], 0, "Das Ozonloch ist ein anderes Problem. Die Erwärmung kommt vor allem von zusätzlichen Treibhausgasen.", 2],
  ["Die warme Erdoberfläche gibt Wärme ab als …", ["Infrarotstrahlung","UV-Licht","Schallwellen","Röntgenstrahlen"], 0, "Die Erde gibt Wärme als Infrarotstrahlung ab.", 2]
 ],
 sea: [
  ["Was passiert mit Meerwasser, wenn es wärmer wird?", ["Es dehnt sich aus und braucht mehr Platz.","Es zieht sich zusammen.","Es gefriert.","Nichts."], 0, "Das nennt mensch Wärmeausdehnung. Sie ist einer der beiden Hauptgründe für den steigenden Meeresspiegel.", 1],
  ["Welches schmelzende Eis lässt den Meeresspiegel steigen?", ["Gletscher und die Eisschilde von Grönland und der Antarktis","schwimmendes Meereis in der Arktis","Eisberge, die schon im Meer treiben","Eiswürfel in einem Getränk"], 0, "Nur Eis, das auf dem Land liegt, bringt neues Wasser ins Meer.", 1],
  ["Warum verändert schmelzendes Meereis den Meeresspiegel kaum?", ["Es schwimmt schon im Wasser, wie ein Eiswürfel im Glas.","Es schmilzt zu langsam.","Es besteht aus Salz.","Es verdunstet sofort."], 0, "Schwimmendes Eis verdrängt bereits so viel Wasser, wie es wiegt.", 2],
  ["Was sind die zwei Hauptgründe für den steigenden Meeresspiegel?", ["Warmes Wasser dehnt sich aus, und Eis auf dem Land schmilzt.","Mehr Regen und mehr Flüsse","Erdbeben und Vulkane","Schiffe und Fische"], 0, "Wärmeausdehnung und schmelzendes Landeis.", 2],
  ["Die Schweiz hat keine Küste. Warum betrifft der steigende Meeresspiegel trotzdem Menschen in der Schweiz?", ["Waren kommen über grosse Häfen, und Menschen aus überschwemmten Regionen müssen vielleicht umziehen.","Er betrifft die Schweiz gar nicht.","Die Schweizer Seen überfluten die Alpen.","Der Rhein fliesst dann rückwärts."], 0, "Handel, Lebensmittelpreise und Migration verbinden die Schweiz mit Küstenregionen, und schmelzende Schweizer Gletscher bringen Wasser ins Meer.", 2],
  ["Was meldete der Bericht «State of the Climate in 2025» zum globalen Meeresspiegel?", ["Er erreichte einen Rekordwert.","Er sank zum ersten Mal.","Er war gleich hoch wie 1900.","Er wurde nicht gemessen."], 0, "Gemäss dem Bericht erreichte der globale Meeresspiegel 2025 einen Rekordwert.", 2]
 ],
 solar: [
  ["Energie kann weder erzeugt noch vernichtet werden. Sie kann nur …", ["umgewandelt werden","produziert werden","verbrannt werden","für immer gespeichert werden"], 0, "Energie kann nur von einer Form in eine andere umgewandelt werden.", 1],
  ["Was wandelt eine Solarzelle um?", ["Lichtenergie in elektrische Energie","Lichtenergie in Wärme","Wärme in Licht","elektrische Energie in Bewegung"], 0, "Eine Solarzelle (Photovoltaikzelle) erzeugt direkt aus Licht Strom.", 1],
  ["Was macht ein Sonnenkollektor?", ["Er erwärmt mit Sonnenlicht Wasser.","Er erzeugt Strom aus Wind.","Er speichert Strom.","Er kühlt ein Haus."], 0, "Ein Sonnenkollektor wandelt Lichtenergie in Wärme um, zum Beispiel für Warmwasser.", 1],
  ["Welches Gerät wandelt Bewegungsenergie in elektrische Energie um?", ["ein Generator","ein Elektromotor","ein Sonnenkollektor","ein Holzofen"], 0, "Ein Generator macht aus Bewegung Strom. Ein Motor macht das Umgekehrte.", 1],
  ["Wasser in einem Stausee hoch in den Bergen hat …", ["Lageenergie (potenzielle Energie)","chemische Energie","Kernenergie","keine Energie"], 0, "Wegen seiner Höhe speichert das Wasser Lageenergie.", 1],
  ["Was ist ein Nachteil der Solarenergie?", ["Nachts erzeugt sie keinen Strom.","Die Energiequelle geht aus.","Sie erzeugt viel CO₂.","Sie braucht viel Wartung."], 0, "Ohne Sonne kein Strom: nachts und bei Bewölkung erzeugen Solaranlagen wenig.", 1],
  ["Was sagt der Wirkungsgrad einer Maschine aus?", ["wie viel der Energie nutzbar ist","wie schnell sie läuft","wie schwer sie ist","wie viel sie kostet"], 0, "Keine Maschine wandelt alle Energie in nutzbare Energie um; ein Teil geht verloren, meist als Wärme.", 2],
  ["Was ist ein Sonnenofen?", ["Viele Spiegel bündeln das Sonnenlicht auf einen kleinen Punkt und machen ihn extrem heiss.","Ein Ofen, in dem Holz brennt.","Eine Solaranlage auf dem Dach.","Eine Batterie für Solarstrom."], 0, "Sonnenöfen erreichen mehrere tausend Grad und dienen der Forschung und dem Schmelzen von Metallen.", 2],
  ["Warum ist der Absorber in einem Sonnenkollektor schwarz?", ["Schwarz nimmt das Licht am besten auf und wird heiss.","Schwarz sieht auf dem Dach schöner aus.","Schwarz reflektiert das Licht.","Schwarz hält das Wasser kalt."], 0, "Eine schwarze Fläche nimmt das meiste Licht auf und wandelt es in Wärme um.", 2],
  ["Was wandelt ein Elektromotor um?", ["elektrische Energie in Bewegungsenergie","Bewegungsenergie in elektrische Energie","Licht in Wärme","chemische Energie in Licht"], 0, "Ein Motor macht aus Strom Bewegung.", 2]
 ],
 water: [
  ["Was ist ein Stausee?", ["ein künstlicher See hinter einer Staumauer","ein grosses Rohr","die Mündung eines Flusses","eine Maschine im Meer"], 0, "Das Wasser wird im Stausee hinter der Staumauer gespeichert.", 1],
  ["Was ist eine Druckleitung?", ["ein grosses Rohr, das das Wasser zu den Turbinen hinunterführt","ein See in den Bergen","eine Fischart","ein Stromkabel"], 0, "Die Druckleitung führt das Wasser vom Stausee zu den Turbinen.", 1],
  ["Wie viel des Schweizer Stroms stammt etwa aus Wasserkraft?", ["mehr als die Hälfte","etwa 5 %","etwa 20 %","gar nichts"], 0, "Die Wasserkraft ist die wichtigste Stromquelle der Schweiz.", 1],
  ["Was nutzt ein Gezeitenkraftwerk?", ["das Steigen und Sinken des Meeresspiegels (Ebbe und Flut)","die Wellen eines Sees","den Regen in den Bergen","warmes Wasser aus dem Boden"], 0, "Gezeitenkraft nutzt Ebbe und Flut, die etwa zweimal am Tag kommen.", 1],
  ["Was ist ein Ästuar?", ["der breite Teil eines Flusses, wo er ins Meer mündet","eine Turbinenart","die Quelle eines Flusses","ein Stausee in den Alpen"], 0, "Gezeitenkraftwerke werden quer über solche Flussmündungen gebaut.", 2],
  ["Warum gibt es nur an wenigen Orten Gezeitenkraftwerke?", ["Sie brauchen einen sehr grossen Unterschied zwischen Ebbe und Flut und eine geeignete Flussmündung.","Sie brauchen viel Sonne.","Sie funktionieren nur in den Alpen.","Sie sind in Europa verboten."], 0, "Beides ist selten. La Rance in Frankreich läuft seit 1966.", 2],
  ["Wie funktioniert ein Pumpspeicherkraftwerk?", ["Bei Stromüberschuss pumpt es Wasser hinauf, bei Bedarf lässt es das Wasser wieder hinunter.","Es pumpt Wasser aus dem Meer.","Es pumpt Wasser mit Wellen.","Es speichert Strom in grossen Batterien."], 0, "Es wirkt wie eine riesige Batterie und hilft, das Stromnetz auszugleichen.", 2],
  ["Warum lässt sich Gezeitenkraft gut vorhersagen?", ["Die Zeiten von Ebbe und Flut sind Jahre im Voraus bekannt.","Der Wind weht immer gleich.","Sie funktioniert nur im Sommer.","Weil es jeden Tag regnet."], 0, "Die Gezeiten folgen dem Mond und sind darum sehr regelmässig.", 2],
  ["Welches Wort bedeutet dasselbe wie «Strom erzeugen»?", ["Strom produzieren","Strom vernichten","Strom zurückwandeln","Strom sparen"], 0, "Strom erzeugen = Strom produzieren.", 2]
 ],
 wind: [
  ["Was dreht den Rotor einer Windturbine?", ["der Wind, der auf die Rotorblätter bläst","ein Motor im Turm","das Wasser im Fluss","die Sonne"], 0, "Der Wind dreht die Rotorblätter, die an der Nabe befestigt sind.", 1],
  ["Wo befindet sich der Generator einer Windturbine?", ["in der Gondel oben auf dem Turm","unter dem Boden","in den Rotorblättern","nur neben dem Transformator unten"], 0, "Getriebe und Generator sind in der Gondel.", 1],
  ["Was misst ein Anemometer?", ["die Windgeschwindigkeit","die Temperatur","die Spannung","die Höhe des Turms"], 0, "Das Anemometer misst die Windgeschwindigkeit, die Windfahne die Richtung.", 1],
  ["Was passiert mit einer Windturbine bei sehr starkem Wind?", ["Sie wird abgeschaltet, damit sie nicht beschädigt wird.","Sie erzeugt den meisten Strom überhaupt.","Sie dreht rückwärts.","Sie fällt um."], 0, "Bei Sturm werden die Turbinen abgeschaltet.", 1],
  ["Was macht das Getriebe?", ["Es erhöht die Drehzahl, damit der Generator schnell genug dreht.","Es dreht die Gondel in den Wind.","Es misst den Wind.","Es speichert Strom."], 0, "Die langsame Welle dreht langsam; das Getriebe lässt die schnelle Welle schnell drehen.", 2],
  ["Was macht der Azimutantrieb (Windnachführung)?", ["Er dreht die Gondel, damit der Rotor immer im Wind steht.","Er bremst die Rotorblätter.","Er erhöht die Spannung.","Er kühlt den Generator."], 0, "Er hält den Rotor in Windrichtung.", 2],
  ["Warum baut mensch Windparks im Meer (offshore)?", ["Der Wind ist dort meist stärker und gleichmässiger.","An Land gibt es keinen Wind.","Fische brauchen Strom.","Bauen im Wasser ist billiger."], 0, "Auf dem Meer weht der Wind stärker und regelmässiger.", 2],
  ["Welches Land hat 2025 etwa drei Viertel der neuen Windkraft weltweit gebaut?", ["China","die Schweiz","Deutschland","die USA"], 0, "China baute 119,4 GW der 158,7 GW (IRENA).", 2],
  ["Warum braucht ein Land mit viel Windkraft auch Speicher oder andere Kraftwerke?", ["Der Wind weht nicht immer.","Windturbinen laufen nur nachts.","Windkraft ist im Winter verboten.","Turbinen brauchen Diesel zum Starten."], 0, "Bei wenig Wind müssen andere Quellen oder Speicher den Strom liefern.", 2]
 ],
 nuclear: [
  ["Woher kommt die Wärme in einem Kernkraftwerk?", ["aus der Kernspaltung","aus dem Verbrennen von Kohle","von der Sonne","vom Wind"], 0, "Urankerne werden gespalten und setzen Wärme frei.", 1],
  ["Was ist der Brennstoff in einem Kernkraftwerk?", ["Uran","Öl","Holz","Wasserstoff"], 0, "Uranoxid wird zu Tabletten gepresst und in Brennstäbe gefüllt.", 1],
  ["Was machen die Steuerstäbe?", ["Sie fangen Neutronen ein und können die Kettenreaktion verlangsamen oder stoppen.","Sie erzeugen Strom.","Sie kühlen den Fluss.","Sie halten die Brennstofftabletten."], 0, "Steuerstäbe absorbieren Neutronen.", 1],
  ["Was steigt aus dem Kühlturm auf?", ["Wasserdampf","Rauch mit CO₂","radioaktives Gas","nichts"], 0, "Die weisse Wolke ist Wasserdampf, kein Rauch.", 1],
  ["Was ist das grösste Problem der Kernenergie?", ["radioaktiver Abfall, der während Tausenden von Jahren gefährlich bleibt","viel CO₂","sie funktioniert nur im Sommer","sie braucht viel Wind"], 0, "In der Schweiz gibt es noch kein Endlager.", 1],
  ["Ist Kernenergie erneuerbar?", ["Nein, Uran wird abgebaut und geht eines Tages aus.","Ja, wie die Solarenergie.","Ja, weil sie Wasser nutzt.","Nur in der Schweiz."], 0, "Sie ist CO₂-arm, aber nicht erneuerbar.", 2],
  ["Warum kocht das Wasser im Primärkreislauf bei etwa 320 °C nicht?", ["Es steht unter sehr hohem Druck.","Es ist mit Salz gemischt.","Es wird zuerst gefroren.","Es fliesst zu schnell."], 0, "Hoher Druck hält das Wasser flüssig.", 2],
  ["Wie entsteht eine Kettenreaktion?", ["Ein Neutron spaltet einen Kern; dabei werden neue Neutronen frei, die weitere Kerne spalten.","Die Turbine dreht immer schneller.","Kaltes Wasser fliesst in den Reaktor.","Die Steuerstäbe werden eingefahren."], 0, "Jede Spaltung setzt neue Neutronen frei.", 2],
  ["Was hat die Schweizer Stimmbevölkerung 2017 entschieden?", ["Es dürfen keine neuen Kernkraftwerke gebaut werden.","Alle Kernkraftwerke müssen sofort schliessen.","Zwei neue Kernkraftwerke werden gebaut.","Atommüll darf exportiert werden."], 0, "Die Energiestrategie 2050 verbietet neue Kernkraftwerke. Heute möchten einige das ändern.", 2],
  ["Was wandelt die Bewegung der Turbine in Strom um?", ["der Generator","die Steuerstäbe","das Reaktorgebäude","der Kühlturm"], 0, "Dampf dreht die Turbine, und der Generator erzeugt Strom.", 2]
 ],
 stats: [
  ["CO₂ am Mauna Loa: 401 ppm (2015) und 427 ppm (2025). Um wie viel stieg der Wert?", ["um etwa 26 ppm","um etwa 6 ppm","um etwa 46 ppm","um etwa 427 ppm"], 0, "427 − 401 = 26 ppm, etwa 2,6 ppm pro Jahr.", 1, {l:["2015","2020","2025"],v:[401,414,427],min:390,u:" ppm"}],
  ["Welches Jahr war bisher (Stand 2025) das wärmste seit Messbeginn?", ["2024","2016","2020","2025"], 0, "2024 lag 1,29 °C über dem Durchschnitt des 20. Jahrhunderts.", 1, {l:["2020","2023","2024","2025"],v:[1.02,1.19,1.29,1.17],min:0,u:" °C"}],
  ["Schweizer Solarstrom: 6,0 TWh (2024) und 8,0 TWh (2025). Wie hat sich die Produktion verändert?", ["um etwa +2 TWh","um etwa −2 TWh","um etwa +8 TWh","gar nicht"], 0, "Von 6,0 auf 8,0 TWh: etwa +2 TWh, eine Zunahme um etwa einen Drittel.", 1, {l:["2024","2025"],v:[6.0,8.0],min:0,u:" TWh"}],
  ["2025 kamen weltweit 692 GW erneuerbare Leistung dazu, davon 511 GW Solar. Wie gross war etwa der Solaranteil?", ["etwa 75 %","etwa 25 %","etwa 50 %","etwa 95 %"], 0, "511 ÷ 692 ≈ 0,74, also etwa drei Viertel.", 2, {l:["Solar","Wind","Wasser","Bio"],v:[511,159,18,3],min:0,u:" GW"}],
  ["Eine Schlagzeile lautet: «2025 war kühler als 2024 – die Erwärmung ist gestoppt!» Warum ist das falsch?", ["Ein einzelnes Jahr stoppt keinen langfristigen Trend; die Temperaturen schwanken von Jahr zu Jahr.","Weil 2025 eigentlich das heisseste Jahr war.","Weil gar nicht mehr gemessen wird.","Die Schlagzeile stimmt."], 0, "Entscheidend ist der lange Trend: Seit 1980 ist es um etwa 0,9 °C wärmer geworden.", 2],
  ["Die y-Achse einer Grafik beginnt bei 395 ppm, nicht bei 0. Was bewirkt das?", ["Der Anstieg wirkt steiler als auf einer Achse, die bei 0 beginnt.","Die Zahlen sind falsch.","Der Anstieg wirkt kleiner.","Es hat keine Wirkung."], 0, "Eine abgeschnittene Achse lässt Veränderungen grösser wirken. Lies die Zahlen, nicht nur die Form.", 2],
  ["Weltweiter Strom 2025: Kohle 33,0 %, alle Erneuerbaren 33,8 %. Was stimmt?", ["Die Erneuerbaren erzeugten etwas mehr als die Kohle.","Kohle erzeugte mehr als alle Erneuerbaren.","Solar war die grösste einzelne Quelle.","Fossile Energien erzeugten weniger als die Hälfte."], 0, "Gemäss Ember war das zum ersten Mal seit etwa 100 Jahren so.", 2],
  ["Die Schweizer Wasserkraft sank von 48,3 TWh (2024) auf 37,5 TWh (2025). Was ist ein möglicher Grund?", ["weniger Regen und Schnee 2025","mehr Sonnenschein 2025","neue Kernkraftwerke","mehr Windturbinen"], 0, "Weniger Wasser in Flüssen und Stauseen bedeutet weniger Wasserkraft.", 2, {l:["2024","2025"],v:[48.3,37.5],min:0,u:" TWh"}],
  ["Beweist eine Grafik, in der CO₂ und Temperatur gemeinsam steigen, dass CO₂ die Erwärmung verursacht?", ["Nein, Korrelation ist keine Kausalität; den Zusammenhang belegen aber Physik und viele Studien.","Ja, zwei steigende Linien beweisen das immer.","Nein, CO₂ hat nichts mit der Temperatur zu tun.","Ja, weil die Grafik blau ist."], 0, "Zwei Dinge können gemeinsam steigen, ohne dass das eine das andere verursacht. Der Beweis kommt aus Physik und Forschung.", 2]
 ],
 island: [
  ["Auf der Insel Mira beträgt der Tidenhub nur etwa 1 Meter. Welche Energiequelle passt am wenigsten?", ["Gezeitenkraft","Solarenergie","Windkraft","Batterien"], 0, "Gezeitenkraft braucht einen sehr grossen Unterschied zwischen Ebbe und Flut.", 1],
  ["Insel Mira: sonnige Sommer, windige Winter. Warum passen Solar- und Windenergie gut zusammen?", ["Wenn die eine wenig erzeugt, erzeugt die andere oft mehr.","Beide erzeugen im Sommer am meisten.","Beide funktionieren ohne Wind.","Beide werden im Meer gespeichert."], 0, "Sonne im Sommer, Wind im Herbst und Winter: Sie ergänzen sich.", 2],
  ["Warum ist ein grosser Staudamm auf der Insel Mira keine gute Idee?", ["Es gibt keine Berge und nur einen kleinen Fluss.","Staudämme erzeugen CO₂.","Touristinnen und Touristen mögen kein Wasser.","Staudämme funktionieren nur nachts."], 0, "Wasserkraft braucht einen grossen Höhenunterschied und viel Wasser.", 2]
 ]
};
var CATS = {gh:"Treibhauseffekt", sea:"Meeresspiegel", solar:"Energieumwandlung und Solarenergie", water:"Wasserkraft", wind:"Windkraft", nuclear:"Kernenergie", stats:"Statistik", island:"Das Inselprojekt"};
'''

EVENTS_DE = r'''var EVENTS = [
 {id:"glacier", img:"pt-event-glacier.jpg", t:"Die Gletscher schmelzen", x:"Ein heisser Sommer lässt einen grossen Teil der Gletscher über deinen Stauseen schmelzen. Langfristig gibt es weniger Schmelzwasser für deine Staudämme.", run:function(p){ meter(1); var n=count(p,"hydro"); if(n){ pay(p,30*n); return "Klimabarometer +1. Du bezahlst "+(30*n)+" Taler für deine Wasserkraftwerke."; } return "Klimabarometer +1."; }},
 {id:"storm", img:"pt-event-storm.jpg", t:"Sturmflut an der Küste", x:"Eine Sturmflut trifft den Hafen deiner Partnerstadt. Zeig, dass du den steigenden Meeresspiegel verstehst, dann wird die Hilfe deiner Stadt günstiger.", q:"sea", ok:function(p){ return "Gut gemacht! Deine Fachleute wissen, was zu tun ist. Keine Kosten."; }, no:function(p){ pay(p,80); return "Du bezahlst 80 Taler für Nothilfe."; }},
 {id:"heatwave", img:"pt-event-heatwave.jpg", t:"Hitzewelle", x:"Die Flüsse sind zu warm. Kernkraftwerke, die mit Flusswasser kühlen, müssen ihre Leistung drosseln.", run:function(p){ var n=count(p,"nuclear"); if(n){ pay(p,50*n); return "Du bezahlst "+(50*n)+" Taler für deine Kernkraftwerke."; } add(p,20); return "Du hast kein Kernkraftwerk. Deine Solarzellen lieben die Sonne: +20 Taler."; }},
 {id:"blackout", img:"pt-event-blackout.jpg", t:"Winterabend ohne Strom", x:"An einem kalten, dunklen Winterabend hat es zu wenig Strom im Netz. Städte, die Energie speichern können, helfen aus und verkaufen ihren Strom.", run:function(p){ var n=count(p,"hydro"); if(n){ add(p,80); return "Deine Wasserkraftwerke liefern auch nachts Strom: +80 Taler."; } pay(p,40); return "Du musst teuren Strom einkaufen: −40 Taler. (Tipp: Wasserkraft und Pumpspeicher helfen im Winter.)"; }},
 {id:"funding", img:"pt-event-funding.jpg", t:"Fördergeld bewilligt!", x:"Der Kanton unterstützt Städte, die in saubere Energie investieren.", run:function(p){ var n=count(p,"solar")+count(p,"wind")+count(p,"hydro"); if(n){ add(p,150); return "Du besitzt erneuerbare Kraftwerke: +150 Taler!"; } add(p,50); return "+50 Taler. Mit erneuerbaren Kraftwerken wären es 150 gewesen."; }},
 {id:"citizens", img:"pt-event-citizens.jpg", t:"Bürgerinnen und Bürger bauen gemeinsam Solar", x:"Nachbarinnen und Nachbarn montieren Solarpanels auf ihrem Mehrfamilienhaus. Deine Stadt unterstützt sie.", run:function(p){ var f=FIELDS.map(function(f,i){return i;}).filter(function(i){ return S.own[i]===p.id && FIELDS[i].t==="solar" && S.lvl[i]<2; }); if(f.length){ S.lvl[f[0]]=2; return "Eines deiner Solarkraftwerke wird gratis ausgebaut: "+FIELDS[f[0]].nm+" ★★"; } add(p,60); return "+60 Taler."; }},
 {id:"tax", img:"pt-event-tax.jpg", t:"Neue CO₂-Abgabe", x:"Fossile Kraftwerke müssen neu für jede Tonne CO₂ eine Abgabe bezahlen.", run:function(p){ var n=count(p,"gas"); if(n){ pay(p,40*n); return "Du bezahlst "+(40*n)+" Taler für deine Gaskraftwerke."; } return "Du hast kein Gaskraftwerk. Nichts zu bezahlen!"; }},
 {id:"prize", img:"pt-event-prize.jpg", t:"Wissenschaftspreis", x:"Eine schwierige Frage. Beantworte sie richtig und gewinne den Wissenschaftspreis der Stadt.", q:"any2", ok:function(p){ add(p,120); return "+120 Taler!"; }, no:function(){ return "Diesmal kein Preis."; }},
 {id:"sunny", img:"pt-event-sunny.jpg", t:"Ein sehr sonniger Sommer", x:"Rekord an Sonnenstunden! Solarkraftwerke produzieren mehr als je zuvor.", run:function(p){ var n=count(p,"solar"); if(n){ add(p,35*n); return "+"+(35*n)+" Taler für deine Solarkraftwerke."; } return "Du hast noch kein Solarkraftwerk."; }},
 {id:"windy", img:"pt-event-windy.jpg", t:"Ein stürmischer Winter", x:"Den ganzen Winter weht starker Wind. Windturbinen produzieren viel, genau dann, wenn Solaranlagen wenig liefern.", run:function(p){ var n=count(p,"wind"); if(n){ add(p,35*n); return "+"+(35*n)+" Taler für deine Windkraftwerke."; } return "Du hast noch kein Windkraftwerk."; }},
 {id:"waste", img:"pt-event-waste.jpg", t:"Radioaktiver Abfall", x:"Wer ein Kernkraftwerk besitzt, zahlt in den Fonds für die Endlagerung radioaktiver Abfälle ein.", run:function(p){ var n=count(p,"nuclear"); if(n){ pay(p,40*n); return "Du bezahlst "+(40*n)+" Taler."; } return "Du hast kein Kernkraftwerk. Nichts zu bezahlen."; }},
 {id:"strike", img:"pt-event-strike.jpg", t:"Klimastreik", x:"Junge Menschen demonstrieren für mehr Klimaschutz. Erkläre den Treibhauseffekt richtig, dann verspricht die Stadt, Emissionen zu senken.", q:"gh", ok:function(){ meter(-1); return "Klimabarometer −1!"; }, no:function(){ return "Der Protest bleibt diesmal ohne Wirkung."; }}
];
'''

RULES_DE = r'''var RULES = '<ul class="pt-rules">'
  +'<li><b>Würfeln und ziehen</b> im Uhrzeigersinn. Wer am <b>Rathaus</b> vorbeizieht, erhält 100 Taler.</li>'
  +'<li><b>Freies Kraftwerksfeld:</b> Beantworte eine Frage zu dieser Energiequelle. Ist sie richtig, darfst du das Kraftwerk kaufen.</li>'
  +'<li><b>Eigenes Kraftwerk:</b> Beantworte eine schwierigere Frage, um es auszubauen (★★). Danach verdient es doppelt.</li>'
  +'<li><b>Kraftwerk einer anderen Stadt:</b> Du bezahlst eine Netzgebühr. Mit einer richtigen Antwort zahlst du nur die Hälfte.</li>'
  +'<li><b>Zu Beginn jedes Zugs</b> verdienen deine Kraftwerke Taler: ☀️ 10 · 🌬️ 12 · 💧 16 · ⚛️ 22 · 🏭 16.</li>'
  +'<li><b>Gaskraftwerke</b> sind günstig, aber schmutzig: Jedes Mal, wenn du am Rathaus vorbeiziehst, erhöht jedes deiner Gaskraftwerke das <b>Klimabarometer</b> um 1. Erreicht es 10, überflutet das Wasser die Städte und <b>alle verlieren</b>.</li>'
  +'<li><b>Ereignis, Quiz, Statistik, Klimagipfel, Energiemesse, Stromausfall:</b> Folge der Karte.</li>'
  +'<li><b>Ende:</b> Nach der letzten Runde ist es 2050. Punkte = Taler + halber Wert deiner Kraftwerke + Sauberkeitsbonus (☀️🌬️💧 je +50, ⚛️ +20, 🏭 −60).</li>'
  +'</ul>';
'''

FIELDS = [("Town Hall","Rathaus"),("Rooftop Solar, Old Town","Solardächer Altstadt"),('nm:"Event"','nm:"Ereignis"'),("Gas Plant, Industrial Zone","Gaskraftwerk Industriezone"),
 ("Wind Park, Jura Ridge","Windpark Jurahöhe"),("Climate Summit","Klimagipfel"),("River Plant, Rhine","Flusskraftwerk Rhein"),("Alpine Solar Farm","Alpine Solaranlage"),
 ('nm:"Statistics"','nm:"Statistik"'),("Nuclear Plant, Aare","Kernkraftwerk Aare"),("Energy Fair","Energiemesse"),("Wind Turbine, Haldenstein","Windturbine Haldenstein"),
 ("Gas Plant, Harbour","Gaskraftwerk Hafen"),("Solar Façade, School","Solarfassade Schulhaus"),('nm:"Blackout", ic','nm:"Stromausfall", ic'),("Pumped Storage, Alps","Pumpspeicher Alpen"),
 ("Wind Park, Gotthard","Windpark Gotthard"),("Nuclear Plant, Lake","Kernkraftwerk am See"),("Dam, Graubünden","Staumauer Graubünden")]

REPL = [
 ('var KEY = "mo_powertown_v1";','var KEY = "mo_powertown_de_v1";'),
 ('name:"Solar", ic','name:"Solar", tag:"Solarenergie", ic'),('name:"Wind", ic','name:"Wind", tag:"Windkraft", ic'),('name:"Hydro", ic','name:"Wasser", tag:"Wasserkraft", ic'),
 ('name:"Nuclear", ic','name:"Kern", tag:"Kernenergie", ic'),('name:"Gas", ic','name:"Gas", tag:"Gaskraft", ic'),
 ('tag:t.name+" power"','tag:t.tag'),
 ('nm:"Tram"}','nm:"Tram"}'),('nm:"Wind turbine"}','nm:"Windturbine"}'),('nm:"Solar house"}','nm:"Solarhaus"}'),('nm:"Bicycle"}','nm:"Velo"}'),
 ("<h2>Power Town</h2>'", "<h2>Power Town</h2>'\n  +'<p class=\"pt-rules\" style=\"margin-top:0\">🇬🇧 <a href=\"pome24b-power-town.html\" style=\"text-decoration:underline\">English version of the game</a></p>'"),
 ("You are mayors of small Swiss towns. Your goal: build a clean, reliable energy supply by <b>2050</b>, earn credits and keep the shared <b>climate meter</b> low. To buy a power plant, you must first answer a question about Unit 9.",
  "Ihr seid Gemeindepräsidentinnen und Gemeindepräsidenten kleiner Schweizer Städte. Euer Ziel: bis <b>2050</b> eine saubere, sichere Energieversorgung aufbauen, Taler verdienen und das gemeinsame <b>Klimabarometer</b> tief halten. Wer ein Kraftwerk kaufen will, beantwortet zuerst eine Frage zu Energie und Umwelt."),
 ("Continue the saved game (round '","Gespeichertes Spiel fortsetzen (Runde '"),
 ("<h3>Players</h3>","<h3>Spielende</h3>"),
 ("One device for everyone: pass it on after each turn. You can also play in teams. Tick the box to play.","Ein Gerät für alle: Nach jedem Zug weitergeben. Ihr könnt auch in Teams spielen. Häkchen setzen, wer mitspielt."),
 ('["Team Tram","Team Wind","Team Sun","Team Bike"]','["Team Tram","Team Wind","Team Sonne","Team Velo"]'),
 ("aria-label=\"Name of player '","aria-label=\"Name von Spieler/in '"),("> plays</label>","> spielt mit</label>"),
 ("<h3>Game length</h3>","<h3>Spieldauer</h3>"),
 ("Short · 8 rounds · about 20 min","Kurz · 8 Runden · etwa 20 Min."),("Normal · 12 rounds · about 35 min","Normal · 12 Runden · etwa 35 Min."),("Long · 18 rounds · about 50 min","Lang · 18 Runden · etwa 50 Min."),
 ("<summary><b>Rules</b></summary>","<summary><b>Spielregeln</b></summary>"),
 ("Start a new game</button>","Neues Spiel starten</button>"),
 ('alert("Please choose at least one player.")','alert("Bitte wähle mindestens eine Spielerin oder einen Spieler.")'),
 ('log("The year is 2026. Good luck, mayors!")','log("Wir schreiben das Jahr 2026. Viel Glück!")'),
 ('aria-label="Bird’s-eye view of a Swiss lakeside town in transition to clean energy"','aria-label="Vogelperspektive auf eine Schweizer Seestadt im Wandel zu sauberer Energie"'),
 ("<h3>Towns</h3>","<h3>Städte</h3>"),('"no plants yet"','"noch keine Kraftwerke"'),("' · ⏸ skips a turn'","' · ⏸ setzt einmal aus'"),
 ("<h3>Diary</h3>","<h3>Tagebuch</h3>"),
 ("title=\"Climate meter: '+S.meter+' of 10\"","title=\"Klimabarometer: '+S.meter+' von 10\""),("<span>climate meter</span>","<span>Klimabarometer</span>"),
 ("+': roll the die</button>","+': würfeln</button>"),("📖 Rules</button>","📖 Regeln</button>"),('id="pt-new" style="padding:8px 14px;font-size:14px">New game</button>','id="pt-new" style="padding:8px 14px;font-size:14px">Neues Spiel</button>'),
 ('title:"How to play Power Town"','title:"So wird Power Town gespielt"'),('[{t:"Close", f:close}]','[{t:"Schliessen", f:close}]'),
 ('confirm("Start a new game? The current game will be lost.")','confirm("Neues Spiel starten? Das laufende Spiel geht verloren.")'),
 ("' · harder question'","' · schwierigere Frage'"),('(ok?"Correct!":"Not quite.")','(ok?"Richtig!":"Nicht ganz.")'),
 ('margin:2px 0 0">Unit:','margin:2px 0 0">Einheit:'),("' · the axis starts at '","' · die Achse beginnt bei '"),
 ('html:"<p>You are at the Town Hall. Time to plan the next investments.</p>"','html:"<p>Du bist im Rathaus. Zeit, die nächsten Investitionen zu planen.</p>"'),
 ('title:"Quiz", tag:"Quiz"','title:"Quiz", tag:"Quiz"'),('html:"<p>Answer correctly and earn <b>50 credits</b>.</p>"','html:"<p>Antworte richtig und verdiene <b>50 Taler</b>.</p>"'),
 ('" answers the quiz question correctly: +50.":" misses the quiz question."','" beantwortet die Quizfrage richtig: +50.":" verpasst die Quizfrage."'),
 ('title:"Statistics", tag:"Statistics"','title:"Statistik", tag:"Statistik"'),('html:"<p>Read the numbers carefully. Correct: <b>+70 credits</b>.</p>"','html:"<p>Lies die Zahlen genau. Richtig: <b>+70 Taler</b>.</p>"'),
 ('" reads the statistics correctly: +70.":" misreads the statistics."','" liest die Statistik richtig: +70.":" liest die Statistik falsch."'),
 ('title:"Climate Summit", tag:"Climate Summit"','title:"Klimagipfel", tag:"Klimagipfel"'),
 ('html:"<p>The towns meet to talk about climate protection. If you answer correctly, the <b>climate meter goes down by 1</b>.</p>"','html:"<p>Die Städte treffen sich, um über Klimaschutz zu sprechen. Antwortest du richtig, <b>sinkt das Klimabarometer um 1</b>.</p>"'),
 ('" convinces the Climate Summit: climate meter −1.":" could not convince the Climate Summit."','" überzeugt am Klimagipfel: Klimabarometer −1.":" kann den Klimagipfel nicht überzeugen."'),
 ('title:"Energy Fair", tag:"Energy Fair"','title:"Energiemesse", tag:"Energiemesse"'),
 ('html:"<p>Present your town’s energy plan at the fair. A harder question: correct gives <b>+150 credits</b>.</p>"','html:"<p>Stelle den Energieplan deiner Stadt an der Messe vor. Eine schwierigere Frage: richtig gibt <b>+150 Taler</b>.</p>"'),
 ('" wins the prize at the Energy Fair: +150.":" goes home from the Energy Fair without a prize."','" gewinnt den Preis der Energiemesse: +150.":" geht ohne Preis von der Energiemesse nach Hause."'),
 ('title:"Blackout!", tag:"Blackout"','title:"Stromausfall!", tag:"Stromausfall"'),
 ('html:"<p>The lights go out. Answer correctly to fix the grid. If not, you <b>miss your next turn</b>.</p>"','html:"<p>Das Licht geht aus. Antworte richtig, um das Netz zu reparieren. Sonst <b>setzt du einmal aus</b>.</p>"'),
 ('" fixes the blackout.":" must wait for the repair team and misses the next turn."','" behebt den Stromausfall.":" muss auf das Reparaturteam warten und setzt einmal aus."'),
 ("'<div class=\"pt-facts\"><span>Price: <b>'+t.price+'</b></span><span>Earns per turn: <b>'","'<div class=\"pt-facts\"><span>Preis: <b>'+t.price+'</b></span><span>Ertrag pro Zug: <b>'"),
 ("<span>Clean bonus at the end: <b>","<span>Sauberkeitsbonus am Schluss: <b>"),
 ("'⚠️ climate meter +1 each time you pass the Town Hall':'no CO₂ while working'","'⚠️ Klimabarometer +1 bei jedem Durchgang am Rathaus':'kein CO₂ im Betrieb'"),
 ("'<p>You do not have enough credits to buy this plant.</p>' : '<p>Answer the question to get the right to buy this plant.</p>'","'<p>Du hast nicht genug Taler, um dieses Kraftwerk zu kaufen.</p>' : '<p>Beantworte die Frage, um das Kraftwerk kaufen zu dürfen.</p>'"),
 ('{t:"Continue", f:next}','{t:"Weiter", f:next}'),
 ('{t:"Not now", alt:true, f:function(){ log(esc(p.nm)+" does not buy "+esc(f.nm)+"."); next(); }}, {t:"Buy for "+t.price','{t:"Jetzt nicht", alt:true, f:function(){ log(esc(p.nm)+" kauft "+esc(f.nm)+" nicht."); next(); }}, {t:"Kaufen für "+t.price'),
 ('log(esc(p.nm)+" buys "+esc(f.nm)+" "+t.ic+".")','log(esc(p.nm)+" kauft "+esc(f.nm)+" "+t.ic+".")'),
 ('log(esc(p.nm)+" cannot buy "+esc(f.nm)+" this time.")','log(esc(p.nm)+" kann "+esc(f.nm)+" diesmal nicht kaufen.")'),
 ('"<p>This is your plant, and it is already fully upgraded ★★.</p>"','"<p>Das ist dein Kraftwerk, und es ist bereits vollständig ausgebaut ★★.</p>"'),
 ('"<p>This is your plant. Answer a <b>harder question</b> to upgrade it for <b>"+cost+"</b> credits. It will then earn double.</p>"','"<p>Das ist dein Kraftwerk. Beantworte eine <b>schwierigere Frage</b>, um es für <b>"+cost+"</b> Taler auszubauen. Danach verdient es doppelt.</p>"'),
 ('"<p>You do not have enough credits for the upgrade.</p>"','"<p>Du hast nicht genug Taler für den Ausbau.</p>"'),
 ('{t:"Not now", alt:true, f:next}, {t:"Upgrade for "+cost','{t:"Jetzt nicht", alt:true, f:next}, {t:"Ausbauen für "+cost'),
 ('log(esc(p.nm)+" upgrades "+esc(f.nm)+" ★★.")','log(esc(p.nm)+" baut "+esc(f.nm)+" aus ★★.")'),
 ('"<p>This plant belongs to <b>"+esc(owner.nm)+"</b>. You must pay a grid fee of <b>"+fee+"</b> credits. Answer correctly and you only pay half.</p>"','"<p>Dieses Kraftwerk gehört <b>"+esc(owner.nm)+"</b>. Du musst eine Netzgebühr von <b>"+fee+"</b> Talern bezahlen. Antwortest du richtig, zahlst du nur die Hälfte.</p>"'),
 ('log(esc(p.nm)+" pays "+x+" credits grid fee to "+esc(owner.nm)+".")','log(esc(p.nm)+" bezahlt "+esc(owner.nm)+" eine Netzgebühr von "+x+" Talern.")'),
 ('tag:"Event", ic:"⚡"','tag:"Ereignis", ic:"⚡"'),('" · Event “"+e.t+"”: "','" · Ereignis «"+e.t+"»: "'),
 ('{start:"Passing the Town Hall gives you 100 credits. Gas plants push the climate meter up here.", event:"Draw an event card.", quiz:"Answer a question: +50 credits.", stats:"Read a chart or numbers: +70 credits.", summit:"Answer correctly: climate meter −1.", fair:"A harder question: +150 credits.", blackout:"Answer correctly, or you miss your next turn."}',
  '{start:"Wer am Rathaus vorbeizieht, erhält 100 Taler. Hier erhöhen Gaskraftwerke das Klimabarometer.", event:"Ziehe eine Ereigniskarte.", quiz:"Beantworte eine Frage: +50 Taler.", stats:"Lies eine Grafik oder Zahlen: +70 Taler.", summit:"Richtig antworten: Klimabarometer −1.", fair:"Eine schwierigere Frage: +150 Taler.", blackout:"Richtig antworten, sonst setzt du einmal aus."}'),
 ("'<div class=\"pt-facts\"><span>Price: <b>'+t.price+'</b></span><span>Earns: <b>'+t.yield+'</b> per turn (★★ '+(t.yield*2)+')</span><span>Clean bonus: <b>'+t.clean+'</b></span><span>Owner: <b>'+(own!=null?esc(S.players[own].nm):\"nobody\")",
  "'<div class=\"pt-facts\"><span>Preis: <b>'+t.price+'</b></span><span>Ertrag: <b>'+t.yield+'</b> pro Zug (★★ '+(t.yield*2)+')</span><span>Sauberkeitsbonus: <b>'+t.clean+'</b></span><span>Besitz: <b>'+(own!=null?esc(S.players[own].nm):\"niemand\")"),
 ("'<p>The climate meter has reached 10. The lake floods the promenade, and the towns must spend all their money on protection. <b>Everyone loses.</b> Fewer gas plants, more clean energy, and more climate summits next time!</p>'",
  "'<p>Das Klimabarometer hat 10 erreicht. Der See überflutet die Promenade, und die Städte müssen ihr ganzes Geld für den Schutz ausgeben. <b>Alle verlieren.</b> Nächstes Mal: weniger Gaskraftwerke, mehr saubere Energie und mehr Klimagipfel!</p>'"),
 ("'<p>The year is <b>2050</b>. '","'<p>Wir schreiben das Jahr <b>2050</b>. '"),
 ("'The climate meter is low: your towns did a great job together!'","'Das Klimabarometer ist tief: Eure Städte haben gemeinsam grossartige Arbeit geleistet!'"),
 ("'The climate meter is in the middle: good, but there is still work to do.'","'Das Klimabarometer liegt in der Mitte: gut, aber es gibt noch zu tun.'"),
 ("'The climate meter is high: the towns made it, but only just.'","'Das Klimabarometer ist hoch: Die Städte haben es geschafft, aber nur knapp.'"),
 ('<th>Town</th><th class="n">Credits</th><th class="n">Plants</th><th class="n">Clean</th><th class="n">Total</th><th class="n">Answers</th>','<th>Stadt</th><th class="n">Taler</th><th class="n">Kraftwerke</th><th class="n">Sauber</th><th class="n">Total</th><th class="n">Antworten</th>'),
 ('title:S.flood?"The sea has won":"Net zero 2050: "+esc(rows[0].p.nm)+" wins!"','title:S.flood?"Das Wasser hat gewonnen":"Netto-null 2050: "+esc(rows[0].p.nm)+" gewinnt!"'),
 ('{t:"Look at the board", alt:true, f:close}, {t:"New game"','{t:"Spielbrett ansehen", alt:true, f:close}, {t:"Neues Spiel"'),
 ("/Close/.test(","/Schliessen/.test("),
 ("<noscript><p>Please turn on JavaScript to play the game.</p></noscript>","<noscript><p>Bitte JavaScript aktivieren, um das Spiel zu spielen.</p></noscript>"),
]


REPL += [
 ("<div class=\"rd\">Round '+Math.min(S.round,S.rounds)+' of '","<div class=\"rd\">Runde '+Math.min(S.round,S.rounds)+' von '"),
 ('log(esc(p.nm)+" rolls a "+n+(inc?" and earns "+inc+" credits from its plants":"")+".");','log(esc(p.nm)+" würfelt eine "+n+(inc?" und verdient "+inc+" Taler mit den Kraftwerken":"")+".");'),
 ('log(esc(p.nm)+" passes the Town Hall: +100 credits. Its gas plants push the climate meter up by "+g+".");','log(esc(p.nm)+" zieht am Rathaus vorbei: +100 Taler. Die Gaskraftwerke erhöhen das Klimabarometer um "+g+".");'),
 ('log(esc(p.nm)+" passes the Town Hall: +100 credits.");','log(esc(p.nm)+" zieht am Rathaus vorbei: +100 Taler.");'),
 ('log("<b>New round: "+year()+"</b>");','log("<b>Neue Runde: "+year()+"</b>");'),
 ('log(esc(cur().nm)+" misses this turn (blackout).");','log(esc(cur().nm)+" setzt diese Runde aus (Stromausfall).");'),
]
REPL = REPL + FIELDS


def build(src):
    s = src
    a = s.index("/* ================= QUESTIONS"); b = s.index("var used = {};")
    s = s[:a] + "/* ================= FRAGEN ================= */\n" + Q_DE + s[b:]
    a = s.index("var EVENTS = ["); b = s.index("/* ================= STATE")
    s = s[:a] + EVENTS_DE + "\n" + s[b:]
    a = s.index("var RULES = '<ul"); b = s.index("/* ================= SETUP SCREEN")
    s = s[:a] + RULES_DE + "\n" + s[b:]
    miss = []
    for x, y in REPL:
        if x not in s: miss.append(x[:70]); continue
        s = s.replace(x, y)
    return s, miss
