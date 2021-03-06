experiment_name = "NONE"
experiment_description = "scene segmentation using images only"

# overall confg
data_root = '../../dataset/structruing/structuring_dataset_test_5k'
shot_frm_path = data_root + "/shot_txt"  
video_name = "test"
shot_num = 4
seq_len = 2
gpus = "0"

# dataset settings
dataset = dict(
    name="demo",
    mode=['place', 'aud'],
)
# model settings
model = dict(
    name='LGSS',
    # backbone='resnet50',
    place_feat_dim=2048,
    aud_feat_dim=512,
    aud=dict(cos_channel=512),
    fix_resnet=False,
    sim_channel=512,  # dim of similarity vector
    bidirectional=True,
    lstm_hidden_size=512,
    ratio=[0.8,0, 0, 0.2]
    )

# optimizer
optim = dict(name='SGD',
             setting=dict(lr=1e-2, weight_decay=5e-4))
stepper = dict(name='MultiStepLR',
               setting=dict(milestones=[15]))
loss = dict(weight=[0.5, 5])

# runtime settings
resume = None
trainFlag = False
testFlag = True
batch_size = 32
epochs = 30
logger = dict(log_interval=200, logs_dir="../run/{}".format(experiment_name))
data_loader_kwargs = dict(num_workers=1, pin_memory=True, drop_last=False)
