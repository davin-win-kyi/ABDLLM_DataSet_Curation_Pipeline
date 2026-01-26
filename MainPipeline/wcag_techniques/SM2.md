# Technique SM2: Adding extended audio description in SMIL 2.0

## About this Technique

This technique relates to:

* [1.2.3: Audio Description or Media Alternative (Prerecorded)](https://www.w3.org/WAI/WCAG22/Understanding/audio-description-or-media-alternative-prerecorded) (Sufficient when used with [G8: Providing a movie with extended audio descriptions](../general/G8))
* [1.2.5: Audio Description (Prerecorded)](https://www.w3.org/WAI/WCAG22/Understanding/audio-description-prerecorded) (Sufficient when used with [G8: Providing a movie with extended audio descriptions](../general/G8))
* [1.2.7: Extended Audio Description (Prerecorded)](https://www.w3.org/WAI/WCAG22/Understanding/extended-audio-description-prerecorded) (Sufficient when used with [G8: Providing a movie with extended audio descriptions](../general/G8))

This technique applies whenever SMIL 2.0 player is available.

## Description

The purpose of this technique is to allow there to be more audio description than will fit into the gaps in the dialogue of the audio-visual material.

With SMIL 2.0 it is possible to specify that particular audio files be played at particular times, and that the program be frozen (paused) while the audio file is being played.

The effect is that the video appears to play through from end to end but freezes in places while a longer audio description is provided. It then continues automatically when the audio description is complete.

To turn the extended audio description on and off one could use script to switch back and forth between two SMIL scripts, one with and one without the extended audio description lines. Or script could be used to add or remove the extended audio description lines from the SMIL file so that the film clips would just play uninterrupted.

If scripting is not available then two versions of the SMIL file could be provided, one with and one without extended audio description.

## Examples

### Example 1: Video with extended audio description

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
  <excl> 
    <priorityClass peers="pause"> 
      <video src="movie.rm" region="video" title="video" alt="video" /> 
      <audio src="desc1.rm" begin="12.85s" alt="Description 1" /> 
      <audio src="desc2.rm" begin="33.71s" alt="Description 2" /> 
      <audio src="desc3.rm" begin="42.65s" alt="Description 3" /> 
      <audio src="desc4.rm" begin="59.80s" alt="Description 4" /> 
    </priorityClass> 
  </excl> 
</body> 
</smil>
```

## Related Resources

No endorsement implied.

* [Synchronized Multimedia Integration Language (SMIL 2.0)](https://www.w3.org/TR/SMIL/)
* [Synchronized Multimedia Integration Language (SMIL 3.0)](https://www.w3.org/TR/SMIL3/)
* [Accessibility Features of SMIL](https://www.w3.org/TR/SMIL-access/)

## Related Techniques

* [G81: Providing a synchronized video of the sign language interpreter that can be displayed in a different viewport or overlaid on the image by the player](../general/G81)
* [SM7: Providing audio description in SMIL 2.0](../smil/SM7)
* [SM11: Providing captions through synchronized text streams in SMIL 1.0](../smil/SM11)

## Tests

### Procedure

1. Play file with extended audio description
2. Check whether video freezes in places and plays extended audio description

### Expected Results

* #2 is true
