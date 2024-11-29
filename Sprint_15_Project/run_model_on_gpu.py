
import pandas as pd

import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet import ResNet50
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout, Flatten
from tensorflow.keras.optimizers import Adam


def load_train(path):
    
    """
    It loads the train part of dataset from path
    """
    
    train_gen = ImageDataGenerator(validation_split = 0.2
                                   ,rescale = 1.0 / 255.0
                                   #,horizontal_flip = True,
                                   #,rotation_range = 20,
                                   #,zoom_range = 0.2
                                   )
    
    df_labels = pd.read_csv(path + 'labels.csv')
    directory = path + 'final_files'
    
    train_gen_flow = train_gen.flow_from_dataframe(
        dataframe = df_labels,
        directory = directory,
        x_col = 'file_name',
        y_col = 'real_age',
        target_size = (150, 150),
        class_mode = 'raw',
        subset = 'training',
        seed = 4321
    )

    return train_gen_flow


def load_test(path):
    
    """
    It loads the validation/test part of dataset from path
    """
    
    test_gen = ImageDataGenerator(validation_split = 0.2
                                  ,rescale = 1.0 / 255.0
                                  #,horizontal_flip = True
                                  #,rotation_range = 20
                                  #,zoom_range = 0.2
                                  )
    
    df_labels = pd.read_csv(path + 'labels.csv')
    directory = path + 'final_files'
    
    test_gen_flow = test_gen.flow_from_dataframe(
        dataframe = df_labels,
        directory = directory,
        x_col = 'file_name',
        y_col = 'real_age',
        target_size =  (150, 150),
        class_mode = 'raw',
        subset = 'validation',
        seed = 4321
    )

    return test_gen_flow


def create_model(input_shape):
    
    """
    Returns a defined model.
    """
    
    base = ResNet50(weights = 'imagenet',
                    input_shape = input_shape)
    
    model = Sequential([
        base,
        GlobalAveragePooling2D(),
        #Dropout(0.2),
        Dense(1, activation = 'relu')
    ])
    
    optimizer = Adam(learning_rate = 0.0005)
    
    model.compile(optimizer = optimizer,
                  loss = 'mse',
                  metrics = ['mae'])

    return model


def train_model(model, 
                train_data, 
                test_data, 
                batch_size=None, 
                epochs=20,
                steps_per_epoch=None, 
                validation_steps=None):

    """
    Trains the model given the parameters
    """
    # Calculate steps for training and validation if not provided
    if steps_per_epoch is None:
        steps_per_epoch = len(train_data)
        
    if validation_steps is None:
        validation_steps = len(test_data)
        
    model.fit(train_data,
              validation_data = test_data,
              batch_size = batch_size,
              epochs = epochs,
              steps_per_epoch = steps_per_epoch,
              valiadtion_steps = validation_steps,
              verbose = 2)
    

    return model


