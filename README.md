# productivityadvisors.com

Static site for Productivity Advisors, hosted on GitHub Pages.

## What's here

| Path | What it is |
|---|---|
| `index.html` | The whole site: masthead, sticky tabs, one panel per tab (About Us, Are We a Fit?, Approach, Services, Customers, Team, Resources), footer, and the pop-out resource viewer |
| `resources/*.html` | One page per resource. Each opens in the pop-out viewer and also works on its own URL |
| `assets/` | Cloud logo and favicons |
| `tools/brand_resources.py` | Adds the Productivity Advisors brand bar to a resource page copied from the gregrobin.com repo |
| `CNAME` | Custom domain for GitHub Pages |

## Tabs and links

Each tab jumps to an anchor on the one page: `#about`, `#fit`, `#approach`, `#services`, `#customers`, `#team`, `#resources`.
Resources deep-link with `#r-<slug>`, for example `productivityadvisors.com/#r-blueprinting`.
"Get in touch" goes to https://www.linkedin.com/in/gnrobin.

## Add a resource

1. Put the HTML file in `resources/`. If it comes from the gregrobin.com repo, add a row to `PAGES` in `tools/brand_resources.py` and run:
   `python3 tools/brand_resources.py <path-to-gregrobin-repo> .`
2. Add one row to the `RESOURCES` list near the bottom of `index.html` (slug, type, title, note, src). The card and viewer are built from that list.

## Publish

1. Create a new GitHub repository (a Pages site can hold only one custom domain, so this can't share the gregrobin.com repo).
2. Upload these files to the repository root, then turn on Pages: Settings → Pages → Deploy from branch → `main` / root.
3. At the domain's DNS host, point `productivityadvisors.com` at GitHub Pages (four A records to GitHub's Pages IPs, plus a `www` CNAME to `<your-user>.github.io`), then tick "Enforce HTTPS" once the certificate is issued.
