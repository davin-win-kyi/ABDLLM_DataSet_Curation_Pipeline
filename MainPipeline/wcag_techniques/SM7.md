# Technique SM7: Providing audio description in SMIL 2.0

## About this Technique

This technique relates to:

* [1.2.3: Audio Description or Media Alternative (Prerecorded)](https://www.w3.org/WAI/WCAG22/Understanding/audio-description-or-media-alternative-prerecorded) (Sufficient when used with [G173: Providing a version of a movie with audio descriptions](../general/G173))
* [1.2.5: Audio Description (Prerecorded)](https://www.w3.org/WAI/WCAG22/Understanding/audio-description-prerecorded) (Sufficient when used with [G173: Providing a version of a movie with audio descriptions](../general/G173))

This technique applies whenever SMIL 2.0 player is available.

## Description

The objective of this technique is to provide a way for people who are blind or otherwise have trouble seeing the video in audio-visual material to be able to access the material. With this technique a description of the video is provided via audio description that will fit into the gaps in the dialogue in the audio-visual material.

## Examples

### Example 1: SMIL 2.0 audio description sample for RealMedia player

```xml
<smil xmlns="https://www.w3.org/2001/SMIL20/Language">
<head>
  <layout>
    <root-layout backgroundColor="black" height="266" width="320"/>
    <region id="video" backgroundColor="black" top="26" left="0" 
     height="144" width="320"/>
  </layout>
  </head>
  <body>
    <par>
      <video src="salesdemo.mpg" region="video" title="Sales Demo" 
      alt="Sales Demo"/>
      <audio src="salesdemo_ad.mp3" begin="33.71s" title="audio description" 
      alt="Sales Demo Audio Description"/>
    </par>
  </body>
</smil>
```

The example shows a par segment containing an audio and a video tag. The audio stream is not started immediately.

## Related Resources

No endorsement implied.

* [Synchronized Multimedia Integration Language (SMIL 2.0)](https://www.w3.org/TR/SMIL/)
* [Synchronized Multimedia Integration Language (SMIL 3.0)](https://www.w3.org/TR/SMIL3/)
* [Accessibility Features of SMIL](https://www.w3.org/TR/SMIL-access/)

## Related Techniques

* [SM2: Adding extended audio description in SMIL 2.0](../smil/SM2)
* [SM6: Providing audio description in SMIL 1.0](../smil/SM6)

## Tests

### Procedure

1. Find method for turning on audio description from content/player (unless it is always played by default)
2. Play file with audio description
3. Check whether audio description is played

### Expected Results

* #3 is true
