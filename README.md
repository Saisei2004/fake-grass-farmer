# Fake Grass Farmer

Fake Grass Farmer is a tiny GitHub Actions setup that farms fake GitHub grass once per day.

Each daily workflow run picks a random number from `0` to `6`. It then creates that many commits by appending success records to `data/fake_grass.log`.

## Files

- `.github/workflows/fake-grass-farmer.yml` - daily GitHub Actions workflow
- `farmer.py` - fixed Python command
- `data/.gitkeep` - keeps the output directory in Git

## Schedule

The workflow runs once per day at `15:15 UTC`, which is `00:15` in Japan Standard Time.

You can also run it manually from the Actions tab with `workflow_dispatch`.

## Command

```bash
python farmer.py --count
python farmer.py --entry-index 1 --entry-total 6
```
