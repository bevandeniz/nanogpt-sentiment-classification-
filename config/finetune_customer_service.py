import time

out_dir = 'out-gpt2-customer-service'
eval_interval = 30
eval_iters = 50
wandb_log = False # feel free to turn on
wandb_project = 'don'
wandb_run_name = 'ft-' + str(time.time())

dataset = 'customer_service'
init_from = 'gpt2' # this is the GPT-2 model

# only save checkpoints if the validation loss improves
always_save_checkpoint = False

# the number of examples per iter:
batch_size = 12
gradient_accumulation_steps = 32
max_iters = 300
block_size = 128

# finetune at constant LR
learning_rate = 3e-5
decay_lr = False