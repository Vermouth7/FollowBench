import argparse
import os

from gpt4_based_evaluation import (save_csl_evaluation,
                                   save_discriminative_evaluation)
from rule_based_evaluation import (save_csl_example_constraint,
                                   save_evaluate_example_constraint)


def main(args):

    ### rule-based evaluation
    save_evaluate_example_constraint(
                                    data_path=args.data_path, 
                                    api_output_path=args.api_output_path, 
                                    model_names=args.model_paths,
                                    evaluation_result_path=args.evaluation_result_path
        )
    
    save_csl_example_constraint(
                                data_path=args.data_path, 
                                api_output_path=args.api_output_path,
                                model_names=args.model_paths,
                                evaluation_result_path=args.evaluation_result_path
                                )


    ### LLM-based evaluation
    for constraint_type in args.constraint_types:
        save_discriminative_evaluation(
                                        data_path=args.data_path,
                                        api_output_path=args.api_output_path,
                                        data_gpt4_discriminative_eval_input_path=args.data_gpt4_discriminative_eval_input_path, 
                                        gpt4_discriminative_eval_output_path=args.gpt4_discriminative_eval_output_path, 
                                        constraint_type=constraint_type, 
                                        model_names=args.model_paths,
                                        evaluation_result_path=args.evaluation_result_path
                                    )
        
        save_csl_evaluation(
                            data_path=args.data_path,
                            api_output_path=args.api_output_path,
                            data_gpt4_discriminative_eval_input_path=args.data_gpt4_discriminative_eval_input_path, 
                            gpt4_discriminative_eval_output_path=args.gpt4_discriminative_eval_output_path, 
                            constraint_type=constraint_type, 
                            model_names=args.model_paths,
                            evaluation_result_path=args.evaluation_result_path
                            )
    
    print(f"\nEvaluation finished!\nThe evaluation results have been saved in '{args.evaluation_result_path}'.")
        


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_paths", nargs='+', type=str, required=True, help="Paths or names of the models to be evaluated.")
    parser.add_argument("--constraint_types", nargs='+', type=str, default=['content', 'situation', 'style', 'format', 'mixed'])
    parser.add_argument("--data_path", type=str, default="data")
    parser.add_argument("--api_output_path", type=str, default="/home/chh/repos/my_ctg/results/followbench/res9")
    parser.add_argument("--data_gpt4_discriminative_eval_input_path", type=str, default="data_gpt4_discriminative_eval_input")
    parser.add_argument("--gpt4_discriminative_eval_output_path", type=str, default="/home/chh/repos/my_ctg/results/followbench/res9/eval_output")
    parser.add_argument("--evaluation_result_path", type=str, default="res9")
    # parser.add_argument("--model_paths", nargs='+', type=str, required=True, help="Paths or names of the models to be evaluated.")
    # parser.add_argument("--constraint_types", nargs='+', type=str, default=['content', 'situation', 'style', 'format', 'mixed'])
    # parser.add_argument("--data_path", type=str, default="data")
    # parser.add_argument("--api_output_path", type=str, default="api_output")
    # parser.add_argument("--data_gpt4_discriminative_eval_input_path", type=str, default="data_gpt4_discriminative_eval_input")
    # parser.add_argument("--gpt4_discriminative_eval_output_path", type=str, default="gpt4_discriminative_eval_output")
    # parser.add_argument("--evaluation_result_path", type=str, default="evaluation_result")

    args = parser.parse_args()

    if not os.path.exists(args.evaluation_result_path):
        os.makedirs(args.evaluation_result_path)

    main(args)
