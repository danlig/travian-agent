# Event Order

Fonte: https://support.travian.com/en/support/solutions/articles/7000060358-event-order
Sezione origine: Advanced Gameplay

## Cosa insegna

Many actions in Travian: Legends are processed as events that occur after a countdown — for example, when troops travel to attack a village, or when a building upgrade finishes. The event order determines in which sequence these actions are completed, especially when multiple things happen at the same time.

### General Event Timing

Events are processed chronologically based on the time they finish.
An event that ends at 10:05:20 will always occur before one that ends at 10:05:21.

### Troops Are Always Last

When multiple events finish in the same second, troop movements are always handled after all other events — such as construction completions or merchant arrivals.

Within troop movements, the order depends on which troops were sent first:
- Troops sent out earlier arrive first, even if another army is scheduled to land at the same second.
- This rule applies to all types of troop movement (attacks, raids, reinforcements, etc.).

Example:
If an attack is already incoming, it is not possible to send reinforcements that arrive in the same second but earlier than that attack.
Reinforcements must reach the village at least one second before the attack to take part in the defense.

However, if reinforcements were already traveling and an attack is sent later — both landing in the same second — the reinforcements will arrive first.

### Building, Merchant, and Other Events

For non-troop events (e.g., building completions, merchant arrivals, or research), the game does not guarantee a fixed order if they occur within the same second.

For instance:
- If a Warehouse finishes construction at the same time a merchant arrives carrying resources, it’s not possible to predict whether the Warehouse completion or the resource delivery will be processed first.

Both will occur before troop movements, but their relative order can vary.

### Events in Different Villages

There is no guaranteed order for events that happen in different villages.
For example:
- If one of your villages is attacked at the same second your own troops reach a target in another village, either event could resolve first.
This behavior is normal and does not affect fairness in battle resolution.

### Instant Actions

Some actions in the game are instant and do not operate through the event queue (they have no countdown).
When triggered, these are typically processed immediately, and their order relative to other ongoing events is not guaranteed.

### Summary

```text
Event Type Order of Resolution
Building completions, merchant arrivals, etc. Before troop events (no guaranteed order between them)
Troop movements (attacks, reinforcements, etc.) After all other events
Simultaneous troop arrivals Based on who sent them first
Events in different villages Randomized order
Instant actions Processed immediately (no fixed position)
```

## Punti chiave operativi
- Events are processed chronologically based on the time they finish.
- An event that ends at 10:05:20 will always occur before one that ends at 10:05:21.
- When multiple events finish in the same second, troop movements are always handled after all other events — such as construction completions or merchant arrivals.
- Within troop movements, the order depends on which troops were sent first:
- Troops sent out earlier arrive first, even if another army is scheduled to land at the same second.
- This rule applies to all types of troop movement (attacks, raids, reinforcements, etc.).
- If an attack is already incoming, it is not possible to send reinforcements that arrive in the same second but earlier than that attack.
- Reinforcements must reach the village at least one second before the attack to take part in the defense.
- However, if reinforcements were already traveling and an attack is sent later — both landing in the same second — the reinforcements will arrive first.
- For non-troop events (e.g., building completions, merchant arrivals, or research), the game does not guarantee a fixed order if they occur within the same second.
- If a Warehouse finishes construction at the same time a merchant arrives carrying resources, it’s not possible to predict whether the Warehouse completion or the resource delivery will be processed first.
- Both will occur before troop movements, but their relative order can vary.
- There is no guaranteed order for events that happen in different villages.
- If one of your villages is attacked at the same second your own troops reach a target in another village, either event could resolve first.

## Implicazioni strategiche
- Gestisci risorse, produzione e capienza come vincoli principali: spendi prima di raccogliere reward grandi e usa NPC merchant solo quando sblocca timing o previene overflow significativo.
- Ogni scelta militare deve avere ritorno chiaro: profitto, difesa, conquista, demolizione mirata o pressione diplomatica.
- Pianifica territorio e cultura in anticipo: capitale, cropper, oasi e slot espansione decidono la traiettoria mid game.
