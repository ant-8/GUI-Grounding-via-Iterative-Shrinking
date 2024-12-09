[![arXiv](https://img.shields.io/badge/arXiv-2411.13591-b31b1b.svg)](https://arxiv.org/abs/2411.13591)

The code for the paper: [Improved GUI Grounding via Iterative Narrowing](https://arxiv.org/abs/2411.13591)

## Abstract

Graphical User Interface (GUI) grounding plays a crucial role in enhancing the capabilities of Vision-Language Model (VLM) agents. While general VLMs, such as GPT-4V, demonstrate strong performance across various tasks, their proficiency in GUI grounding remains suboptimal. Recent studies have focused on fine-tuning these models specifically for one-shot GUI grounding, yielding significant improvements over baseline performance. We introduce a visual prompting framework that employs an iterative narrowing mechanism to improve the performance of both general and fine-tuned models. In the case of general models, we observed improvements by up to 61%. For evaluation, we tested our method on a comprehensive benchmark comprising various UI platforms and provided the code to reproduce our results.


| Models              | Baseline | IN (n=3)    |
|---------------------|----------|-------|
| InternVL-2-4B       | 4.32     | **6.53**  |
| Qwen2-VL-7B         | 42.89    | **69.1**  |
| OS-Atlas-Base-7B    | 82.47    | **83.33** |

Table 1: Overall average accuracy (%) comparing baseline against our method (IN) on the ScreenSpot
benchmark.

## ScreenSpot Setup

1. Create a `screenspot/images` directory.
2. Follow the steps from [this repository](https://github.com/njucckevin/SeeClick) to download SceenSpot images.
3. Place the images in the recently created directory.

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
