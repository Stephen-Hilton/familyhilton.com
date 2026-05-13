# familyhilton.com

The Hilton family's website — a tiny "desktop OS" you can poke around.

| Path | File | What it is |
|---|---|---|
| `/` | `index.html` | **FamilyHiltonOS** — the family desktop: apps for Family, Photos, Travel, and Contact, a working menu bar, a photo lightbox, and launchers for the per-person desktops below. |
| `/stephen` | `stephen.html` | Stephen's desktop — résumé (live from `stephen.skillsnap.me`), a career timeline, a full-screen keynote, plus SkillSnap.me / MakeInfinite / GitHub / LinkedIn. |
| `/joy` | `joy.html` | Joy's desktop — résumé, the American Canyon Community & Parks Foundation, and the Napa River Ecology Center. |
| `/sunny` | `sunny.html` | Sunny's desktop. The golden retriever got to it. |

`assets/` — photos and images used by the pages.

Plain static HTML/CSS/JS — no build step. Deployed to GitHub Pages from `main`
via `.github/workflows/static.yml`; the custom domain is set in `CNAME`.
