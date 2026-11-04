# Darurile filosofiei

Prototip de site editorial cu interfață Decap CMS.

## Vizualizare
Deschide `index.html` într-un server web local (de exemplu `python -m http.server 8000`).

## Publicare și administrare
1. Creează un repository GitHub și încarcă fișierele.
2. În `admin/config.yml`, înlocuiește `INLOCUIESTE_UTILIZATOR/INLOCUIESTE_REPO`.
3. Conectează repository-ul la Netlify și publică site-ul.
4. Configurează autentificarea OAuth pentru Decap CMS/GitHub printr-un furnizor compatibil. Panoul `/admin` nu va putea salva conținut până la finalizarea autentificării.
5. Pentru afișarea automată a articolelor și materialelor pe pagina principală, trebuie adăugat un pas de build care regenerează fișierele `content/posts/index.json` și `content/materiale/index.json`. Prototipul include un script pentru asta.

Nu introduce date private în repository: conținutul site-ului este public.
