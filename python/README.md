# CS50P solutions

Logic that several problem sets share lives in [`shared/`](shared); each week's
script keeps only its own prompts and printing.

| Module | Contents |
| --- | --- |
| `shared/prompts.py` | `prompt_until`, `prompt_int`, `iter_until_eof` — the re-prompt and read-until-EOF loops |
| `shared/text.py` | `remove_vowels`, `camel_to_snake` |
| `shared/fuel.py` | `convert`, `gauge` |
| `shared/plates.py` | `is_valid` |
| `shared/bank.py` | `value` |

Because the scripts import `shared`, run them from this directory as modules:

```
cd python
python -m week5.fuel
python -m pytest
```
