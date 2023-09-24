#!/bin/bash

model_name_or_path=$1
data_path=$2
output_dir=$3

layers_to_freeze=$(seq -s ' ' 1 30)
python fastchat/train/train_mem.py \
	--model_name_or_path "$model_name_or_path" \
	--data_path "$data_path" \
	--fp16 True \
	--output_dir "$output_dir" \
	--num_train_epochs 5 \
	--per_device_train_batch_size 1 \
	--per_device_eval_batch_size 1 \
	--gradient_accumulation_steps 16 \
	--evaluation_strategy "no" \
	--save_strategy "steps" \
	--save_steps 1200 \
	--save_total_limit 10 \
	--learning_rate 2e-5 \
    	--weight_decay 0. \
    	--warmup_ratio 0.03 \
    	--lr_scheduler_type "cosine" \
    	--logging_steps 1 \
  	--tf32 False \
    	--model_max_length 2048 \
    	--gradient_checkpointing True \
    	--lazy_preprocess True \
	--freeze_embed True \
	--freeze_layers_idxs $layers_to_freeze
