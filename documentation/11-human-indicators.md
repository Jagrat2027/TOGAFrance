# TOGAFrance – Chapter 11: Catalogue of Human Indicators

_French version available here: [11-indicateurs-humains-FR.md](./11-indicateurs-humains-FR.md)_

---

The method rejects "indicators empty of human meaning". This catalogue offers the opposite: indicators that measure what people actually live through, each with a simple way to measure it.

A good TOGAFrance indicator answers three questions:

1. **What does it change in someone's life?** If nobody feels it, it is not a human indicator.
2. **Who can measure it, and how?** An indicator without a protocol does not exist.
3. **At what threshold do we act?** Every tracked indicator should be able to feed a reversibility sheet (deliverable 13).

---

## The catalogue

| Code | Indicator | What it says about real life | How to measure it | Frequency |
| --- | --- | --- | --- | --- |
| H-01 | **Real time of a procedure** | How much time a person loses to obtain what they are entitled to | Time 10 real user journeys, from first contact to answer | Quarterly |
| H-02 | **Time to resolve a problem** | How long people stay in difficulty after reporting it | Report date → resolution date, from the issue log | Monthly |
| H-03 | **Number of steps in a procedure** | Perceived complexity | Count screens, forms, trips and documents required for a typical journey | At each change |
| H-04 | **Non-take-up rate** | How many people give up on a right | Estimated eligible − beneficiaries, over eligible (with the relevant service) | Yearly |
| H-05 | **Share of procedures possible without digital** | Who is left behind by "screens only" | For each procedure: is there a counter, a phone line or post? (yes / no) | Yearly |
| H-06 | **User satisfaction** | Lived experience, in people's own words | Single question "Did this service help you?" (yes / partly / no), paper and QR code | Continuous |
| H-07 | **Incidents and endangerment** | Real and perceived safety | Shared log: police, school, residents, staff | Monthly |
| H-08 | **Staff sense of purpose** | Whether those who deliver the service still believe in it | Single anonymous question "Does your work serve people?" (1 to 5) | Twice a year |
| H-09 | **User feedback acted upon** | Whether speaking up changes anything | Feedback that led to a change ÷ feedback received | Quarterly |
| H-10 | **Document comprehension** | Whether plain language is really plain | 5 people read the document, then summarise it: how many understood? | At each version |

---

## Rules of use

- **Few indicators, well tracked.** Three indicators measured every month beat fifteen forgotten ones.
- **Always a qualitative version.** A number without testimony does not say *why*. Add two or three anonymised user quotes to each measurement.
- **Measure before acting.** Record the indicator before the change: without a baseline, there is no way to tell whether things improved.
- **No ranking between territories.** These indicators are for improving, not for sanctioning. An indicator used to punish always ends up gamed.
- **Protect people.** No personal data; surveys are anonymous and optional.

---

## Linking indicators to the rest of the method

Each indicator tracked in a project gets a local identifier (`IND-01`, `IND-02`…) and is linked:

- to one or more **requirements** (deliverable 7), which it verifies;
- optionally to a **reversibility sheet** (deliverable 13), with a trigger threshold;
- to the **monitoring log** (deliverable 14), where it is recorded over time.

These links live in a `tracabilite.yaml` file at the root of the pilot project. The repository's automated check verifies the chain is complete: see the [traffic light example](../pilots-territories/00_example_territory/00_example_city/00_example_feurouge.md/tracabilite.yaml) and [`tools/qualite`](../tools/qualite/README.md).

---

_Previous chapter: [10-appendices.md](./10-appendices.md)_
