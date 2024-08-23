[Go back to the main page](../../../README.md)

# Table of contents

- [Table of contents](#table-of-contents)
- [Object Oriented Programming - Reported Problems](#object-oriented-programming---reported-problems)
  - [Week 14](#week-14)
    - [7.5 Audio Playback - Files](#75-audio-playback---files)
      - [7.504 Adding a File Chooser](#7504-adding-a-file-chooser)
  - [Week 18](#week-18)
    - [9.2 Adding a moveable playhead](#92-adding-a-moveable-playhead)
      - [9.207 - Implement A Timer](#9207-Implement-a-timer)
  - [Week 19](#week-19)
    - [Vector Subscript Out of Range](#vector-subscript-out-of-range)

# Object Oriented Programming - Reported Problems

This page is about the [Object Oriented Programming module](../../../modules/level-5/cm-2005-object-oriented-programming/).

## Week 14

### 7.5 Audio Playback - Files

#### 7.504 Adding a File Chooser

_"For those of you wondering how to get the file browser working (chooser.browseForFileToOpen does not exist any more) without changing the library preprocessor symbols - use the async version, e.g. like this:"_ - Matthias Truxa

In `MainComponent.h` -> `private:`

```C++
juce::FileChooser chooser{ "Select a file..." };
```

In `MainComponent.cpp` -> `MainComponent::buttonClicked`

```C++
void MainComponent::buttonClicked(Button* button)
{
  if (button == &loadButton)
    {
    auto dlgFlags = 
      juce::FileBrowserComponent::openMode | 
      juce::FileBrowserComponent::canSelectFiles; 

				this->chooser.launchAsync(dlgFlags, 
						[this](const juce::FileChooser& chooser) 
				{
            player1.loadURL(chooser.getURLResult());
				});

        // juce::FileChooser chooser{ "Select a file..." };
        // if (chooser.browseForFileToOpen())
        // {
        //     player1.loadURL(URL{ chooser.getResult() });
        // }
    }
}
```

Note: There is another method where you can add `JUCE_MODAL_LOOPS_PERMITTED=1` to your JUCE preprocessors, but this method is not suggested as any changes you make to your preprocessor might not reflect in the graders' version. This might cause your project to not function as intended.

## Week 18

### 9.2 Adding a moveable playhead

#### 9.207 Implement a timer

_"There's a nasty bug in week 18 video 9.207. When you load a file the application will crash. After a bit of detective work it turns out that as the timer is being called before a file is loaded, the position is NaN (not a number). I found a simple fix for this: "_ - Jamie Jackson

```C++
void WaveformDisplay::setPositionRelative(double pos)
{
  if (pos != position && !isnan(pos))
  {
    position = pos;
    repaint();
  }
}
```

## Week 19

### 10.1 Starter Table Component

#### "Vector Subscript Out of Range"

"_If you try maximising the window you'll get a crash. Inspecting the error message it says vector subscript out of range. So I looked up the paintCell function in the juce API, it says in the description:_
> Note that the rowNumber value may be greater than the number of rows in your list, so be careful that you don't assume it's less than getNumRows().

_So a solution I came up with for the problem is to use getNumRows() and check if rowNum is less than it like in the image below._" - Jamie Jackson

```C++
void PlaylistComponent::paintCell(juce::Graphics& g, int rowNumber, int columnId, int width, int height, bool rowIsSelected)
{
  if (rowNumber < getNumRows())
  {
    g.drawText(trackTitles[rowNumber], 2, 0, width -4, height, juce:Justification::centredleft, true);
  }
}
```
