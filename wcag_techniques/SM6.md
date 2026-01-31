# Technique SM6: Providing audio description in SMIL 1.0

## About this Technique

This technique relates to:

* [1.2.3: Audio Description or Media Alternative (Prerecorded)](https://www.w3.org/WAI/WCAG22/Understanding/audio-description-or-media-alternative-prerecorded) (Sufficient when used with [G173: Providing a version of a movie with audio descriptions](../general/G173))
* [1.2.5: Audio Description (Prerecorded)](https://www.w3.org/WAI/WCAG22/Understanding/audio-description-prerecorded) (Sufficient when used with [G173: Providing a version of a movie with audio descriptions](../general/G173))

This technique applies whenever SMIL 1.0 player is available.

## Description

The objective of this technique is to provide a way for people who are blind or otherwise have trouble seeing the video in audio-visual material to be able to access the material. With this technique a description of the video is provided via audio description that will fit into the gaps in the dialogue in the audio-visual material.

## Examples

### Example 1: SMIL 1.0 audio description sample for QuickTime player

```xml
<?xml version="1.0" encoding="UTF-8"?>
<smil xmlns:qt="http://www.apple.com/quicktime/resources/smilextensions" 
      xmlns="https://www.w3.org/TR/REC-smil" qt:time-slider="true">
<head>
  <layout>
    <root-layout background-color="black" height="266" width="320"/>
    <region id="videoregion" background-color="black" top="26" left="0" 
      height="144" width="320"/>
  </layout>
</head>
<body>
  <par>
    <video dur="0:01:20.00" region="videoregion" src="salesdemo.mov" 
     alt="Sales Demo"/>
    <audio dur="0:01:20.00" src="salesdemo_ad.mp3" 
     alt="Sales Demo Audio Description"/>
  </par>
</body>
</smil>
```

## Related Resources

No endorsement implied.

* [Synchronized Multimedia Integration Language (SMIL 2.0)](https://www.w3.org/TR/SMIL/)
* [Synchronized Multimedia Integration Language (SMIL 3.0)](https://www.w3.org/TR/SMIL3/)
* [Accessibility Features of SMIL](https://www.w3.org/TR/SMIL-access/)

## Related Techniques

* [SM2: Adding extended audio description in SMIL 2.0](../smil/SM2)
* [SM7: Providing audio description in SMIL 2.0](../smil/SM7)

## Tests

### Procedure

1. Find method for turning on audio description from content/player (unless it is always played by default)
2. Play file with audio description
3. Check whether audio description is played

### Expected Results

* #3 is true
