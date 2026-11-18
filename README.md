# makefun-news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/zhazha473/makefun-news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/zhazha473/makefun-news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

Entry for make.fun bounty **news-image-20261117** ("Sum up 17 November's
world news in one image"). Free to enter; $250 prize pool, 50 paid places.

## What it is

A one-page newspaper front page summarising the six biggest world stories
of Tuesday, 17 November 2026: the U.S. strikes on Iran's Qeshm Island after
Iranian drone attacks on U.S. targets in Bahrain, Ukraine's renewed strike
on the Crimean Bridge, the first Trump–Xi–Putin trilateral summit in
Shenzhen at the APEC forum, Nvidia's spy-scandal resignation and Wall
Street's fall, the United States losing its measles elimination status, and
Japan scrambling jets as Russian planes entered its airspace amid a day of
network outages.

`main.py` (Python 3.13, standard library only) copies the bundled image
`entry.png` to `/output/entry.png`. No network access; running it twice
produces byte-identical output. The image is 1024x1024 px, under 1 MiB.

The front page was rendered at build time by `build/compose.py` (PIL);
every headline and fact was drawn in code so it is spelled exactly as
researched.

## Run it

```sh
python3 main.py   # writes /output/entry.png
```

## Sources (17 November 2026)

- U.S. strikes Iran: warplanes hit a missile launch site on Qeshm Island
  after Iranian drone attacks on U.S. targets in Bahrain; Trump weighs an
  unverified "dirty bomb" report, Tehran denies it — Reuters / AP via
  https://www.profilenews.com/en/november-17-2026-world-news/ and
  https://www.foreignexchanges.news/p/world-roundup-november-17-2026
- Ukraine: drones and missiles strike the Crimean Bridge; Russia hits
  bridges in Kyiv — AP / Reuters via
  https://www.profilenews.com/en/november-17-2026-world-news/ and
  https://asaspress.com/en/news/world-news-digest-top-stories-of-november-17-2026
- Shenzhen summit: Trump, Xi and Putin set for a first three-way summit at
  the APEC forum; Xi urges free trade — via
  https://www.standardtopic.com/archive/world and
  https://podcastrex.com/shows/world-news-tonight-with-david-muir/full-episode-tuesday-november-17-2026
- Nvidia / markets: ex-CEO Jensen Huang resigns amid a spy scandal, record
  quarterly revenue; AI stocks lead Wall Street lower — AP / Dow Jones via
  https://www.morningstar.com/news/dow-jones/202611176128/dow-jones-top-markets-headlines-at-11-am-et-dow-lower-ahead-of-nvidia-earnings-feds
  and https://podcastrex.com/shows/npr-news-now/5pm-et-november-17-the-latest-headlines-from-npr
- Measles: PAHO announces the United States has lost its measles
  elimination status, the first time since 2000 — via
  https://www.profilenews.com/en/november-17-2026-world-news/
- Security: Japan launches fighters after Russian aircraft violate its
  airspace; NSA internal comms crash amid bank and Microsoft outages — via
  https://asaspress.com/en/news/world-news-digest-top-stories-of-november-17-2026
  and https://www.foreignexchanges.news/p/world-roundup-november-17-2026

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=6dykmzap&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
