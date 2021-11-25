# Freelance Token recognition

If you input

```py

dict_toks("hello * world /")

```

It'll output

```py

{'*': 'TOKEN', 'hello': '*_subtext', '/': 'TOKEN', 'world': '/_subtext'}

```

It's mainly used for analysis, not for production.