# Fake Grass Farmer

Fake Grass Farmer is a tiny GitHub Actions setup that runs one fixed Python command once per day.

The command writes a success record to `data/fake_grass.log`. The workflow commits that file back to the repository, so the daily run leaves a persistent trace.

## Files

- `.github/workflows/fake-grass-farmer.yml` - daily GitHub Actions workflow
- `farmer.py` - fixed Python command
- `data/.gitkeep` - keeps the output directory in Git

## Schedule

The workflow runs once per day at `15:15 UTC`, which is `00:15` in Japan Standard Time.

You can also run it manually from the Actions tab with `workflow_dispatch`.

## Command

```bash
python farmer.py
```

