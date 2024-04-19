import tensorflow as tf
from keras import Input
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator


class PyDataset(tf.data.Dataset):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Call superclass constructor with all arguments
        self._warn_if_super_not_called()


train_dir = 'training'
validation_dir = 'validation'
test_dir = 'testing'

# Generators for our training, validation, and testing data
train_datagen = ImageDataGenerator(rescale=1. / 255)
val_datagen = ImageDataGenerator(rescale=1. / 255)
test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(150, 150),
    batch_size=20,
    class_mode='categorical')

validation_generator = val_datagen.flow_from_directory(
    validation_dir,
    target_size=(150, 150),
    batch_size=20,
    class_mode='categorical')

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(150, 150),
    batch_size=20,
    class_mode='categorical')

# Defining our model
model = Sequential([
    Input(shape=(150, 150, 3)),
    Conv2D(16, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Conv2D(32, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Conv2D(64, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(4)  # We have 4 classes: glass, metal, paper, plastic
])

# Compile the model
model.compile(optimizer='adam',
              loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Train the model
history = model.fit(
    train_generator,
    steps_per_epoch=len(train_generator),
    epochs=10,
    validation_data=validation_generator,
    validation_steps=len(validation_generator)
)

# Evaluate the model on the test data
score = model.evaluate(test_generator, steps=len(test_generator))
print('Test loss:', score[0])
print('Test accuracy:', score[1])

# images, labels = next(train_generator)
#
# # Set up a matplotlib figure with subplots
# fig, axes = plt.subplots(4, 4, figsize=(10, 10))
# axes = axes.flatten()
#
# # Define class names
# class_names = ['glass', 'metal', 'paper', 'plastic']
#
# # Loop through the images and labels
# for i in range(16):
#     # Display the image
#     axes[i].imshow(images[i])
#
#     # Get the label of the current image (one-hot encoded)
#     label = labels[i]
#
#     # Find the index of the class with a value of 1 (indicating the class)
#     class_index = label.argmax()
#
#     # Get the corresponding class name
#     class_name = class_names[class_index]
#
#     # Set the title of the subplot to the class name
#     axes[i].set_title(class_name)
#
#     # Remove axes
#     axes[i].axis('off')
#
# plt.tight_layout()
# plt.show()
