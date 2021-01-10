"""
This file is part of the AniSearch Discord Bot.

Copyright (C) 2021 IchBinLeoon

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

SEARCH_USER_QUERY = '''
query ($search: String){
  User(search: $search) {
    id
    name
    avatar {
      large
      medium
    }
    about
    bannerImage
    statistics {
      anime {
        count
        meanScore
        minutesWatched
        episodesWatched
      }
      manga {
        count
        meanScore
        chaptersRead
        volumesRead
      }
    }
    mediaListOptions {
      scoreFormat
      rowOrder
      useLegacyLists
      sharedTheme
      sharedThemeEnabled
      animeList {
        splitCompletedSectionByFormat
        theme
        advancedScoringEnabled
      }
      mangaList {
        splitCompletedSectionByFormat
        theme
        advancedScoringEnabled
      }
    }
    favourites {
      anime {
        edges {
          id
          node {
            id
            siteUrl
            title {
              romaji
              english
              native
              userPreferred
            }
          }
        }
      }
      manga {
        edges {
          id
          node {
            id
            siteUrl
            title {
              romaji
              english
              native
              userPreferred
            }
          }
        }
      }
      characters {
        edges {
          id
          node {
            id
            siteUrl
            name {
              first
              last
              full
              native
            }
          }
        }
      }
      staff {
        edges {
          id
          node{
            id
            siteUrl
            name {
              first
              last
              full
              native
            }
          }
        }
      }
      studios {
        edges {
          id
          node {
            id
            siteUrl
            name
          }
        }
      }
    }
    siteUrl
  }
}
'''