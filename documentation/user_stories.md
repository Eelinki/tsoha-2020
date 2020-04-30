# Käyttötapaukset

## Keskeiset ominaisuudet

 * Tunnuksen luonti

```
INSERT INTO account
    (name, username, password) VALUES ("name", "username", "password")
```

 * Ylläpitäjänä lautojen tekeminen (boards)

```
INSERT INTO boards
    (boardname) VALUES ("board name")
```

 * Langan aloittaminen (threads)

```
INSERT INTO threads
    (title, user_id, board_id) VALUES ("title", 1, 1)
```

 * Lankaan vastaaminen

```
INSERT INTO posts
    (message, thread_id, user_id) VALUES ("message", 1, 1)
```

 * Tarkastella käyttäjiä joilla ei ole vielä lankoja

```
SELECT account.username FROM account
    LEFT JOIN thread ON thread.user_id = account.id
    GROUP BY account.id
    HAVING COUNT(thread.id) = 0
```

## User stories

Ylläpitäjillä voi olla useita syitä käyttää keskustelufoorumia:

 * Ylläpidän peliyhteisöä netissä ja laajentaa yhteisöä keskustelufoorumilla
 * Olen yrityksen CFO ja haluan alustan yrityksen sisäiseen viestintään
 * Haluan luoda julkisen keskustelufoorumin autoista ja rakentaa yhteisöä, jonka jäsenillä on yhteinen harrastus
 * Voin moderoida keskustelufoorumia poistamalla lankoja.

Käyttäjät voivat hyödyntää keskustelufoorumia:

 * Etsin tietoa lemmikkieläimistä ja jakaa omia vinkkejäni
 * Löysin nettikaupan ja haluan jakaa sen muiden harrastajien kesken
 * Voin poistaa tekemäni langan, koska se ei ole enää ajankohtaista
 * Voin muokata lankani otsikkoa pitääkseni sen relevanttina.