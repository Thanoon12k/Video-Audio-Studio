# import argparse
# from audio_files_merge import mergeAudioFiles
# from audio_splitter import splitAudioFiles
# from video_to_audio import extractAudioFromVideo

# def main():
#     parser = argparse.ArgumentParser(description='Process audio and video files.')
#     subparsers = parser.add_subparsers(dest='operation')

#     # Extract audio parser
#     extract_parser = subparsers.add_parser('extract', help='Extract audio from a video file')
#     extract_parser.add_argument('--filepath', type=str, required=True, help='Path to the video file')

#     # Split audio parser
#     split_parser = subparsers.add_parser('split', help='Split audio file into segments')
#     split_parser.add_argument('--filepath', type=str, required=True, help='Path to the audio file')
#     split_parser.add_argument('--duration', type=int, required=True, help='Segment duration in seconds')

#     # Merge audio parser
#     merge_parser = subparsers.add_parser('merge', help='Merge audio files')
#     merge_parser.add_argument('--folderpath', type=str, required=True, help='Path to the folder with audio files')

#     args = parser.parse_args()

#     if args.operation == 'extract':
#         audio_path = extractAudioFromVideo(args.filepath)
#         print(f"Audio extracted: {audio_path}")

#     elif args.operation == 'split':
#         segments_path = splitAudioFiles(args.filepath, args.duration)
#         print(f"Audio split into segments at: {segments_path}")

#     elif args.operation == 'merge':
#         merged_file_path = mergeAudioFiles(args.folderpath)
#         print(f"Merged audio file created at: {merged_file_path}")

#     else:
#         parser.print_help()

# if __name__ == "__main__":
#     main()
