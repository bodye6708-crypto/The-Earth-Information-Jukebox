export type Language = 'ar' | 'en';

export interface QuizQuestion {
  id: number;
  qEn: string;
  qAr: string;
  optionsEn: string[];
  optionsAr: string[];
  correct: number;
  explanationEn: string;
  explanationAr: string;
  source: string;
}

export interface QuizLevel {
  level: number;
  titleEn: string;
  titleAr: string;
  difficulty: string;
  questionCount?: number;
  questions?: QuizQuestion[];
}

export interface ClimateIndicator {
  id: string;
  titleEn: string;
  titleAr: string;
  value: string;
  unit: string;
  observationYear: number;
  source: string;
  sourceUrl: string;
  descriptionEn: string;
  descriptionAr: string;
  category: string;
}

export interface HistoricalClimatePoint {
  year: number;
  anomaly: number;
  co2: number;
  seaLevel: number;
  note: string;
}

export interface GeologicalChapter {
  id: string;
  titleEn: string;
  titleAr: string;
  timespan: string;
  summaryEn: string;
  summaryAr: string;
  contentEn: string;
  contentAr: string;
  sources: string[];
}

export interface PeerPublication {
  id: string;
  title: string;
  authors: string;
  journal: string;
  year: number;
  doi: string;
  url: string;
  abstract: string;
  institution: string;
}

export interface CountryProfile {
  code: string;
  nameEn: string;
  nameAr: string;
  capital: string;
  continent: string;
  coordinates: { lat: number; lng: number };
  established: string;
  areaKm2: number;
  climateClass: string;
  meanAnnualTemp: string;
  geographySummaryEn: string;
  geographySummaryAr: string;
  source: string;
}

export interface StoryChapter {
  chapterNumber: number;
  titleEn: string;
  titleAr: string;
  textEn: string;
  textAr: string;
  audioPrompt?: string;
  interactiveQuestion: {
    qEn: string;
    qAr: string;
    optionsEn: string[];
    optionsAr: string[];
    correct: number;
  };
}

export interface ChildrenStory {
  id: string;
  titleEn: string;
  titleAr: string;
  targetAge: string;
  character: string;
  coverImage: string;
  chapters: StoryChapter[];
}
