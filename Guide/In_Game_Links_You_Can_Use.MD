# In-Game Links You Can Use

Fonte: https://support.travian.com/en/support/solutions/articles/7000092470-in-game-links-you-can-use
Sezione origine: Game Guides

## Cosa insegna

You can trigger common actions by opening special URLs in your browser. Replace the placeholder with your gameworld before using any link:
- Your base: https://XXXXXXX.travian.com/
(e.g., Europe 30 might be https://ts30.x3.europe.travian.com/)

## Quick Navigation

Open a tile by coordinates
https://XXXXXXX.travian.com/position_details.php?x=100&y=-10
Opens the map tile overview for (100|-10).

Open Marketplace with coords prefilled
https://XXXXXXX.travian.com/build.php?gid=17&x=100&y=-10&t=5
Loads Marketplace with (100|-10) set.

## Troop Sending (Rally Point)

Open “Send troops” with coords
https://XXXXXXX.travian.com/build.php?id=39&tt=2&x=100&y=-10
Opens the Send Troops window to (100|-10); default movement = Reinforcement.

Open with exact troops + movement type
- Add/adjust units with &troop[tn]=amount

t1..t6 = tribe units, t7 = rams, t8 = catapults, t9 = settlers, t10 = chiefs, t11 = hero

Add/adjust units with &troop[tn]=amount
- t1..t6 = tribe units, t7 = rams, t8 = catapults, t9 = settlers, t10 = chiefs, t11 = hero
- Choose movement with eventType:

2 Reinforcement, 3 Attack, 4 Raid
Example payload: troop[t1]=20000&troop[t6]=5000&troop[t7]=2000&troop[t8]=700&troop[t11]=1.

Choose movement with eventType:
- 2 Reinforcement, 3 Attack, 4 Raid
Example payload: troop[t1]=20000&troop[t6]=5000&troop[t7]=2000&troop[t8]=700&troop[t11]=1.

Redeploy hero to coords

Useful if you frequently move your hero.

## Gold Club: Create Trade Routes by URL

What each part means:
- did_dest – target village ID (find it from your village list or via map.sql)
- r1..r4 – resources to send (lumber, clay, iron, crop)
- trade_route_mode=deliver (arrive at a set time) or send
- hour / minute – delivery time (use 3 not 03, 0 not 00)
- repeat – number of times (1–3)
- every – frequency in hours (1, 2, 3, 4, 6, 8, 12, 24)

Example above creates 24 routes (every 1 hour) that deliver 11/22/33/44 at 10:16 server time. (Gold Club required.)

## Tips & Good Practice
- Always double-check coordinates and movement type before confirming.
- Keep a personal note of your most-used links with your gameworld prefix already set.
- For village IDs at scale, export or consult map.sql (updated daily at midnight server time) and filter the data.

## Punti chiave operativi
- You can trigger common actions by opening special URLs in your browser. Replace the placeholder with your gameworld before using any link:
- (e.g., Europe 30 might be https://ts30.x3.europe.travian.com/)
- https://XXXXXXX.travian.com/position_details.php?x=100&y=-10
- Opens the map tile overview for (100|-10).
- https://XXXXXXX.travian.com/build.php?gid=17&x=100&y=-10&t=5
- https://XXXXXXX.travian.com/build.php?id=39&tt=2&x=100&y=-10
- Opens the Send Troops window to (100|-10); default movement = Reinforcement.
- https://XXXXXXX.travian.com/build.php?id=39&tt=2&x=100&y=-10 &troop[t1]=19&troop[t8]=1 &c=3&gid=16&eventType=3
- t1..t6 = tribe units, t7 = rams, t8 = catapults, t9 = settlers, t10 = chiefs, t11 = hero
- Example payload: troop[t1]=20000&troop[t6]=5000&troop[t7]=2000&troop[t8]=700&troop[t11]=1.
- https://XXXXXXX.travian.com/build.php?id=39&tt=2&x=-100&y=-10 &troop[t11]=1&c=3&gid=16&eventType=2&redeployHero=1
- Useful if you frequently move your hero.
- https://XXXXXXX.travian.com/build.php? gid=17&t=3
- did_dest – target village ID (find it from your village list or via map.sql)

## Implicazioni strategiche
- Gestisci risorse, produzione e capienza come vincoli principali: spendi prima di raccogliere reward grandi e usa NPC merchant solo quando sblocca timing o previene overflow significativo.
- L'eroe e gli oggetti sono acceleratori: avventure sicure, equip coerente con obiettivo corrente e salute preservata per evitare downtime.
- Ogni scelta militare deve avere ritorno chiaro: profitto, difesa, conquista, demolizione mirata o pressione diplomatica.
- Pianifica territorio e cultura in anticipo: capitale, cropper, oasi e slot espansione decidono la traiettoria mid game.
- Adatta stile e priorita alla tribu: sfrutta bonus naturali invece di seguire una build generica.
