# FollowBench: A Multi-level Fine-grained Constraints Following Benchmark for Large Language Models

we introduce **FollowBench**, a Multi-level Fine-grained Constraints Following Benchmark for LLMs.
- **FollowBench** comprehensively includes five different types (i.e., Content, Scenario, Style, Format, and Example) of _fine-grained constraints_. 
- To enable a precise constraint following estimation on diverse difficulties, we introduce a _Multi-level_ mechanism that incrementally adds a single constraint to the initial instruction at each increased level. 
- To evaluate whether LLMs' outputs have satisfied every individual constraint, we propose to prompt strong LLMs with _constraint-evolution paths_ to handle challenging semantic constraints. 

By evaluating nine closed-source and open-source popular LLMs on FollowBench, we highlight the weaknesses of LLMs in instruction following and point towards potential avenues for future work.


## Data
The data of FollowBench can be found in the [data/](data/).


## How to Implement

### Install Dependencies

```
conda create -n followbench python=3.10
conda activate followbench
conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 pytorch-cuda=11.7 -c pytorch -c nvidia
pip install -r requirements.txt
```

### Model Inference
```bash
cd FollowBench/
python code/model_inference.py --model-path <model_name_or_path>
```

### Evaluation
You should first use GPT-4's API to acquire the LLM-based evaluation results, then we can organize and merge the rule-based evaluation results and LLM-based evaluation results using the following script:
```bash
cd FollowBench/
python code/eval.py --model_names <a_list_of_evaluated_models>
```



## Citation
Please cite our paper if you use the code in this repo.
```
@misc{jiang2023followbench,
      title={FollowBench: A Multi-level Fine-grained Constraints Following Benchmark for Large Language Models}, 
      author={Yuxin Jiang and Yufei Wang and Xingshan Zeng and Wanjun Zhong and Liangyou Li and Fei Mi and Lifeng Shang and Xin Jiang and Qun Liu and Wei Wang},
      year={2023},
      eprint={2310.20410},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
