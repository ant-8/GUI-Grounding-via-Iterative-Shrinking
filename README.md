[![arXiv](https://img.shields.io/badge/arXiv-2411.13591-b31b1b.svg)](https://arxiv.org/abs/2411.13591)

The code for the paper: [Improved GUI Grounding via Iterative Narrowing](https://arxiv.org/abs/2411.13591)

## Abstract

GUI grounding, the task of identifying a precise location on an interface image from a natural language query, plays a crucial role in enhancing the capabilities of Vision-Language Model (VLM) agents. While general VLMs, such as GPT-4V, demonstrate strong performance across various tasks, their proficiency in GUI grounding remains suboptimal. Recent studies have focused on fine-tuning these models specifically for one-shot GUI grounding, yielding significant improvements over baseline performance. We introduce a visual prompting framework called Iterative Narrowing (IN) to further enhance the performance of both general and fine-tuned models in GUI grounding. For evaluation, we tested our method on a comprehensive benchmark comprising different UI platforms.


| Models              | Baseline | IN (n=3)    |
|---------------------|----------|-------|
| InternVL-2-4B       | 4.32     | **6.53**  |
| Qwen2-VL-7B         | 42.89    | **69.1**  |
| OS-Atlas-Base-7B    | 82.47    | **83.33** |

Table 1: Overall average accuracy comparing baseline against our method (IN) on the ScreenSpot
benchmark.

## ScreenSpot Setup

Create a `screenspot/images` directory, then put all the images from the benchmark in it.

## Dependencies

- pillow
- torch
- numpy
- transformers
- qwen_vl_utils

### Citation
```
@misc{nguyen2024improvedguigroundingiterative,
      title={Improved GUI Grounding via Iterative Narrowing}, 
      author={Anthony Nguyen},
      year={2024},
      eprint={2411.13591},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2411.13591}, 
}
```
