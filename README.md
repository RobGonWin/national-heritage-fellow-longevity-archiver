# National Heritage Fellow Longevity Archiver

Independent source-bound archival comparison of National Heritage Fellowship recipients and identified group members. No NEA endorsement is asserted.

[Explore the comparison](https://robgonwin.github.io/national-heritage-fellow-longevity-archiver/site/)
· [Research spreadsheet](https://docs.google.com/spreadsheets/d/1S6qyeGziZLWRqTXUA9Twg6NCyQ-ccSGWu8aMJVZ_e-I/edit)

The 2026-10-23 research checkpoint contains 502 awards, 473 named fellows and 584 identified subjects. 493 awards are fully resolved under the accepted evidence, or 494 including the conditional screen; eight collective membership boundaries remain open. Roma Wilson is first among the current identified comparison population under accepted evidence and assumptions. A universal historical maximum is not established.

`data/public` contains the complete CSV, JSON, source register and eight-tab editable workbook. Possible rank intervals, source roles, reported ages, screening bounds and exact lifespans stay distinct. Sorting does not establish an official longevity rank.

```sh
python public_offline.py --data data/public
python -m pip install -e . pytest
pytest -q
python build_web.py
python -m http.server 8080 --bind 127.0.0.1 --directory build
```

The static explorer works from the downloaded build without network access except when opening original sources. CI performs offline validation and tests; no repository secrets are required. Source-image links do not grant redistribution rights. No image files, private vault or private history are published.

Methods and synthetic tests are available in `src/nea_archiver` and `tests`. Authenticated research and the complete local media vault belong to the separate private installation. Read `LOOP.md` and `docs/reproduction.md` before changing a snapshot.
