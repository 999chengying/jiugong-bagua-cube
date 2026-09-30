

```markdown
# 3.0 文件清单

## 根目录

- `README.md`：3.0 总览
- `CHANGELOG.md`：版本记录
- `LICENSE`：MIT

## docs/

| 文件 | 内容 |
|---|---|
| `00-overview.md` | 总览 |
| `01-jiugong.md` | 九宫编码器与剪枝 |
| `02-cycle.md` | 二十四山循环 |
| `03-55-50.md` | 天地之数 55 与大衍之数 50 |
| `04-four-images.md` | 四象结构 24/28/32/36 |
| `05-recursive-fault-tolerance.md` | 递归容错与虚实转换 |
| `06-ai-architecture.md` | AI 帝宫架构 |
| `07-military-analogy.md` | 军事理论映射 |
| `08-experiment-checklist.md` | 实验清单 |
| `09-file-manifest.md` | 本文件 |
| `figures/README.md` | 图目录说明 |

## src/

| 文件 | 功能 |
|---|---|
| `jiugong_encoder.py` | 四数形态分类 |
| `pruning.py` | 剪枝规则库 |
| `cycle_analysis.py` | 二十四山循环分析 |
| `four_images.py` | 四象结构 |
| `fault_tolerance.py` | 递归容错模拟 |
| `fifty_model.py` | 大衍之数 50 模型 |
| `fiftyfive_model.py` | 天地之数 55 模型 |

## tests/

| 文件 | 覆盖 |
|---|---|
| `test_encoder.py` | 编码器与剪枝 |
| `test_cycle.py` | K=5~9 循环 |
| `test_four_images.py` | 四象 |
| `test_fault_tolerance.py` | 容错 |
| `test_fifty_model.py` | 50 模型 |
| `test_fiftyfive_model.py` | 55 模型 |

## data/

| 文件 | 内容 |
|---|---|
| `faces.json` | 六表面 |
| `diagonals.json` | 六对角截面 |
| `generating_pairs.json` | 生成对与合十对 |
| `24_mountains.json` | 二十四山 |
| `cycles.json` | K=5~9 结果 |
| `four_images.json` | 四象 |
| `55_50_models.json` | 55/50 模型 |

## benchmark/

| 文件 | 内容 |
|---|---|
| `run_benchmark.py` | A/B 组 token 对比 |
| `test_cases.json` | 测试用例 |
| `report_template.md` | 报告模板 |

## 运行入口

```bash
python src/jiugong_encoder.py 1 6 7 8
python src/cycle_analysis.py 5 子
python src/four_images.py
python src/fault_tolerance.py
python src/fifty_model.py
python src/fiftyfive_model.py
python benchmark/run_benchmark.py
python -m unittest discover tests
```

版本

· 1.0：编码器 + 剪枝
· 2.0：循环分析
· 2.1：Benchmark
· 3.0：55/50、四象、容错、AI 帝宫架构

```

---
